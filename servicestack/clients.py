import decimal
import inspect
import json
import requests
import typing
from enum import Enum
from requests.exceptions import HTTPError
from requests.models import Response

from dataclasses import field, fields, asdict, is_dataclass
from typing import Callable, get_args, Type, get_origin, ForwardRef, Union
from urllib.parse import urljoin, quote_plus
from stringcase import camelcase, snakecase

from servicestack.dtos import *
from servicestack.fields import *
from servicestack.log import Log

JSON_MIME_TYPE = "application/json"
AUTHORIZATION_HEADER = "Authorization"
CONTENT_TYPE = "Content-Type"
SS_TOKEN_COOKIE = "ss-tok"
SS_REFRESH_TOKEN_COOKIE = "ss-reftok"


def _dump(obj):
    print("")
    for attr in dir(obj):
        print(f"obj.{attr} = {getattr(obj, attr)}")
    print("")


def _resolve_response_type(request):
    if isinstance(request, IReturn):
        for cls in request.__orig_bases__:
            if hasattr(cls, '__args__'):
                candidate = cls.__args__[0]
                if type(candidate) == ForwardRef:
                    return _resolve_forwardref(candidate, type(request))
                return candidate
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


def append_querystring(url: str, args: dict[str, Any]):
    if args:
        for key in args:
            val = args[key]
            if val is None:
                continue
            url += '&' if '?' in url else '?'
            url += key + '=' + qsvalue(val)
    return url


def has_request_body(method: str):
    return not (method == "GET" or method == "DELETE" or method == "HEAD" or method == "OPTIONS")


def _empty(x):
    return x is None or x == {} or x == []


def _clean_list(d: list):
    return [v for v in (clean_any(v) for v in d) if not _empty(v)]


def _clean_dict(d: dict):
    return {k: v for k, v in ((k, clean_any(v)) for k, v in d.items()) if not _empty(v)}


def clean_any(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary"""
    if not isinstance(d, (dict, list)):
        return d
    elif isinstance(d, list):
        return _clean_list(d)
    else:
        return _clean_dict(d)


def _json_encoder(obj: Any):
    if is_dataclass(obj):
        return clean_any(asdict(obj))
    if hasattr(obj, '__dict__'):
        return vars(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, timedelta):
        return to_timespan(obj)
    if isinstance(obj, bytes):
        return base64.b64encode(obj).decode('ascii')
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(f"Unsupported Type in JSON encoding: {type(obj)}")


def to_json(obj: Any):
    if is_dataclass(obj):
        return json.dumps(clean_any(obj.to_dict()), default=_json_encoder)
    return json.dumps(obj, default=_json_encoder)


class TypeConverters:
    deserializers: dict[Type, Callable[[Any], Any]]

    @staticmethod
    def register_deserializer(cls: Type, deserializer: Callable[[Any], Any]):
        TypeConverters.deserializers[cls] = deserializer


TypeConverters.deserializers = {
    mf.DateTime: from_datetime,
    mf.TimeDelta: from_timespan,
}


def is_optional(cls: Type): return f"{cls}".startswith("typing.Optional")


def is_list(cls: Type):
    return cls == typing.List or cls == list or get_origin(cls) == list


def is_dict(cls: Type):
    return cls == typing.Dict or cls == dict or get_origin(cls) == dict


def generic_arg(cls: Type): return generic_args(cls)[0]


def generic_args(cls: Type):
    if not hasattr(cls, '__args__'):
        raise TypeError(f"{cls} is not a Generic Type")
    return cls.__args__


def _resolve_forwardref(cls: Type, orig: Type = None):
    type_name = cls.__forward_arg__
    if orig is not None and orig.__name__ == type_name:
        return orig
    if type_name not in globals():
        raise TypeError(f"Could not resolve ForwardRef('{type_name}')")
    return globals()[type_name]


def unwrap(cls: Type):
    if type(cls) == ForwardRef:
        cls = _resolve_forwardref(cls)
    if is_optional(cls):
        return generic_arg(cls)
    return cls


def dict_get(name: str, obj: dict, case: Callable[[str], str] = None):
    if name in obj:
        return obj[name]
    if case:
        name_case = case(name)
        if name_case in obj:
            return obj[name_case]
    name_snake = snakecase(name)
    if name_snake in obj:
        return obj[name_snake]
    name_camel = camelcase(name)
    if name_camel in obj:
        return obj[name_camel]
    if name.endswith('_'):
        return dict_get(name.rstrip('_'), obj, case)
    return None


def _resolve_type(cls: Type, substitute_types: Dict[Type, type]):
    if substitute_types is None:
        return cls
    return substitute_types[cls] if cls in substitute_types else cls


def convert(into: Type, obj: Any, substitute_types: Dict[Type, type] = None):
    if obj is None:
        return None
    into = unwrap(into)
    into = _resolve_type(into, substitute_types)
    if Log.debug_enabled():
        Log.debug(f"convert({into}, {obj})")

    generic_def = get_origin(into)
    if generic_def is not None and is_dataclass(generic_def):
        reified_types = {}
        generic_type_args = get_args(into)
        i = 0
        for t in generic_def.__parameters__:
            reified_types[t] = generic_type_args[i]
            i += 1
        return convert(generic_def, obj, reified_types)

    if is_dataclass(into):
        to = {}
        for f in fields(into):
            val = dict_get(f.name, obj)
            # print(f"to[{f.name}] = convert({f.type}, {val}, {substitute_types})")
            to[f.name] = convert(f.type, val, substitute_types)
            # print(f"to[{f.name}] = {to[f.name]}")
        return into(**to)
    elif is_list(into):
        el_type = _resolve_type(generic_arg(into), substitute_types)
        to = []
        for item in obj:
            to.append(convert(el_type, item, substitute_types))
        return to
    elif is_dict(into):
        key_type, val_type = generic_args(into)
        key_type = _resolve_type(key_type, substitute_types)
        val_type = _resolve_type(val_type, substitute_types)
        to = {}
        for key, val in obj.items():
            to_key = convert(key_type, key, substitute_types)
            to_val = convert(val_type, val, substitute_types)
            to[to_key] = to_val
        return to
    else:
        if into in TypeConverters.deserializers:
            converter = TypeConverters.deserializers[into]
            try:
                return converter(obj)
            except Exception as e:
                Log.error(f"converter(obj) {into}({obj})", e)
                raise e
        elif inspect.isclass(into) and issubclass(into, mf.Field):
            try:
                return into().deserialize(obj)
            except Exception as e:
                Log.error(f"into().deserialize(obj) {into}({obj})", e)
                raise e
        else:
            try:
                return into(obj)
            except Exception as e:
                Log.error(f"into(obj) {into}({obj})", e)
                raise e


def from_json(into: Type, json_str: str):
    if json_str is None or json_str == "":
        return None
    json_obj = json.loads(json_str)
    return convert(into, json_obj)


def ex_message(e: Exception):
    if hasattr(e, 'message'):
        return e.message
    return str(e)


def log(o: Any):
    print(o)
    return o


@dataclass_json
@dataclass
class SendContext:
    session: Optional[requests.Session] = None
    headers: dict[str, str] = field(default_factory=dict)
    method: str = None
    url: Optional[str] = None
    request: Optional[Union[IReturn, IReturnVoid, List[IReturn], List[IReturnVoid]]] = None
    body: Optional[Any] = None
    body_string: Optional[str] = None
    args: Optional[dict[str, str]] = None
    response_as: type = None
    request_filter: Callable[[Any], None] = None
    response_filter: Callable[[Response], None] = None

    def exec(self):
        if has_request_body(self.method):
            if CONTENT_TYPE not in self.headers:
                self.headers[CONTENT_TYPE] = JSON_MIME_TYPE
        else:
            if CONTENT_TYPE in self.headers:
                self.headers.pop(CONTENT_TYPE)

        if Log.debug_enabled():
            using = "requests"
            if self.session is not None:
                using = "session"
                Log.debug(f"{using}.cookies: {self.session.cookies}")
                # if "ss-tok" in self.session.cookies:
                #     ss_tok = self.session.cookies["ss-tok"]
                #     print('ss_tok', inspect_jwt(ss_tok))
            Log.debug(f"{using}.request({self.method}): url={self.url}, headers={self.headers}, data={self.body_string}")

        response: Optional[Response] = None
        if has_request_body(self.method):
            if self.session is not None:
                response = self.session.request(self.method, self.url, data=self.body_string, headers=self.headers)
            else:
                response = requests.request(self.method, self.url, data=self.body_string, headers=self.headers)
        else:
            if self.session is not None:
                response = self.session.request(self.method, self.url, headers=self.headers)
            else:
                response = requests.request(self.method, self.url, headers=self.headers)

        if Log.debug_enabled():
            if self.response_as is not bytes:
                Log.debug(f"response.text: {response.text}")
            else:
                Log.debug(f"response.content len: {len(response.content)}")
            Log.debug(f"response.cookies[{len(response.cookies)}]: {response.cookies}")

        return response


class WebServiceExceptionType(Enum):
    DEFAULT = 1
    REFRESH_TOKEN_EXCEPTION = 2


class WebServiceException(Exception):
    status_code: int = None
    status_description: str = None
    message: str = None
    inner_exception: Exception = None
    response_status: ResponseStatus = None
    type: WebServiceExceptionType = WebServiceExceptionType.DEFAULT


T = TypeVar('T')


class JsonServiceClient:
    base_url: str = None
    reply_base_url: str = None
    oneway_base_url: str = None
    headers: Optional[Dict[str, str]] = None
    bearer_token: Optional[str] = None
    refresh_token: Optional[str] = None
    refresh_token_uri: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    max_retries: int = 5
    use_token_cookie = False
    global_request_filter: Callable[[SendContext], None] = None  # static
    request_filter: Callable[[SendContext], None] = None
    global_response_filter: Callable[[Response], None] = None  # static
    response_filter: Callable[[Response], None] = None
    exception_filter: Callable[[Response, Exception], None] = None
    global_exception_filter: Callable[[Response, Exception], None] = None
    on_authentication_required: Callable[[], None] = None

    _session: requests.Session = None

    def __init__(self, base_url):
        if not base_url:
            raise TypeError(f"base_url is required")
        self.base_url = base_url
        self.reply_base_url = urljoin(base_url, 'json/reply') + "/"
        self.oneway_base_url = urljoin(base_url, 'json/oneway') + "/"
        self.headers = {'Accept': JSON_MIME_TYPE}
        self._session = requests.Session()

    def set_credentials(self, username, password):
        self.username = username
        self.password = password
        return self

    def set_bearer_token(self, bearer_token):
        self.bearer_token = bearer_token
        return self

    def set_refresh_token(self, refresh_token):
        self.refresh_token = refresh_token
        return self

    def _get_cookie_value(self, name: str) -> Optional[str]:
        if self._session is not None and name in self._session.cookies:
            return self._session.cookies[name]
        return None

    @property
    def token_cookie(self): return self._get_cookie_value(SS_TOKEN_COOKIE)

    @property
    def refresh_token_cookie(self): return self._get_cookie_value(SS_REFRESH_TOKEN_COOKIE)

    def create_url_from_dto(self, method: str, request: Any):
        url = urljoin(self.reply_base_url, nameof(request))
        if not has_request_body(method):
            url = append_querystring(url, request.__dict__)
        return url

    def get(self, request: IReturn[T], args: Dict[str, Any] = None) -> T:
        return self.send(request, "GET", None, args)

    def post(self, request: IReturn[T], body: Any = None, args: Dict[str, Any] = None) -> T:
        return self.send(request, "POST", body, args)

    def put(self, request: IReturn[T], body: Any = None, args: Dict[str, Any] = None) -> T:
        return self.send(request, "PUT", body, args)

    def patch(self, request: IReturn[T], body: Any = None, args: Dict[str, Any] = None) -> T:
        return self.send(request, "PATCH", body, args)

    def delete(self, request: IReturn[T], args: Dict[str, Any] = None) -> T:
        return self.send(request, "DELETE", None, args)

    def options(self, request: IReturn[T], args: Dict[str, Any] = None) -> T:
        return self.send(request, "OPTIONS", None, args)

    def head(self, request: IReturn[T], args: Dict[str, Any] = None) -> T:
        return self.send(request, "HEAD", None, args)

    def to_absolute_url(self, path_or_url: str):
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            return path_or_url
        return urljoin(self.base_url, path_or_url)

    def get_url(self, path: str, response_as: Type, args: dict[str, Any] = None):
        return self.send_url(path, "GET", response_as, None, args)

    def delete_url(self, path: str, response_as: Type, args: dict[str, Any] = None):
        return self.send_url(path, "DELETE", response_as, None, args)

    def options_url(self, path: str, response_as: Type, args: dict[str, Any] = None):
        return self.send_url(path, "OPTIONS", response_as, None, args)

    def head_url(self, path: str, response_as: Type, args: dict[str, Any] = None):
        return self.send_url(path, "HEAD", response_as, None, args)

    def post_url(self, path: str, body: Any = None, response_as: Type = None, args: dict[str, Any] = None):
        return self.send_url(path, "POST", response_as, body, args)

    def put_url(self, path: str, body: Any = None, response_as: Type = None, args: dict[str, Any] = None):
        return self.send_url(path, "PUT", response_as, body, args)

    def patch_url(self, path: str, body: Any = None, response_as: Type = None, args: dict[str, Any] = None):
        return self.send_url(path, "PATCH", response_as, body, args)

    def send_url(self, path: str, method: str = None, response_as: Type = None, body: Any = None, args: dict[str, Any] = None):

        if body and not response_as:
            response_as = _resolve_response_type(body)

        info = SendContext(
            session=self._session,
            headers=self.headers.copy(),
            method=method or resolve_httpmethod(body),
            url=self.to_absolute_url(path),
            request=None,
            body=body,
            body_string=None,
            args=args,
            response_as=response_as)

        return self.send_request(info)

    def send(self, request, method="POST", body: Any = None, args: Dict[str, Any] = None):
        if not isinstance(request, IReturn) and not isinstance(request, IReturnVoid):
            raise TypeError(f"'{nameof(request)}' does not implement IReturn or IReturnVoid")

        response_as = _resolve_response_type(request)
        if response_as is None:
            raise TypeError(f"Could not resolve Response Type for '{nameof(request)}'")

        return self.send_request(SendContext(
            session=self._session,
            headers=self.headers.copy(),
            method=method or resolve_httpmethod(request),
            url=None,
            request=request,
            body=body,
            body_string=None,
            args=args,
            response_as=response_as))

    def assert_valid_batch_request(self, requests: list):
        if not isinstance(requests, list):
            raise TypeError(f"'{nameof(requests)}' is not a List")

        if len(requests) == 0:
            return []

        request = requests[0]
        if not isinstance(request, IReturn) and not isinstance(request, IReturnVoid):
            raise TypeError(f"'{nameof(request)}' does not implement IReturn or IReturnVoid")

        item_response_as = _resolve_response_type(request)
        if item_response_as is None:
            raise TypeError(f"Could not resolve Response Type for '{nameof(request)}'")
        return request, item_response_as

    def send_all(self, requests: List[IReturn[T]]):
        request, item_response_as = self.assert_valid_batch_request(requests)
        url = urljoin(self.reply_base_url, nameof(request) + "[]")

        return self.send_request(SendContext(
            session=self._session,
            headers=self.headers.copy(),
            method="POST",
            url=url,
            request=list(requests),
            body=None,
            body_string=None,
            args=None,
            response_as=list.__class_getitem__(item_response_as)))

    def send_all_oneway(self, requests: list):
        request, item_response_as = self.assert_valid_batch_request(requests)
        url = urljoin(self.oneway_base_url, nameof(request) + "[]")

        self.send_request(SendContext(
            session=self._session,
            headers=self.headers.copy(),
            method="POST",
            url=url,
            request=list(requests),
            body=None,
            body_string=None,
            args=None,
            response_as=list.__class_getitem__(item_response_as)))

    def _resend_request(self, info: SendContext):

        if self.bearer_token is not None:
            info.headers[AUTHORIZATION_HEADER] = f"Bearer {self.bearer_token}"
        elif self.username is not None:
            info.headers[AUTHORIZATION_HEADER] = \
                "Basic " + base64.b64encode(f"{self.username}:{self.password}".encode('ascii')).decode('ascii')

        response = info.exec()

        try:
            response.raise_for_status()
            res_dto = self._create_response(response, info)
            return res_dto, response
        except Exception as e:
            raise self._handle_error(response, e)

    def _create_response(self, response: Response, info: SendContext):

        if info.response_filter:
            info.response_filter(response)
        if self.response_filter:
            self.response_filter(response)
        if JsonServiceClient.global_response_filter:
            JsonServiceClient.global_response_filter(response)

        if len(response.cookies) > 0 and SS_REFRESH_TOKEN_COOKIE in response.cookies:
            self.use_token_cookie = True

        into = info.response_as

        if into is bytes:
            return response.content

        json_str = response.text

        if into is None:
            return json.loads(json_str)

        if into is str:
            return json_str

        try:
            res_dto = from_json(into, json_str)
        except Exception as e:
            Log.error(f"Failed to deserialize into {into}: {e}", e)
            raise e

        return res_dto

    def _raise_error(self, res: Response, e: Exception) -> Exception:
        if self.exception_filter:
            self.exception_filter(res, e)
        if JsonServiceClient.global_exception_filter:
            JsonServiceClient.global_exception_filter(res, e)
        return e

    def _handle_error(self, hold_res: Optional[Response], e: Exception, kind: Optional[WebServiceExceptionType] = None):
        if type(e) == WebServiceException:
            raise self._raise_error(hold_res, e)

        web_ex = WebServiceException()
        web_ex.inner_exception = e
        web_ex.status_code = 500
        web_ex.status_description = ex_message(e)
        if kind is not None:
            web_ex.type = kind

        res = hold_res
        if type(e) == HTTPError and e.response is not None:
            res = e.response

        if res is not None:
            if Log.debug_enabled():
                Log.debug(f"error.text: {res.text}")
            web_ex.status_code = res.status_code
            web_ex.status_description = res.reason

            web_ex.response_status = ResponseStatus(
                error_code=f"{res.status_code}",
                message=res.reason)

            try:
                error_response: EmptyResponse = from_json(EmptyResponse, res.text)
                if error_response is not None:
                    web_ex.response_status = error_response.response_status
            except Exception as ex:
                Log.error(f"Could not deserialize error response {res.text}", ex)

        raise self._raise_error(res, web_ex)

    def create_request(self, info: SendContext):
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
            if Log.debug_enabled():
                Log.debug(f"send_request(): {ex_message(e)}")
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
                info.body_string = to_json(body)

        return info

    def send_request(self, info: SendContext):
        info = self.create_request(info)
        if Log.debug_enabled():
            Log.debug(f"info method: {info.method}, url: {info.url}, body_string: {info.body_string}")
        response: Optional[Response] = None
        try:
            res_dto, response = self._resend_request(info)

            if Log.debug_enabled():
                Log.debug(f"res_dto = {type(res_dto)}")

            return res_dto
        except Exception as e:
            if Log.debug_enabled():
                Log.debug(f"send_request() create_response: {ex_message(e)}")

            has_refresh_token_cookie = False
            if self.refresh_token is not None or self.use_token_cookie or has_refresh_token_cookie:
                Log.debug("attempting to refresh bearer_token with refresh_token")
                jwt_request = GetAccessToken(refresh_token=self.refresh_token)
                url = self.refresh_token_uri or self.create_url_from_dto("POST", jwt_request)

                try:
                    jwt_info = SendContext(
                        session=self._session,
                        headers=self.headers.copy(),
                        method="POST",
                        request=jwt_request,
                        url=url,
                        response_as=_resolve_response_type(jwt_request))
                    jwt_info = self.create_request(jwt_info)
                    jwt_res = jwt_info.exec()
                    jwt_res.raise_for_status()
                    jwt_response: GetAccessTokenResponse = self._create_response(jwt_res, jwt_info)
                    self.bearer_token = jwt_response.access_token
                    Log.debug("send_request() bearer_token refreshed")
                    if AUTHORIZATION_HEADER in info.headers:
                        info.headers.pop(AUTHORIZATION_HEADER)
                    res_dto, response = self._resend_request(info)
                    return res_dto
                except Exception as jwt_ex:
                    if Log.debug_enabled():
                        Log.debug(f"send_request() jwt_ex: {jwt_ex}")
                    return self._handle_error(response, jwt_ex, WebServiceExceptionType.REFRESH_TOKEN_EXCEPTION)

            if self.on_authentication_required is not None:
                self.on_authentication_required()
                res_dto, response = self._resend_request(info)
                return res_dto

            return self._handle_error(response, e)
