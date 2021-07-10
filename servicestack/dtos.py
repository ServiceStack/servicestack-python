from typing import TypeVar, Generic, Optional, Dict, List, Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase, Undefined
from datetime import datetime, timedelta

T = TypeVar('T')
Table = TypeVar('Table')
From = TypeVar('From')
Into = TypeVar('Into')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class IReturn(Generic[T]):
    pass


class IReturnVoid:
    pass


class IGet:
    pass


class IPost:
    pass


class IPut:
    pass


class IDelete:
    pass


class IPatch:
    pass


class IOptions:
    pass


class IMeta:
    meta: Optional[Dict[str, str]] = None


class IHasSessionId:
    session_id: Optional[str] = None


class IHasBearerToken:
    bearer_token: Optional[str] = None


class IHasVersion:
    version: Optional[int] = None


class ICrud:
    pass


class ICreateDb(Generic[Table]):
    pass


class IUpdateDb(Generic[Table]):
    pass


class IPatchDb(Generic[Table]):
    pass


class IDeleteDb(Generic[Table]):
    pass


class ISaveDb(Generic[Table]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KeyValuePair(Generic[TKey, TValue]):
    key: TKey = None
    value: TValue = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResponseError:
    error_code: Optional[str] = None
    field_name: Optional[str] = None
    message: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResponseStatus:
    error_code: Optional[str] = None
    message: Optional[str] = None
    stack_trace: Optional[str] = None
    errors: List[ResponseError] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryBase:
    skip: Optional[int] = None
    take: Optional[int] = None
    order_by: Optional[str] = None
    order_by_desc: Optional[str] = None
    include: Optional[str] = None
    fields: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryDb(Generic[T], QueryBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryDb1(Generic[T], QueryBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryDb2(Generic[From, Into], QueryBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryData(Generic[T], QueryBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryData1(Generic[From, Into], QueryBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryData2(Generic[From, Into], QueryBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryResponse(Generic[T]):
    offset: int = None
    total: int = None
    results: List[T] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthenticateResponse(IHasSessionId, IHasBearerToken):
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    user_name: Optional[str] = None
    display_name: Optional[str] = None
    referrer_url: Optional[str] = None
    bearer_token: Optional[str] = None
    refresh_token: Optional[str] = None
    profile_url: Optional[str] = None
    roles: Optional[List[str]] = None
    permissions: Optional[List[str]] = None
    response_status: Optional[ResponseStatus] = None
    meta: Optional[Dict[str, str]] = None


# @Route("/auth")
# @Route("/auth/{provider}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Authenticate(IReturn[AuthenticateResponse], IPost):
    provider: Optional[str] = None
    state: Optional[str] = None
    oauth_token: Optional[str] = None
    oauth_verifier: Optional[str] = None
    user_name: Optional[str] = None
    password: Optional[str] = None
    remember_me: Optional[bool] = None
    error_view: Optional[str] = None
    nonce: Optional[str] = None
    uri: Optional[str] = None
    response: Optional[str] = None
    qop: Optional[str] = None
    nc: Optional[str] = None
    cnonce: Optional[str] = None
    use_token_cookie: Optional[bool] = None
    access_token: Optional[str] = None
    access_token_secret: Optional[str] = None
    scope: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRolesResponse:
    all_roles: Optional[List[str]] = None
    all_permissions: Optional[List[str]] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


# @Route("/assignroles")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRoles(IReturn[AssignRolesResponse], IPost):
    user_name: Optional[str] = None
    permissions: Optional[List[str]] = None
    roles: Optional[List[str]] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnAssignRolesResponse:
    all_roles: Optional[List[str]] = None
    all_permissions: Optional[List[str]] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


# @Route("/unassignroles")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnAssignRoles(IReturn[UnAssignRolesResponse], IPost):
    user_name: Optional[str] = None
    permissions: Optional[List[str]] = None
    roles: Optional[List[str]] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConvertSessionToTokenResponse:
    meta: Optional[Dict[str, str]] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


# @Route("/session-to-token")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConvertSessionToToken(IReturn[ConvertSessionToTokenResponse], IPost):
    preserve_session: bool = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccessTokenResponse:
    access_token: Optional[str] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


# @Route("/access-token")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccessToken(IReturn[GetAccessTokenResponse], IPost):
    refresh_token: Optional[str] = None
    use_token_cookie: Optional[bool] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelRequestResponse:
    tag: Optional[str] = None
    elapsed: timedelta = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelRequest(IPost):
    tag: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateEventSubscriber(IPost):
    id: Optional[str] = None
    subscribe_channels: Optional[List[str]] = None
    unsubscribe_channels: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateEventSubscriberResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserApiKey:
    key: Optional[str] = None
    key_type: Optional[str] = None
    expiry_date: Optional[datetime] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetApiKeys(IGet):
    environment: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetApiKeysResponse:
    results: List[UserApiKey] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegenerateApiKeysResponse:
    results: List[UserApiKey] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegenerateApiKeys(IPost):
    environment: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NavItem:
    label: Optional[str] = None
    href: Optional[str] = None
    exact: Optional[bool] = None
    id: Optional[str] = None
    class_name: Optional[str] = None
    icon_class: Optional[str] = None
    show: Optional[str] = None
    hide: Optional[str] = None
    children: List[Any] = None  # NavItem
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetNavItems:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetNavItemsResponse:
    base_url: Optional[str] = None
    results: List[NavItem] = None
    nav_items_map: Dict[str, List[NavItem]] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmptyResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IdResponse:
    id: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StringResponse:
    results: Optional[str] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StringsResponse:
    results: Optional[List[str]] = None
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuditBase:
    created_date: datetime = None
    # @Required()
    created_by: Optional[str] = None

    modified_date: datetime = None
    # @Required()
    modified_by: Optional[str] = None

    deleted_date: Optional[datetime] = None
    deleted_by: Optional[str] = None
