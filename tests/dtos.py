""" Options:
Date: 2021-07-04 05:47:30
Version: 5.111
Tip: To override a DTO option, remove "//" prefix before updating
BaseUrl: https://localhost:5001

#GlobalNamespace: 
#MakePropertiesOptional: False
#AddServiceStackTypes: True
#AddResponseStatus: False
#AddImplicitVersion: 
#AddDescriptionAsComments: True
#IncludeTypes: 
#ExcludeTypes: 
#DefaultImports: typing:TypeVar/Generic/Optional/Dict/List/Tuple,dataclasses:dataclass/field,dataclasses_json:dataclass_json/LetterCase/Undefined,enum:Enum,datetime:datetime/timedelta,servicestack:*
#DataClass: 
#DataClassJson: 
"""

from typing import TypeVar, Generic, Optional, Dict, List, Tuple
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, Undefined
from enum import Enum
from datetime import datetime, timedelta
from servicestack import *

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Item:
    name: str = None
    description: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Poco:
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CustomType:
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SetterType:
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeChildValidation:
    name: str = None
    # @Validate(Validator="MaximumLength(20)")
    value: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class FluentChildValidation:
    name: str = None
    value: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeSingleValidation:
    name: str = None
    # @Validate(Validator="MaximumLength(20)")
    value: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class FluentSingleValidation:
    name: str = None
    value: str = None

class IAuthTokens:
    provider: str = None
    user_id: str = None
    access_token: str = None
    access_token_secret: str = None
    refresh_token: str = None
    refresh_token_expiry: Optional[datetime] = None
    request_token: str = None
    request_token_secret: str = None
    items: Dict[str,str] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class AuthUserSession:
    referrer_url: str = None
    id: str = None
    user_auth_id: str = None
    user_auth_name: str = None
    user_name: str = None
    twitter_user_id: str = None
    twitter_screen_name: str = None
    facebook_user_id: str = None
    facebook_user_name: str = None
    first_name: str = None
    last_name: str = None
    display_name: str = None
    company: str = None
    email: str = None
    primary_email: str = None
    phone_number: str = None
    birth_date: Optional[datetime] = None
    birth_date_raw: str = None
    address: str = None
    address2: str = None
    city: str = None
    state: str = None
    country: str = None
    culture: str = None
    full_name: str = None
    gender: str = None
    language: str = None
    mail_address: str = None
    nickname: str = None
    postal_code: str = None
    time_zone: str = None
    request_token_secret: str = None
    created_at: datetime = None
    last_modified: datetime = None
    roles: List[str] = None
    permissions: List[str] = None
    is_authenticated: bool = None
    from_token: bool = None
    profile_url: str = None
    sequence: str = None
    tag: int = None
    auth_provider: str = None
    provider_o_auth_access: List[IAuthTokens] = None
    meta: Dict[str,str] = None
    audiences: List[str] = None
    scopes: List[str] = None
    dns: str = None
    rsa: str = None
    sid: str = None
    hash: str = None
    home_phone: str = None
    mobile_phone: str = None
    webpage: str = None
    email_confirmed: Optional[bool] = None
    phone_number_confirmed: Optional[bool] = None
    two_factor_enabled: Optional[bool] = None
    security_stamp: str = None
    type: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class NestedClass:
    value: str = None

class EnumType(str,Enum):
    VALUE1 = 'VALUE1'
    VALUE2 = 'VALUE2'
    VALUE3 = 'VALUE3'

# @Flags()
class EnumTypeFlags(Enum):
    VALUE1 = 0
    VALUE2 = 1
    VALUE3 = 2

class EnumWithValues(str,Enum):
    NONE = 'None'
    VALUE1 = 'Member 1'
    VALUE2 = 'Value2'

# @Flags()
class EnumFlags(Enum):
    VALUE0 = 'Value0'
    VALUE1 = 'Value 1'
    VALUE2 = 'Value2'
    VALUE3 = 'Value3'
    VALUE123 = 'Value123'

class EnumAsInt(Enum):
    VALUE1 = 1000
    VALUE2 = 2000
    VALUE3 = 3000

class EnumStyle(str,Enum):
    LOWER = 'LOWER'
    UPPER = 'UPPER'
    PASCAL_CASE = 'PASCAL_CASE'
    CAMEL_CASE = 'CAMEL_CASE'
    CAMEL_U_P_P_E_R = 'CAMEL_U_P_P_E_R'
    PASCAL_U_P_P_E_R = 'PASCAL_U_P_P_E_R'

class EnumStyleMembers(str,Enum):
    LOWER = 'lower'
    UPPER = 'UPPER'
    PASCAL_CASE = 'PascalCase'
    CAMEL_CASE = 'camelCase'
    CAMEL_UPPER = 'camelUPPER'
    PASCAL_UPPER = 'PascalUPPER'

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SubType:
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class AllTypesBase:
    id: int = None
    nullable_id: Optional[int] = None
    byte: int = None
    short: int = None
    int: int = None
    long: int = None
    u_short: int = None
    u_int: int = None
    u_long: int = None
    float: float = None
    double: float = None
    decimal: float = None
    string: str = None
    date_time: datetime = None
    time_span: timedelta = None
    date_time_offset: datetime = None
    guid: str = None
    char: str = None
    key_value_pair: KeyValuePair[str, str] = None
    nullable_date_time: Optional[datetime] = None
    nullable_time_span: Optional[timedelta] = None
    string_list: List[str] = None
    string_array: List[str] = None
    string_map: Dict[str,str] = None
    int_string_map: Dict[int,str] = None
    sub_type: SubType = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloBase:
    id: int = None

T = TypeVar('T')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloBase1(Generic[T]):
    items: List[T] = None
    counts: List[int] = None

class IPoco:
    name: str = None

class IEmptyInterface:
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class EmptyClass:
    pass

class DayOfWeek(str,Enum):
    SUNDAY = 'SUNDAY'
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'

class ScopeType(Enum):
    GLOBAL_ = 1
    SALE = 2

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PingService:
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Channel:
    name: str = None
    value: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Device:
    id: int = None
    type: str = None
    time_stamp: int = None
    channels: List[Channel] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Logger:
    id: int = None
    devices: List[Device] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Rockstar:
    id: int = None
    first_name: str = None
    last_name: str = None
    age: Optional[int] = None

From = TypeVar('From')
Into = TypeVar('Into')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryDbTenant(Generic[From, Into],QueryDb2[From, Into]):
    pass

class LivingStatus(str,Enum):
    ALIVE = 'ALIVE'
    DEAD = 'DEAD'

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarAuditTenant(AuditBase):
    tenant_id: int = None
    id: int = None
    first_name: str = None
    last_name: str = None
    age: Optional[int] = None
    date_of_birth: datetime = None
    date_died: Optional[datetime] = None
    living_status: LivingStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarBase:
    first_name: str = None
    last_name: str = None
    age: Optional[int] = None
    date_of_birth: datetime = None
    date_died: Optional[datetime] = None
    living_status: LivingStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarAuto(RockstarBase):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class OnlyDefinedInGenericType:
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class OnlyDefinedInGenericTypeFrom:
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class OnlyDefinedInGenericTypeInto:
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarAudit(RockstarBase):
    id: int = None
    created_date: datetime = None
    created_by: str = None
    created_info: str = None
    modified_date: datetime = None
    modified_by: str = None
    modified_info: str = None

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateAuditBase(Generic[Table, TResponse],ICreateDb[Table]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateAuditTenantBase(Generic[Table, TResponse],CreateAuditBase[Table, TResponse]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAuditBase(Generic[Table, TResponse],IUpdateDb[Table]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAuditTenantBase(Generic[Table, TResponse],UpdateAuditBase[Table, TResponse]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PatchAuditBase(Generic[Table, TResponse],IPatchDb[Table]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PatchAuditTenantBase(Generic[Table, TResponse],PatchAuditBase[Table, TResponse]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SoftDeleteAuditBase(Generic[Table, TResponse],IUpdateDb[Table]):
    pass

Table = TypeVar('Table')
TResponse = TypeVar('TResponse')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SoftDeleteAuditTenantBase(Generic[Table, TResponse],SoftDeleteAuditBase[Table, TResponse]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarVersion(RockstarBase):
    id: int = None
    row_version: int = None

# @Route("/messages/crud/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MessageCrud(IReturnVoid,ISaveDb["MessageCrud"]):
    id: int = None
    name: str = None
    def createResponse(): return None
    def getTypeName(): return 'MessageCrud'

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestNestedChild:
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestChild:
    name: str = None
    results: List[MetadataTestNestedChild] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MenuItemExampleItem:
    # @ApiMember()
    name1: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MenuItemExample:
    # @ApiMember()
    name1: str = None

    menu_item_example_item: MenuItemExampleItem = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MenuExample:
    # @ApiMember()
    menu_item_example1: MenuItemExample = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ListResult:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ArrayResult:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloResponseBase:
    ref_id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithReturnResponse:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloType:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class InnerType:
    id: int = None
    name: str = None

class InnerEnum(str,Enum):
    FOO = 'FOO'
    BAR = 'BAR'
    BAZ = 'BAZ'

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ReturnedDto:
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CustomUserSession(AuthUserSession):
    custom_name: str = None
    custom_info: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class UnAuthInfo:
    custom_info: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TypesGroup:
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ChatMessage:
    id: int = None
    channel: str = None
    from_user_id: str = None
    from_name: str = None
    display_name: str = None
    message: str = None
    user_auth_id: str = None
    private: bool = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetChatHistoryResponse:
    results: List[ChatMessage] = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetUserDetailsResponse:
    provider: str = None
    user_id: str = None
    user_name: str = None
    full_name: str = None
    display_name: str = None
    first_name: str = None
    last_name: str = None
    company: str = None
    email: str = None
    phone_number: str = None
    birth_date: Optional[datetime] = None
    birth_date_raw: str = None
    address: str = None
    address2: str = None
    city: str = None
    state: str = None
    country: str = None
    culture: str = None
    gender: str = None
    language: str = None
    mail_address: str = None
    nickname: str = None
    postal_code: str = None
    time_zone: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CustomHttpErrorResponse:
    custom: str = None
    response_status: ResponseStatus = None

T = TypeVar('T')
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryResponseAlt(Generic[T]):
    offset: int = None
    total: int = None
    results: List[T] = None
    meta: Dict[str,str] = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Items:
    results: List[Item] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowTypeResponse:
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowValidationResponse:
    age: int = None
    required: str = None
    email: str = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowBusinessErrorResponse:
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Account:
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Project:
    account: str = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SecuredResponse:
    result: str = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateJwtResponse:
    token: str = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateRefreshJwtResponse:
    token: str = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestResponse:
    id: int = None
    results: List[MetadataTestChild] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetExampleResponse:
    response_status: ResponseStatus = None
    # @ApiMember()
    menu_example1: MenuExample = None

# @Route("/messages/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Message(IReturn["Message"]):
    id: int = None
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetRandomIdsResponse:
    results: List[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloResponse:
    result: str = None

#
# Description on HelloAllResponse type
#
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloAnnotatedResponse:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class AllTypes(IReturn["AllTypes"]):
    id: int = None
    nullable_id: Optional[int] = None
    byte: int = None
    short: int = None
    int: int = None
    long: int = None
    u_short: int = None
    u_int: int = None
    u_long: int = None
    float: float = None
    double: float = None
    decimal: float = None
    string: str = None
    date_time: datetime = None
    time_span: timedelta = None
    date_time_offset: datetime = None
    guid: str = None
    char: str = None
    key_value_pair: KeyValuePair[str, str] = None
    nullable_date_time: Optional[datetime] = None
    nullable_time_span: Optional[timedelta] = None
    string_list: List[str] = None
    string_array: List[str] = None
    string_map: Dict[str,str] = None
    int_string_map: Dict[int,str] = None
    sub_type: SubType = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class AllCollectionTypes(IReturn["AllCollectionTypes"]):
    int_array: List[int] = None
    int_list: List[int] = None
    string_array: List[str] = None
    string_list: List[str] = None
    float_array: List[float] = None
    double_list: List[float] = None
    byte_array: bytes = None
    char_array: List[str] = None
    decimal_list: List[float] = None
    poco_array: List[Poco] = None
    poco_list: List[Poco] = None
    poco_lookup: Dict[str,List[Poco]] = None
    poco_lookup_map: Dict[str,List[Dict[str,Poco]]] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloAllTypesResponse:
    result: str = None
    all_types: AllTypes = None
    all_collection_types: AllCollectionTypes = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SubAllTypes(AllTypesBase):
    hierarchy: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloDateTime(IReturn["HelloDateTime"]):
    date_time: datetime = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDataContractResponse:
    result: str = None

#
# Description on HelloWithDescriptionResponse type
#
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDescriptionResponse:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithInheritanceResponse(HelloResponseBase):
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithAlternateReturnResponse(HelloWithReturnResponse):
    alt_result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithRouteResponse:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithTypeResponse:
    result: HelloType = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloInnerTypesResponse:
    inner_type: InnerType = None
    inner_enum: InnerEnum = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloVerbResponse:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class EnumResponse:
    operator: ScopeType = None

# @Route("/hellotypes/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloTypes(IReturn["HelloTypes"]):
    string: str = None
    bool: bool = None
    int: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloZipResponse:
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PingResponse:
    responses: Dict[str,ResponseStatus] = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RequiresRoleResponse:
    result: str = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendVerbResponse:
    id: int = None
    path_info: str = None
    request_method: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetSessionResponse:
    result: CustomUserSession = None
    un_auth_info: UnAuthInfo = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetStuffResponse:
    summary_date: Optional[datetime] = None
    summary_end_date: Optional[datetime] = None
    symbol: str = None
    email: str = None
    is_enabled: Optional[bool] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class StoreLogsResponse:
    existing_logs: List[Logger] = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TestAuthResponse:
    user_id: str = None
    session_id: str = None
    user_name: str = None
    display_name: str = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RequiresAdmin(IReturn["RequiresAdmin"]):
    id: int = None

# @Route("/custom")
# @Route("/custom/{Data}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CustomRoute(IReturn["CustomRoute"]):
    data: str = None

# @Route("/wait/{ForMs}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Wait(IReturn["Wait"]):
    for_ms: int = None

# @Route("/echo/types")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class EchoTypes(IReturn["EchoTypes"]):
    byte: int = None
    short: int = None
    int: int = None
    long: int = None
    u_short: int = None
    u_int: int = None
    u_long: int = None
    float: float = None
    double: float = None
    decimal: float = None
    string: str = None
    date_time: datetime = None
    time_span: timedelta = None
    date_time_offset: datetime = None
    guid: str = None
    char: str = None

# @Route("/echo/collections")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class EchoCollections(IReturn["EchoCollections"]):
    string_list: List[str] = None
    string_array: List[str] = None
    string_map: Dict[str,str] = None
    int_string_map: Dict[int,str] = None

# @Route("/echo/complex")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class EchoComplexTypes(IReturn["EchoComplexTypes"]):
    sub_type: SubType = None
    sub_types: List[SubType] = None
    sub_type_map: Dict[str,SubType] = None
    string_map: Dict[str,str] = None
    int_string_map: Dict[int,str] = None

# @Route("/rockstars", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class StoreRockstars(List[Rockstar],IReturn["StoreRockstars"]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdResponse:
    id: int = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdAndResultResponse:
    id: int = None
    result: RockstarAuto = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdAndCountResponse:
    id: int = None
    count: int = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdAndRowVersionResponse:
    id: int = None
    row_version: int = None
    response_status: ResponseStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryItems(QueryDb2[Item, Poco],IReturn[List[QueryResponse]]):
    pass

# @Route("/channels/{Channel}/raw")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PostRawToChannel(IReturnVoid):
    from_: str = None
    to_user_id: str = None
    channel: str = None
    message: str = None
    selector: str = None
    def createResponse(): return None
    def getTypeName(): return 'PostRawToChannel'

# @Route("/channels/{Channel}/chat")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PostChatToChannel(IReturn[ChatMessage]):
    from_: str = None
    to_user_id: str = None
    channel: str = None
    message: str = None
    selector: str = None

# @Route("/chathistory")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetChatHistory(IReturn[GetChatHistoryResponse]):
    channels: List[str] = None
    after_id: Optional[int] = None
    take: Optional[int] = None

# @Route("/reset")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ClearChatHistory(IReturnVoid):
    def createResponse(): return None
    def getTypeName(): return 'ClearChatHistory'

# @Route("/reset-serverevents")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ResetServerEvents(IReturnVoid):
    def createResponse(): return None
    def getTypeName(): return 'ResetServerEvents'

# @Route("/channels/{Channel}/object")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PostObjectToChannel(IReturnVoid):
    to_user_id: str = None
    channel: str = None
    selector: str = None
    custom_type: CustomType = None
    setter_type: SetterType = None
    def createResponse(): return None
    def getTypeName(): return 'PostObjectToChannel'

# @Route("/account")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetUserDetails(IReturn[GetUserDetailsResponse]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CustomHttpError(IReturn[CustomHttpErrorResponse]):
    status_code: int = None
    status_description: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class AltQueryItems(IReturn[List[QueryResponseAlt]]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetItems(IReturn[Items]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetNakedItems(IReturn[List[list]]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeCollectiveValidationTest(IReturn[EmptyResponse]):
    # @Validate(Validator="NotEmpty")
    # @Validate(Validator="MaximumLength(20)")
    site: str = None

    declarative_validations: List[DeclarativeChildValidation] = None
    fluent_validations: List[FluentChildValidation] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeSingleValidationTest(IReturn[EmptyResponse]):
    # @Validate(Validator="NotEmpty")
    # @Validate(Validator="MaximumLength(20)")
    site: str = None

    declarative_single_validation: DeclarativeSingleValidation = None
    fluent_single_validation: FluentSingleValidation = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class DummyTypes:
    hello_responses: List[HelloResponse] = None
    list_result: List[ListResult] = None
    array_result: List[ArrayResult] = None
    cancel_request: CancelRequest = None
    cancel_request_response: CancelRequestResponse = None
    update_event_subscriber: UpdateEventSubscriber = None
    update_event_subscriber_response: UpdateEventSubscriberResponse = None
    get_api_keys: GetApiKeys = None
    get_api_keys_response: GetApiKeysResponse = None
    regenerate_api_keys: RegenerateApiKeys = None
    regenerate_api_keys_response: RegenerateApiKeysResponse = None
    user_api_key: UserApiKey = None
    convert_session_to_token: ConvertSessionToToken = None
    convert_session_to_token_response: ConvertSessionToTokenResponse = None
    get_access_token: GetAccessToken = None
    get_access_token_response: GetAccessTokenResponse = None
    nav_item: NavItem = None
    get_nav_items: GetNavItems = None
    get_nav_items_response: GetNavItemsResponse = None
    empty_response: EmptyResponse = None
    id_response: IdResponse = None
    string_response: StringResponse = None
    strings_response: StringsResponse = None
    audit_base: AuditBase = None

# @Route("/throwhttperror/{Status}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowHttpError:
    status: Optional[int] = None
    message: str = None

# @Route("/throw404")
# @Route("/throw404/{Message}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Throw404:
    message: str = None

# @Route("/throwcustom400")
# @Route("/throwcustom400/{Message}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowCustom400:
    message: str = None

# @Route("/throw/{Type}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowType(IReturn[ThrowTypeResponse]):
    type: str = None
    message: str = None

# @Route("/throwvalidation")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowValidation(IReturn[ThrowValidationResponse]):
    age: int = None
    required: str = None
    email: str = None

# @Route("/throwbusinesserror")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ThrowBusinessError(IReturn[ThrowBusinessErrorResponse]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RootPathRoutes:
    path: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetAccount(IReturn[Account]):
    account: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetProject(IReturn[Project]):
    account: str = None
    project: str = None

# @Route("/image-stream")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsStream(IReturn[bytes]):
    format: str = None

# @Route("/image-bytes")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsBytes(IReturn[bytes]):
    format: str = None

# @Route("/image-custom")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsCustomResult(IReturn[bytes]):
    format: str = None

# @Route("/image-response")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ImageWriteToResponse(IReturn[bytes]):
    format: str = None

# @Route("/image-file")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsFile(IReturn[bytes]):
    format: str = None

# @Route("/image-redirect")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsRedirect:
    format: str = None

# @Route("/hello-image/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloImage(IReturn[bytes]):
    name: str = None
    format: str = None
    width: Optional[int] = None
    height: Optional[int] = None
    font_size: Optional[int] = None
    font_family: str = None
    foreground: str = None
    background: str = None

# @Route("/secured")
# @ValidateRequest(Validator="IsAuthenticated")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Secured(IReturn[SecuredResponse]):
    name: str = None

# @Route("/jwt")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateJwt(AuthUserSession,IReturn[CreateJwtResponse]):
    jwt_expiry: Optional[datetime] = None

# @Route("/jwt-refresh")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateRefreshJwt(IReturn[CreateRefreshJwtResponse]):
    user_auth_id: str = None
    jwt_expiry: Optional[datetime] = None

# @Route("/jwt-invalidate")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class InvalidateLastAccessToken(IReturn[EmptyResponse]):
    pass

# @Route("/logs")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ViewLogs(IReturn[str]):
    clear: bool = None

# @Route("/metadatatest")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTest(IReturn[MetadataTestResponse]):
    id: int = None

# @Route("/metadatatest-array")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestArray(IReturn[List[list]]):
    id: int = None

# @Route("/example", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetExample(IReturn[GetExampleResponse]):
    pass

# @Route("/messages/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RequestMessage(IReturn[Message]):
    id: int = None

# @Route("/randomids")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetRandomIds(IReturn[GetRandomIdsResponse]):
    take: Optional[int] = None

# @Route("/textfile-test")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TextFileTest:
    as_attachment: bool = None

# @Route("/return/text")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ReturnText:
    text: str = None

# @Route("/return/html")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ReturnHtml:
    text: str = None

# @Route("/hello")
# @Route("/hello/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Hello(IReturn[HelloResponse]):
    # @Required()
    name: str = None

    title: str = None

#
# Description on HelloAll type
#
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloAnnotated(IReturn[HelloAnnotatedResponse]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithNestedClass(IReturn[HelloResponse]):
    name: str = None
    nested_class_prop: NestedClass = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloList(IReturn[List[list]]):
    names: List[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloArray(IReturn[List[list]]):
    names: List[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithEnum:
    enum_prop: EnumType = None
    enum_type_flags: EnumTypeFlags = None
    enum_with_values: EnumWithValues = None
    nullable_enum_prop: Optional[EnumType] = None
    enum_flags: EnumFlags = None
    enum_as_int: EnumAsInt = None
    enum_style: EnumStyle = None
    enum_style_members: EnumStyleMembers = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithEnumList:
    enum_prop: List[EnumType] = None
    enum_with_values: List[EnumWithValues] = None
    nullable_enum_prop: List[EnumType] = None
    enum_flags: List[EnumFlags] = None
    enum_style: List[EnumStyle] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithEnumMap:
    enum_prop: Dict[str,EnumType] = None
    enum_with_values: Dict[str,EnumWithValues] = None
    nullable_enum_prop: Dict[str,EnumType] = None
    enum_flags: Dict[str,EnumFlags] = None
    enum_style: Dict[str,EnumStyle] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RestrictedAttributes:
    id: int = None
    name: str = None
    hello: Hello = None

#
# AllowedAttributes Description
#
# @Route("/allowed-attributes", "GET")
# @Api(Description="AllowedAttributes Description")
# @ApiResponse(Description="Your request was not understood", StatusCode=400)
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class AllowedAttributes:
    #
    # Range Description
    #
    # @ApiMember(DataType="double", Description="Range Description", IsRequired=true, ParameterType="path")
    range: float = None

# @Route("/all-types")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloAllTypes(IReturn[HelloAllTypesResponse]):
    name: str = None
    all_types: AllTypes = None
    all_collection_types: AllCollectionTypes = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloSubAllTypes(AllTypesBase,IReturn[SubAllTypes]):
    hierarchy: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloString(IReturn[str]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloVoid:
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDataContract(IReturn[HelloWithDataContractResponse]):
    name: str = None
    id: int = None

#
# Description on HelloWithDescription type
#
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDescription(IReturn[HelloWithDescriptionResponse]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithInheritance(HelloBase,IReturn[HelloWithInheritanceResponse]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithGenericInheritance(HelloBase1[Poco]):
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithGenericInheritance2(HelloBase1[Hello]):
    result: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithReturn(IReturn[HelloWithAlternateReturnResponse]):
    name: str = None

# @Route("/helloroute")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithRoute(IReturn[HelloWithRouteResponse]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithType(IReturn[HelloWithTypeResponse]):
    name: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloInterface:
    poco: IPoco = None
    empty_interface: IEmptyInterface = None
    empty_class: EmptyClass = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloInnerTypes(IReturn[HelloInnerTypesResponse]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloBuiltin:
    day_of_week: DayOfWeek = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloGet(IReturn[HelloVerbResponse],IGet):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloPost(HelloBase,IReturn[HelloVerbResponse],IPost):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloPut(IReturn[HelloVerbResponse],IPut):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloDelete(IReturn[HelloVerbResponse],IDelete):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloPatch(IReturn[HelloVerbResponse],IPatch):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloReturnVoid(IReturnVoid):
    id: int = None
    def createResponse(): return None
    def getTypeName(): return 'HelloReturnVoid'

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class EnumRequest(IReturn[EnumResponse],IPut):
    operator: ScopeType = None

# @Route("/hellozip")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloZip(IReturn[HelloZipResponse]):
    name: str = None
    test: List[str] = None

# @Route("/ping")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class Ping(IReturn[PingResponse]):
    pass

# @Route("/reset-connections")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ResetConnections:
    pass

# @Route("/requires-role")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RequiresRole(IReturn[RequiresRoleResponse]):
    pass

# @Route("/return/string")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ReturnString(IReturn[str]):
    data: str = None

# @Route("/return/bytes")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ReturnBytes(IReturn[bytes]):
    data: bytes = None

# @Route("/return/stream")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class ReturnStream(IReturn[bytes]):
    data: bytes = None

# @Route("/Request1", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetRequest1(IReturn[List[list]],IGet):
    pass

# @Route("/Request2", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetRequest2(IReturn[List[list]],IGet):
    pass

# @Route("/sendjson")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendJson(IReturn[str]):
    id: int = None
    name: str = None

# @Route("/sendtext")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendText(IReturn[str]):
    id: int = None
    name: str = None
    content_type: str = None

# @Route("/sendraw")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendRaw(IReturn[bytes]):
    id: int = None
    name: str = None
    content_type: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendDefault(IReturn[SendVerbResponse]):
    id: int = None

# @Route("/sendrestget/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendRestGet(IReturn[SendVerbResponse],IGet):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendGet(IReturn[SendVerbResponse],IGet):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendPost(IReturn[SendVerbResponse],IPost):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendPut(IReturn[SendVerbResponse],IPut):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SendReturnVoid(IReturnVoid):
    id: int = None
    def createResponse(): return None
    def getTypeName(): return 'SendReturnVoid'

# @Route("/session")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetSession(IReturn[GetSessionResponse]):
    pass

# @Route("/session/edit/{CustomName}")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class UpdateSession(IReturn[GetSessionResponse]):
    custom_name: str = None

# @Route("/Stuff")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class GetStuff(IReturn[GetStuffResponse]):
    # @ApiMember(DataType="DateTime", Name="Summary Date")
    summary_date: Optional[datetime] = None

    # @ApiMember(DataType="DateTime", Name="Summary End Date")
    summary_end_date: Optional[datetime] = None

    # @ApiMember(DataType="string", Name="Symbol")
    symbol: str = None

    # @ApiMember(DataType="string", Name="Email")
    email: str = None

    # @ApiMember(DataType="bool", Name="Is Enabled")
    is_enabled: Optional[bool] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class StoreLogs(IReturn[StoreLogsResponse]):
    loggers: List[Logger] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class HelloAuth(IReturn[HelloResponse]):
    name: str = None

# @Route("/testauth")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TestAuth(IReturn[TestAuthResponse]):
    pass

# @Route("/testdata/AllTypes")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TestDataAllTypes(IReturn[AllTypes]):
    pass

# @Route("/testdata/AllCollectionTypes")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TestDataAllCollectionTypes(IReturn[AllCollectionTypes]):
    pass

# @Route("/void-response")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TestVoidResponse:
    pass

# @Route("/null-response")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class TestNullResponse:
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryRockstarAudit(QueryDbTenant[RockstarAuditTenant, RockstarAuto],IReturn[List[QueryResponse]]):
    id: Optional[int] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryRockstarAuditSubOr(QueryDb2[RockstarAuditTenant, RockstarAuto],IReturn[List[QueryResponse]]):
    first_name_starts_with: str = None
    age_older_than: Optional[int] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryPocoBase(QueryDb[OnlyDefinedInGenericType],IReturn[List[QueryResponse]]):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryPocoIntoBase(QueryDb2[OnlyDefinedInGenericTypeFrom, OnlyDefinedInGenericTypeInto],IReturn[List[QueryResponse]]):
    id: int = None

# @Route("/message/query/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class MessageQuery(QueryDb["MessageQuery"],IReturn[List[QueryResponse]]):
    id: int = None

# @Route("/rockstars", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class QueryRockstars(QueryDb[Rockstar],IReturn[List[QueryResponse]]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarAudit(RockstarBase,IReturn[RockstarWithIdResponse],ICreateDb[RockstarAudit]):
    pass

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarAuditTenant(CreateAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse],IReturn[RockstarWithIdAndResultResponse],IHasSessionId):
    session_id: str = None
    first_name: str = None
    last_name: str = None
    age: Optional[int] = None
    date_of_birth: datetime = None
    date_died: Optional[datetime] = None
    living_status: LivingStatus = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class UpdateRockstarAuditTenant(UpdateAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse],IReturn[RockstarWithIdAndResultResponse],IHasSessionId):
    session_id: str = None
    id: int = None
    first_name: str = None
    living_status: Optional[LivingStatus] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class PatchRockstarAuditTenant(PatchAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse],IReturn[RockstarWithIdAndResultResponse],IHasSessionId):
    session_id: str = None
    id: int = None
    first_name: str = None
    living_status: Optional[LivingStatus] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class SoftDeleteAuditTenant(SoftDeleteAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse],IReturn[RockstarWithIdAndResultResponse]):
    id: int = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarAuditMqToken(RockstarBase,IReturn[RockstarWithIdResponse],ICreateDb[RockstarAudit],IHasBearerToken):
    bearer_token: str = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class RealDeleteAuditTenant(IReturn[RockstarWithIdAndCountResponse],IDeleteDb[RockstarAuditTenant],IHasSessionId):
    session_id: str = None
    id: int = None
    age: Optional[int] = None

@dataclass_json(letter_case=LetterCase.CAMEL,undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarVersion(RockstarBase,IReturn[RockstarWithIdAndRowVersionResponse],ICreateDb[RockstarVersion]):
    pass
