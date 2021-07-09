from datetime import datetime, date, timedelta
import json
from re import L

from servicestack.utils import to_timespan

from requests.models import HTTPError, Response

from servicestack.client_dtos import IDelete, IGet, IPatch, IPost, IPut, IReturn, IReturnVoid, ResponseStatus, KeyValuePair
from servicestack.log import Log
from servicestack.utils import *

from typing import Callable, TypeVar, Generic, Optional, Dict, List, Tuple, get_args, Any, Type
from dataclasses import dataclass, field, fields, asdict, is_dataclass, Field
from dataclasses_json import dataclass_json, LetterCase, Undefined, config, mm
from urllib.parse import urljoin, urlencode, quote_plus
from stringcase import camelcase, snakecase
import marshmallow.fields as mf
import requests
import base64
import decimal

JSON_MIME_TYPE = "application/json"

class Bytes(mf.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return to_bytearray(value)

    def _deserialize(self, value, attr, data, **kwargs):
        return from_bytearray(value)

mm.TYPES[timedelta] = mf.DateTime
mm.TYPES[KeyValuePair] = KeyValuePair[str,str]
mm.TYPES[bytes] = Bytes
mm.TYPES[Bytes] = Bytes

@dataclass
class A:
    l: list
    li: list[int]
    gl: List[int]
    ol: Optional[List[int]]
    od: Optional[Dict[int,str]]
    int_:int = field(metadata=config(field_name="@name"), default=0)
    int_string_map: Optional[Dict[int,str]] = None

def dump(obj):
  print("")
  for attr in dir(obj):
    print(f"obj.{attr} = {getattr(obj, attr)}")
  print("")

def _resolve_response_type(request):
    if isinstance(request, IReturn):
        for cls in request.__orig_bases__:
            if hasattr(cls,'__args__'):
                return cls.__args__[0]
    if isinstance(request, IReturnVoid):
        return type(None)
    return None

def resolve_httpmethod(request):
    if isinstance(request, IGet):
        return "GET"
    if isinstance(request, IPost):
        return "POST"
    if isinstance(request, IPut):
        return "PUT"
    if isinstance(request, IPatch):
        return "PATCH"
    if isinstance(request, IDelete):
        return "DELETE"
    return "POST"

def nameof(instance):
    return type(instance).__name__

def qsvalue(arg):
    if not arg: 
        return ""
    arg_type = type(arg)
    if arg_type is str:
        return quote_plus(arg)
    if arg_type is bytes or arg_type is bytearray:
        return base64.b64encode(arg).decode("utf-8")
    return quote_plus(str(arg))

def append_querystring(url:str, args:dict[str,Any]):
    if args:
        for key in args:
            val = args[key]
            if (val is None): continue
            url += '&' if '?' in url else '?'
            url += key + '=' + qsvalue(val)
    return url

def has_request_body(method:str):
    return not (method == "GET" or method == "DELETE" or method == "HEAD" or method == "OPTIONS")

def _empty(x):
    return x is None or x == {} or x == []

def _clean_list(d:list):
    return [v for v in (clean_any(v) for v in d) if not _empty(v)]

def _clean_dict(d:dict):
    return {k: v for k, v in ((k, clean_any(v)) for k, v in d.items()) if not _empty(v)}

def clean_any(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary"""
    if not isinstance(d, (dict, list)):
        return d
    elif isinstance(d, list):
        return _clean_list(d)
    else:
        return _clean_dict(d)

def _json_encoder(obj:Any):
    if is_dataclass(obj):
        return clean_any(asdict(obj))
    if hasattr(obj,'__dict__'):
        return vars(obj)
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    if isinstance(obj, timedelta):
        #a=timedelta(days=1,hours=1,minutes=1,seconds=1,milliseconds=1)
        return to_timespan(obj)
    if isinstance(obj, bytes):
        return base64.b64encode(obj).decode('ascii')
    raise TypeError(f"Unsupported Type in JSON encoding: {type(obj)}")

def json_encode(obj:Any):
    if is_dataclass(obj):
        # return obj.to_json()
        return json.dumps(clean_any(obj.to_dict()), default=_json_encoder)
    return json.dumps(obj, default=_json_encoder)

def _json_decoder(obj:Any):
    # print('ZZZZZZZZZZZZZZZZZ')
    # print(type(obj))
    return obj

class TypeConverters:
    converters: dict[Type, Callable[[Any],Any]]
    
    def register(type:Type, converter:Callable[[Any],Any]):
        TypeConverters.converters[type] = converter

TypeConverters.converters = {
    mf.Integer: int,
    mf.Float: float,
    mf.Decimal: decimal.Decimal,
    mf.String: str,
    mf.Boolean: bool,
    mf.DateTime: from_datetime,
    mf.TimeDelta: from_timespan,
    Bytes: from_bytearray,
    bytes: from_bytearray,
}

def is_optional(cls:Type): return f"{cls}".startswith("typing.Optional")
def is_list(cls:Type): return f"{cls}".startswith("typing.List")
def is_dict(cls:Type): return f"{cls}".startswith("typing.Dict")

def generic_arg(cls:Type): return cls.__args__[0]
def generic_args(cls:Type): return cls.__args__
def unwrap(cls:Type):
    if is_optional(cls):
        return generic_arg(cls)
    return cls

def dict_get(name:str, obj:dict, case:Callable[[str],str] = None):
    if name in obj: return obj[name]
    if case:
        nameCase = case(name)
        if nameCase in obj: return obj[nameCase]
    nameSnake = snakecase(name)
    if nameSnake in obj: return obj[nameSnake]
    nameCamel = camelcase(name)
    if nameCamel in obj: return obj[nameCamel]
    if name.endswith('_'):
        return dict_get(name.rstrip('_'), obj, case)
    return None

def convert(into:Type, obj:Any):
    if obj is None: return None
    into = unwrap(into)
    if is_dataclass(into):
        to = {}
        for f in fields(into):
            val = dict_get(f.name, obj)            
            to[f.name] = convert(f.type, val)
            # print(f"to[{f.name}] = {to[f.name]}")
        return into(**to)
    elif is_list(into):
        el_type = generic_arg(into)
        to = []
        for item in obj:
            to.append(convert(el_type, item))
        return to
    elif is_dict(into):
        key_type, val_type = generic_args(into)
        to = {}
        for key, val in obj.items():
            to_key = convert(key_type, key)
            to_val = convert(val_type, val)
            to[to_key] = to_val
        return to
    else:
        if into in TypeConverters.converters:
            converter = TypeConverters.converters[into]
            try:
                return converter(obj)
            except Exception as e:
                Log.error(f"ERROR converter(obj) {into}({obj})", e)
                raise e
        else:
            # print(f"TRY {obj} into {into}")
            try:
                return into(obj)
            except Exception as e:
                Log.error(f"ERROR into(obj) {into}({obj})", e)
                raise e

def ex_message(e:Exception):
    if hasattr(e,'message'):
        return e.message
    return str(e)

def log(o:Any):
    print(o)
    return o

@dataclass
class SendContext:
    headers: dict[str,str] = None
    method: str = None
    url: str = None
    request: IReturn = None
    body: Any = None
    body_string: str = None
    args: dict[str,str] = None
    response_as: type = None
    request_filter:Callable[[Any],None] = None
    response_filter:Callable[[Response],None] = None

class WebServiceException(Exception):
    status_code: int = None
    status_description: str = None
    message: str = None
    inner_exception: Exception = None
    response_status:ResponseStatus = None

class JsonServiceClient:
    base_url: str = None
    reply_base_url: str = None
    oneway_base_url: str = None
    headers: dict[str,str] = None
    bearer_token: str = None
    username: str = None
    password: str = None
    max_retries = 5
    use_token_cookie = False
    global_request_filter:Callable[[SendContext],None] = None #static
    request_filter:Callable[[SendContext],None] = None
    global_response_filter:Callable[[Response],None] = None   #static
    response_filter:Callable[[Response],None] = None

    def __init__(self,base_url):
        if not base_url:
            raise TypeError(f"base_url is required")
        self.base_url = base_url
        self.reply_base_url = urljoin(base_url,'json/reply') + "/"
        self.oneway_base_url = urljoin(base_url,'json/oneway') + "/"
        self.headers = { 'Accept': JSON_MIME_TYPE }

    def create_url_from_dto(self, method:str, request:Any):
        url = urljoin(self.reply_base_url, nameof(request))
        if not has_request_body(method):
            url = append_querystring(url, request.__dict__)
        return url

    def get(self,request,args=None):
        return self.send(request,"GET",None,args)
    def post(self,request,body=None,args=None):
        return self.send(request,"POST",body,args)
    def put(self,request,body=None,args=None):
        return self.send(request,"PUT",body,args)
    def patch(self,request,body=None,args=None):
        return self.send(request,"PATCH",body,args)
    def delete(self,request,args=None):
        return self.send(request,"DELETE",None,args)
    def options(self,request,args=None):
        return self.send(request,"OPTIONS",None,args)
    def head(self,request,args=None):
        return self.send(request,"HEAD",None,args)

    def to_absolute_url(self, path_or_url:str):
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            return path_or_url
        return urljoin(self.base_url, path_or_url)

    def get_url(self, path:str, response_as:Type, args:dict[str,Any]=None):
        return self.send_url("GET", path, response_as, None, args)
    def delete_url(self, path:str, response_as:Type, args:dict[str,Any]=None):
        return self.send_url("DELETE", path, response_as, None, args)
    def options_url(self, path:str, response_as:Type, args:dict[str,Any]=None):
        return self.send_url("OPTIONS", path, response_as, None, args)
    def head_url(self, path:str, response_as:Type, args:dict[str,Any]=None):
        return self.send_url("HEAD", path, response_as, None, args)

    def post_url(self, path:str, body:Any=None, response_as:Type=None, args:dict[str,Any]=None):
        return self.send_url("POST", path, response_as, body, args)
    def put_url(self, path:str, body:Any=None, response_as:Type=None, args:dict[str,Any]=None):
        return self.send_url("PUT", path, response_as, body, args)
    def patch_url(self, path:str, body:Any=None, response_as:Type=None, args:dict[str,Any]=None):
        return self.send_url("PATCH", path, response_as, body, args)

    def send_url(self, method:str, path:str, response_as:Type=None, body=None, args:dict[str,Any]=None):

        if body and not response_as:
            response_as = _resolve_response_type(body)

        info = SendContext(
            headers=self.headers,
            method=method,
            url=self.to_absolute_url(path),
            request=None,
            body=body,
            body_string=None,
            args=args,
            response_as=response_as)

        return self.send_request(info)

    def send(self,request,method,body=None,args=None):
        if not isinstance(request, IReturn) and not isinstance(request, IReturnVoid):
            raise TypeError(f"'{nameof(request)}' does not implement IReturn or IReturnVoid")

        response_as = _resolve_response_type(request)
        if response_as is None:
            raise TypeError(f"Could not resolve Response Type for '{nameof(request)}'")

        return self.send_request(SendContext(
            headers=self.headers,
            method=method or resolve_httpmethod(request),
            url=None,
            request=request,            
            body=body,
            body_string=None,
            args=args,
            response_as=response_as))

    def _resend_request(self, info):
        if has_request_body(info.method):
            headers = info.headers.copy() if info.headers else []
            headers['Content-Type'] = JSON_MIME_TYPE
            response = requests.request(info.method, info.url, data=info.body_string, headers=headers)
        else:
            response = requests.request(info.method, info.url, headers=info.headers)
        response.raise_for_status()
        return response

    def _create_response(self, response:Response, info:SendContext):

        if info.response_filter:
            info.response_filter(response)
        if self.response_filter:
            self.response_filter(response)
        if JsonServiceClient.global_response_filter:
            JsonServiceClient.global_response_filter(response)

        into = info.response_as

        if into is bytes:
            return response.content

        json_str = response.text
        if Log.debug_enabled: Log.debug(f"json_str: {json_str}")

        if not into:
            return json.loads(json_str)

        if into is str:
            return json_str

        try:
            # res_dto = into.schema().loads(json_str, object_hook=_json_decoder)

            json_obj = json.loads(json_str)
            res_dto = convert(into, json_obj)
        except Exception as e:
            Log.error(f"Failed to deserialize into {into}: {e}", e)
            raise e

        return res_dto

    def _raise_error(self, e:Exception):
        return e

    def _handle_error(self, hold_res:Response, e:Exception):
        if e is WebServiceException:
            raise self._raise_error(e)

        web_ex = WebServiceException()
        web_ex.inner_exception = e
        web_ex.status_code = 500
        web_ex.status_description = ex_message(e)

        if e is HTTPError:
            web_ex.status_code = e.response.status_code
            if Log.debug_enabled: Log.debug(f"{e}")

        if hold_res:
            pass

        raise web_ex
        
    def send_request(self, info:SendContext):
        try:
            url = info.url
            body = info.body or info.request
            if not url:
                body_not_request_dto = info.request and info.body
                if body_not_request_dto:
                    url = urljoin(self.reply_base_url, nameof(info.request))
                    url = append_querystring(url, clean_any(asdict(info.request)))
                else:
                    url = self.create_url_from_dto(info.method, body)

            if not url:
                raise TypeError

            if info.args:
                url = append_querystring(url, info.args)
        except Exception as e:
            if Log.debug_enabled(): Log.debug(f"send_request(): {ex_message(e)}")
            return self._handle_error(None, e)

        info.url = url
        if info.request_filter:
            info.request_filter(info)
        if self.request_filter:
            self.request_filter(info)
        if JsonServiceClient.global_request_filter:
            JsonServiceClient.global_request_filter(info)

        if has_request_body(info.method):
            if type(body) is str:
                info.body_string = body
            else:
                info.body_string = json_encode(body)

        Log.debug(f"info method: {info.method}, url: {info.url}, body_string: {info.body_string}")
        response:Response = None
        try:
            response = self._resend_request(info)
            res_dto = self._create_response(response,info)
    
            if Log.debug_enabled(): Log.debug(f"res_dto = {type(res_dto)}")
    
            return res_dto
        except Exception as e:
            if Log.debug_enabled(): Log.debug(f"send_request() create_response: {ex_message(e)}")
            return self._handle_error(response, e)


