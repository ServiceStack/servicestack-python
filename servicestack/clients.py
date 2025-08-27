import base64
import json
from dataclasses import dataclass, field
from enum import Enum
from typing_extensions import Type, get_origin
from typing import Callable, Union, ForwardRef
from typing import TypeVar, Optional, Dict, List, Any
from urllib.parse import urljoin, quote_plus

import requests
from dataclasses_json import dataclass_json
from requests.exceptions import HTTPError
from requests.models import Response,RequestField, encode_multipart_formdata

from dataclasses import dataclass
from typing import BinaryIO, List, Optional, TypeVar, Union
import mimetypes

from servicestack.types import IDeleteDb, IPatchDb, IReturn, IReturnVoid, IGet, IPost, IPut, IPatch, \
    IDelete, IUpdateDb, QueryBase, ResponseStatus, EmptyResponse, GetAccessToken, GetAccessTokenResponse
from servicestack.log import Log
from servicestack.reflection import TypeConverters, to_dict, nameof, is_list, is_dict, _resolve_forwardref, \
    has_type_vars, _dict_with_string_keys, _get_type_vars_map, from_json, to_json, to_jsv_data
from servicestack.utils import ex_message, clean_camelcase


JSON_MIME_TYPE = "application/json"
AUTHORIZATION_HEADER = "Authorization"
CONTENT_TYPE = "Content-Type"
SS_TOKEN_COOKIE = "ss-tok"
SS_REFRESH_TOKEN_COOKIE = "ss-reftok"


def _resolve_response_type(request):
    t = type(request)

    def resolve_response_type():
        if isinstance(request, IReturn):
            for cls in t.__orig_bases__:
                if get_origin(cls) == IReturn and hasattr(cls, '__args__'):
                    candidate = cls.__args__[0]
                    if type(candidate) == ForwardRef:
                        return _resolve_forwardref(candidate, type(request))
                    return candidate
        if isinstance(request, IReturnVoid):
            return type(None)
        return None

    if hasattr(t, 'response_type'):
        ret = t.response_type()
        if has_type_vars(ret):
            # avoid reifying type vars if request type has concrete type return marker
            ret_candidate = resolve_response_type()
            if not has_type_vars(ret_candidate):
                return ret_candidate

            type_map = _dict_with_string_keys(_get_type_vars_map(t))
            if isinstance(ret, TypeVar):
                return get_origin(ret).__class_getitem__(type_map[f"{ret}"])
            reified_args = [type_map[f"{x}"] for x in ret.__args__]
            reified_type = get_origin(ret).__class_getitem__(*reified_args)
            return reified_type
        return ret
    else:
        return resolve_response_type()


def resolve_httpmethod(request):
    if isinstance(request, IGet) or isinstance(request, QueryBase):
        return "GET"
    if isinstance(request, IPost):
        return "POST"
    if isinstance(request, IPut) or isinstance(request, IUpdateDb):
        return "PUT"
    if isinstance(request, IPatch) or isinstance(request, IPatchDb):
        return "PATCH"
    if isinstance(request, IDelete) or isinstance(request, IDeleteDb):
        return "DELETE"
    return "POST"


def qsvalue(arg):
    if arg is None:
        return ""
    arg_type = type(arg)
    if arg_type == bool:
        return f"{arg}".lower()
    if is_list(arg_type):
        return "[" + ','.join([qsvalue(x) for x in arg]) + "]"
    if is_dict(arg_type):
        return "{" + ','.join([k + ":" + qsvalue(v) for k, v in arg]) + "}"
    if arg_type is str:
        return quote_plus(arg)
    if issubclass(arg_type, Enum):
        return qsvalue(arg.value)
    if arg_type in TypeConverters.serializers:
        return TypeConverters.serialize(arg)
    return quote_plus(str(arg))


def append_querystring(url: str, args: Dict[str, Any]):
    if args:
        for key in args:
            val = args[key]
            # print("append_querystring", key, val)
            if val is None:
                continue
            url += '&' if '?' in url else '?'
            qs_val = qsvalue(val)
            if qs_val is not None:
                url += key + '=' + qs_val
    return url


def has_request_body(method: str):
    return not (method == "GET" or method == "DELETE" or method == "HEAD" or method == "OPTIONS")


def combine_with(base_url: str, relative_url: str):
    if not base_url:
        return relative_url
    if not relative_url:
        return base_url
    # We want to handle relative urls different by maintaining the base_url path at all times
    temp_relative_url = relative_url
    temp_base_url = base_url
    if not temp_base_url.endswith("/"):
        temp_base_url += "/"
    if temp_relative_url.startswith("/"):
        temp_relative_url = temp_relative_url[1:]
    return urljoin(temp_base_url, temp_relative_url)

@dataclass_json
@dataclass
class SendContext:
    session: Optional[requests.Session] = None
    headers: Dict[str, str] = field(default_factory=dict)
    method: str = None
    url: Optional[str] = None
    request: Optional[Union[IReturn, IReturnVoid, List[IReturn], List[IReturnVoid]]] = None
    body: Optional[Any] = None
    body_string: Optional[str] = None
    args: Optional[Dict[str, str]] = None
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
            Log.debug(
                f"{using}.request({self.method}): url={self.url}, headers={self.headers}, data={self.body_string}")

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

@dataclass
class UploadFile:
    field_name: Optional[str]
    file_name: Optional[str]
    content_type: Optional[str]
    stream: BinaryIO

    def __post_init__(self):
        if not self.content_type and self.file_name:
            guessed_type = mimetypes.guess_type(self.file_name)[0]
            self.content_type = guessed_type or 'application/octet-stream'

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
    use_token_cookie = False
    global_request_filter: Callable[[SendContext], None] = None  # static
    request_filter: Callable[[SendContext], None] = None
    global_response_filter: Callable[[Response], None] = None  # static
    response_filter: Callable[[Response], None] = None
    exception_filter: Callable[[Response, Exception], None] = None
    global_exception_filter: Callable[[Response, Exception], None] = None
    on_authentication_required: Callable[[], None] = None

    _session: requests.Session = None

    def __init__(self, base_url:str):
        if not base_url:
            raise TypeError(f"base_url is required")
        self.base_url = base_url
        self._session = requests.Session()
        self.headers = {'Accept': JSON_MIME_TYPE}
        self.set_base_path('api')

    def set_base_path(self, base_path:str=''):
        if not base_path:
            self.reply_base_url = combine_with(self.base_url, 'json/reply') + "/"
            self.oneway_base_url = combine_with(self.base_url, 'json/oneway') + "/"
        else:
            self.reply_base_url = combine_with(self.base_url, base_path) + "/"
            self.oneway_base_url = combine_with(self.base_url, base_path) + "/"
        return self

    def set_credentials(self, username:str, password:str):
        self.username = username
        self.password = password
        return self

    def set_bearer_token(self, bearer_token:str):
        self.bearer_token = bearer_token
        return self

    def set_refresh_token(self, refresh_token:str):
        self.refresh_token = refresh_token
        return self

    def _get_cookie_value(self, name: str) -> Optional[str]:
        if self._session is not None and name in self._session.cookies:
            return self._session.cookies[name]
        return None

    @property
    def token_cookie(self):
        return self._get_cookie_value(SS_TOKEN_COOKIE)

    @property
    def refresh_token_cookie(self):
        return self._get_cookie_value(SS_REFRESH_TOKEN_COOKIE)

    def create_url_from_dto(self, method: str, request: Any):
        url = combine_with(self.reply_base_url, nameof(request))
        if not has_request_body(method):
            url = append_querystring(url, to_dict(request, key_case=clean_camelcase))
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
        return combine_with(self.base_url, path_or_url)

    def get_url(self, path: str, response_as: Type, args: Dict[str, Any] = None):
        return self.send_url(path, "GET", response_as, None, args)

    def delete_url(self, path: str, response_as: Type, args: Dict[str, Any] = None):
        return self.send_url(path, "DELETE", response_as, None, args)

    def options_url(self, path: str, response_as: Type, args: Dict[str, Any] = None):
        return self.send_url(path, "OPTIONS", response_as, None, args)

    def head_url(self, path: str, response_as: Type, args: Dict[str, Any] = None):
        return self.send_url(path, "HEAD", response_as, None, args)

    def post_url(self, path: str, body: Any = None, response_as: Type = None, args: Dict[str, Any] = None):
        return self.send_url(path, "POST", response_as, body, args)

    def put_url(self, path: str, body: Any = None, response_as: Type = None, args: Dict[str, Any] = None):
        return self.send_url(path, "PUT", response_as, body, args)

    def patch_url(self, path: str, body: Any = None, response_as: Type = None, args: Dict[str, Any] = None):
        return self.send_url(path, "PATCH", response_as, body, args)

    def send_url(self, path: str, method: str = None, response_as: Type = None, body: Any = None,
                 args: Dict[str, Any] = None):

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

    def send(self, request, method: Any = None, body: Any = None, args: Dict[str, Any] = None):
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

    def post_file_with_request(self, request: IReturn[T], file: UploadFile) -> T:
        """
        Post file with a request DTO using multipart/form-data

        :param request: The request DTO
        :param files: Single UploadFile or List of UploadFile objects
        :return: Response DTO
        """
        return self.post_files_with_request_url(combine_with(self.reply_base_url, nameof(request)), request, [file])

    def post_file_with_request_url(self, request_uri: str, request: IReturn[T], file: UploadFile) -> T:
        """
        Post file with a request DTO using multipart/form-data

        :param request_uri: The request URI
        :param request: The request DTO
        :param files: Single UploadFile or List of UploadFile objects
        :return: Response DTO
        """
        return self.post_files_with_request_url(combine_with(self.reply_base_url, nameof(request)), request, [file])

    def post_files_with_request(self, request: IReturn[T], files: List[UploadFile]) -> T:
        """
        Post files with a request DTO using multipart/form-data

        :param request: The request DTO
        :param files: Single UploadFile or List of UploadFile objects
        :return: Response DTO
        """
        return self.post_files_with_request_url(combine_with(self.reply_base_url, nameof(request)), request, files)

    def post_files_with_request_url(self, request_uri: str, request: Any, files: List[UploadFile]) -> T:
        """
        Post files with a request DTO using multipart/form-data

        :param request_uri: The request URI
        :param request: The request DTO
        :param files: Single UploadFile or List of UploadFile objects
        :return: Response DTO
        """
        if isinstance(files, UploadFile):
            files = [files]

        # Convert request DTO to dict
        request_data = to_jsv_data(request)

        # Prepare the files dictionary for requests
        files_dict = {}
        for file in files:
            files_dict[file.field_name or 'upload'] = (
                file.file_name,
                file.stream,
                file.content_type or 'application/octet-stream'
            )

        # Prepare headers
        headers = self.headers.copy()
        if self.bearer_token:
            headers['Authorization'] = f'Bearer {self.bearer_token}'

        url = self.to_absolute_url(request_uri)

        try:
            # Send the multipart request
            response = self._session.post(
                url,
                data=request_data,
                files=files_dict,
                headers=headers,
                verify=self._session.verify
            )

            # Handle errors
            response.raise_for_status()

            # Parse response
            response_type = _resolve_response_type(request)
            if response_type is None:
                return response.json()

            if response_type is str:
                return response.text

            if response_type is bytes:
                return response.content

            return from_json(response_type, response.text)

        finally:
            # Close all file streams
            for file in files:
                file.stream.close()


    @staticmethod
    def assert_valid_batch_request(request_dtos: list):
        if not isinstance(request_dtos, list):
            raise TypeError(f"'{nameof(request_dtos)}' is not a List")

        if len(request_dtos) == 0:
            return []

        request = request_dtos[0]
        if not isinstance(request, IReturn) and not isinstance(request, IReturnVoid):
            raise TypeError(f"'{nameof(request)}' does not implement IReturn or IReturnVoid")

        item_response_as = _resolve_response_type(request)
        if item_response_as is None:
            raise TypeError(f"Could not resolve Response Type for '{nameof(request)}'")
        return request, item_response_as

    def send_all(self, request_dtos: List[IReturn[T]]):
        request, item_response_as = self.assert_valid_batch_request(request_dtos)
        url = combine_with(self.reply_base_url, nameof(request) + "[]")

        return self.send_request(SendContext(
            session=self._session,
            headers=self.headers.copy(),
            method="POST",
            url=url,
            request=list(request_dtos),
            body=None,
            body_string=None,
            args=None,
            response_as=list.__class_getitem__(item_response_as)))  # requires 3.9

    def send_all_oneway(self, request_dtos: list):
        request, item_response_as = self.assert_valid_batch_request(request_dtos)
        url = combine_with(self.oneway_base_url, nameof(request) + "[]")

        self.send_request(SendContext(
            session=self._session,
            headers=self.headers.copy(),
            method="POST",
            url=url,
            request=list(request_dtos),
            body=None,
            body_string=None,
            args=None,
            response_as=list.__class_getitem__(item_response_as)))  # requires 3.9

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
                    url = combine_with(self.reply_base_url, nameof(info.request))
                    url = append_querystring(url, to_dict(info.request, key_case=clean_camelcase))
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

