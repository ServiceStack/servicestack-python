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
    meta: Dict[str, str] = None


class IHasSessionId:
    session_id: str = None


class IHasBearerToken:
    bearer_token: str = None


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
    error_code: str = None
    field_name: str = None
    message: str = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResponseStatus:
    error_code: str = None
    message: str = None
    stack_trace: str = None
    errors: List[ResponseError] = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryBase:
    skip: Optional[int] = None
    take: Optional[int] = None
    order_by: str = None
    order_by_desc: str = None
    include: str = None
    fields: str = None
    meta: Dict[str, str] = None


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
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthenticateResponse(IHasSessionId, IHasBearerToken):
    user_id: str = None
    session_id: str = None
    user_name: str = None
    display_name: str = None
    referrer_url: str = None
    bearer_token: str = None
    refresh_token: str = None
    profile_url: str = None
    roles: List[str] = None
    permissions: List[str] = None
    response_status: ResponseStatus = None
    meta: Dict[str, str] = None


# @Route("/auth")
# @Route("/auth/{provider}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Authenticate(IReturn[AuthenticateResponse], IPost):
    provider: str = None
    state: str = None
    oauth_token: str = None
    oauth_verifier: str = None
    user_name: str = None
    password: str = None
    remember_me: Optional[bool] = None
    error_view: str = None
    nonce: str = None
    uri: str = None
    response: str = None
    qop: str = None
    nc: str = None
    cnonce: str = None
    use_token_cookie: Optional[bool] = None
    access_token: str = None
    access_token_secret: str = None
    scope: str = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRolesResponse:
    all_roles: List[str] = None
    all_permissions: List[str] = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


# @Route("/assignroles")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRoles(IReturn[AssignRolesResponse], IPost):
    user_name: str = None
    permissions: List[str] = None
    roles: List[str] = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnAssignRolesResponse:
    all_roles: List[str] = None
    all_permissions: List[str] = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


# @Route("/unassignroles")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnAssignRoles(IReturn[UnAssignRolesResponse], IPost):
    user_name: str = None
    permissions: List[str] = None
    roles: List[str] = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConvertSessionToTokenResponse:
    meta: Dict[str, str] = None
    access_token: str = None
    refresh_token: str = None
    response_status: ResponseStatus = None


# @Route("/session-to-token")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConvertSessionToToken(IReturn[ConvertSessionToTokenResponse], IPost):
    preserve_session: bool = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccessTokenResponse:
    access_token: str = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


# @Route("/access-token")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccessToken(IReturn[GetAccessTokenResponse], IPost):
    refresh_token: str = None
    use_token_cookie: Optional[bool] = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelRequestResponse:
    tag: str = None
    elapsed: timedelta = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelRequest(IPost):
    tag: str = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateEventSubscriber(IPost):
    id: str = None
    subscribe_channels: List[str] = None
    unsubscribe_channels: List[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateEventSubscriberResponse:
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserApiKey:
    key: str = None
    key_type: str = None
    expiry_date: Optional[datetime] = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetApiKeys(IGet):
    environment: str = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetApiKeysResponse:
    results: List[UserApiKey] = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegenerateApiKeysResponse:
    results: List[UserApiKey] = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegenerateApiKeys(IPost):
    environment: str = None
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NavItem:
    label: str = None
    href: str = None
    exact: Optional[bool] = None
    id: str = None
    class_name: str = None
    icon_class: str = None
    show: str = None
    hide: str = None
    children: List[Any] = None  # NavItem
    meta: Dict[str, str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetNavItems:
    name: str = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetNavItemsResponse:
    base_url: str = None
    results: List[NavItem] = None
    nav_items_map: Dict[str, List[NavItem]] = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmptyResponse:
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IdResponse:
    id: str = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StringResponse:
    results: str = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StringsResponse:
    results: List[str] = None
    meta: Dict[str, str] = None
    response_status: ResponseStatus = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuditBase:
    created_date: datetime = None
    # @Required()
    created_by: str = None

    modified_date: datetime = None
    # @Required()
    modified_by: str = None

    deleted_date: Optional[datetime] = None
    deleted_by: str = None
