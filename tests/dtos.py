""" Options:
Date: 2025-08-02 04:39:48
Version: 8.81
Tip: To override a DTO option, remove "#" prefix before updating
BaseUrl: https://test.servicestack.net

#GlobalNamespace: 
#AddServiceStackTypes: True
#AddResponseStatus: False
#AddImplicitVersion: 
#AddDescriptionAsComments: True
#IncludeTypes: 
#ExcludeTypes: 
#DefaultImports: datetime,decimal,marshmallow.fields:*,servicestack:*,typing:*,dataclasses:dataclass/field,dataclasses_json:dataclass_json/LetterCase/Undefined/config,enum:Enum/IntEnum
#DataClass: 
#DataClassJson: 
"""

import datetime
import decimal
from marshmallow.fields import *
from servicestack import *
from typing import *
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, Undefined, config
from enum import Enum, IntEnum


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Item:
    name: Optional[str] = None
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Poco:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CustomType:
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetterType:
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeChildValidation:
    name: Optional[str] = None
    # @Validate(Validator="MaximumLength(20)")
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FluentChildValidation:
    name: Optional[str] = None
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeSingleValidation:
    name: Optional[str] = None
    # @Validate(Validator="MaximumLength(20)")
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FluentSingleValidation:
    name: Optional[str] = None
    value: Optional[str] = None


class IGeneration:
    ref_id: Optional[str] = None
    tag: Optional[str] = None


class IAuthTokens:
    provider: Optional[str] = None
    user_id: Optional[str] = None
    access_token: Optional[str] = None
    access_token_secret: Optional[str] = None
    refresh_token: Optional[str] = None
    refresh_token_expiry: Optional[datetime.datetime] = None
    request_token: Optional[str] = None
    request_token_secret: Optional[str] = None
    items: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthUserSession:
    referrer_url: Optional[str] = None
    id: Optional[str] = None
    user_auth_id: Optional[str] = None
    user_auth_name: Optional[str] = None
    user_name: Optional[str] = None
    twitter_user_id: Optional[str] = None
    twitter_screen_name: Optional[str] = None
    facebook_user_id: Optional[str] = None
    facebook_user_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    primary_email: Optional[str] = None
    phone_number: Optional[str] = None
    birth_date: Optional[datetime.datetime] = None
    birth_date_raw: Optional[str] = None
    address: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    culture: Optional[str] = None
    full_name: Optional[str] = None
    gender: Optional[str] = None
    language: Optional[str] = None
    mail_address: Optional[str] = None
    nickname: Optional[str] = None
    postal_code: Optional[str] = None
    time_zone: Optional[str] = None
    request_token_secret: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime(1, 1, 1)
    last_modified: datetime.datetime = datetime.datetime(1, 1, 1)
    roles: Optional[List[str]] = None
    permissions: Optional[List[str]] = None
    is_authenticated: bool = False
    from_token: bool = False
    profile_url: Optional[str] = None
    sequence: Optional[str] = None
    tag: int = 0
    auth_provider: Optional[str] = None
    provider_o_auth_access: Optional[List[IAuthTokens]] = None
    meta: Optional[Dict[str, str]] = None
    audiences: Optional[List[str]] = None
    scopes: Optional[List[str]] = None
    dns: Optional[str] = None
    rsa: Optional[str] = None
    sid: Optional[str] = None
    hash: Optional[str] = None
    home_phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    webpage: Optional[str] = None
    email_confirmed: Optional[bool] = None
    phone_number_confirmed: Optional[bool] = None
    two_factor_enabled: Optional[bool] = None
    security_stamp: Optional[str] = None
    type: Optional[str] = None
    recovery_token: Optional[str] = None
    ref_id: Optional[int] = None
    ref_id_str: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NestedClass:
    value: Optional[str] = None


class EnumType(str, Enum):
    VALUE1 = 'Value1'
    VALUE2 = 'Value2'
    VALUE3 = 'Value3'


# @Flags()
class EnumTypeFlags(IntEnum):
    VALUE1 = 0
    VALUE2 = 1
    VALUE3 = 2


class EnumWithValues(str, Enum):
    NONE = 'None'
    VALUE1 = 'Member 1'
    VALUE2 = 'Value2'


# @Flags()
class EnumFlags(IntEnum):
    VALUE0 = 0
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 4
    VALUE123 = 7


class EnumAsInt(IntEnum):
    VALUE1 = 1000
    VALUE2 = 2000
    VALUE3 = 3000


class EnumStyle(str, Enum):
    LOWER = 'lower'
    UPPER = 'UPPER'
    PASCAL_CASE = 'PascalCase'
    CAMEL_CASE = 'camelCase'
    CAMEL_U_P_P_E_R = 'camelUPPER'
    PASCAL_U_P_P_E_R = 'PascalUPPER'


class EnumStyleMembers(str, Enum):
    LOWER = 'lower'
    UPPER = 'UPPER'
    PASCAL_CASE = 'PascalCase'
    CAMEL_CASE = 'camelCase'
    CAMEL_UPPER = 'camelUPPER'
    PASCAL_UPPER = 'PascalUPPER'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubType:
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AllTypesBase:
    id: int = 0
    nullable_id: Optional[int] = None
    byte: int = 0
    short: int = 0
    int_: int = field(metadata=config(field_name='int'), default=0)
    long: int = 0
    u_short: int = 0
    u_int: int = 0
    u_long: int = 0
    float_: float = field(metadata=config(field_name='float'), default=0.0)
    double: float = 0.0
    decimal: Decimal = decimal.Decimal(0)
    string: Optional[str] = None
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)
    time_span: datetime.timedelta = datetime.timedelta()
    date_time_offset: datetime.datetime = datetime.datetime(1, 1, 1)
    guid: Optional[str] = None
    char: Optional[str] = None
    key_value_pair: Optional[KeyValuePair[str, str]] = None
    nullable_date_time: Optional[datetime.datetime] = None
    nullable_time_span: Optional[datetime.timedelta] = None
    string_list: List[str] = field(default_factory=list)
    string_array: List[str] = field(default_factory=list)
    string_map: Dict[str, str] = field(default_factory=dict)
    int_string_map: Dict[int, str] = field(default_factory=dict)
    sub_type: Optional[SubType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloBase:
    id: int = 0


T = TypeVar('T')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloBase1(Generic[T]):
    items: List[T] = field(default_factory=list)
    counts: List[int] = field(default_factory=list)


class IPoco:
    name: Optional[str] = None


class IEmptyInterface:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmptyClass:
    pass


class DayOfWeek(str, Enum):
    SUNDAY = 'Sunday'
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'


class ScopeType(IntEnum):
    GLOBAL_ = 1
    SALE = 2


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Channel:
    name: Optional[str] = None
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Device:
    id: int = 0
    type: Optional[str] = None
    time_stamp: int = 0
    channels: List[Channel] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Logger:
    id: int = 0
    devices: List[Device] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Rockstar:
    id: int = 0
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None


From = TypeVar('From')
Into = TypeVar('Into')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryDbTenant(Generic[From, Into], QueryDb2[From, Into]):
    pass


class LivingStatus(str, Enum):
    ALIVE = 'Alive'
    DEAD = 'Dead'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarAuditTenant(AuditBase):
    tenant_id: int = 0
    id: int = 0
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: datetime.datetime = datetime.datetime(1, 1, 1)
    date_died: Optional[datetime.datetime] = None
    living_status: Optional[LivingStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarBase:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: datetime.datetime = datetime.datetime(1, 1, 1)
    date_died: Optional[datetime.datetime] = None
    living_status: Optional[LivingStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarAuto(RockstarBase):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OnlyDefinedInGenericType:
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OnlyDefinedInGenericTypeFrom:
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OnlyDefinedInGenericTypeInto:
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarAudit(RockstarBase):
    id: int = 0
    created_date: datetime.datetime = datetime.datetime(1, 1, 1)
    created_by: Optional[str] = None
    created_info: Optional[str] = None
    modified_date: datetime.datetime = datetime.datetime(1, 1, 1)
    modified_by: Optional[str] = None
    modified_info: Optional[str] = None


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAuditBase(Generic[Table, TResponse], IReturn[TResponse], ICreateDb[Table]):
    @staticmethod
    def response_type(): return TResponse


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAuditTenantBase(Generic[Table, TResponse], CreateAuditBase[Table, TResponse]):
    pass


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAuditBase(Generic[Table, TResponse], IReturn[TResponse], IUpdateDb[Table]):
    @staticmethod
    def response_type(): return TResponse


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAuditTenantBase(Generic[Table, TResponse], UpdateAuditBase[Table, TResponse]):
    pass


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PatchAuditBase(Generic[Table, TResponse], IReturn[TResponse], IPatchDb[Table]):
    @staticmethod
    def response_type(): return TResponse


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PatchAuditTenantBase(Generic[Table, TResponse], PatchAuditBase[Table, TResponse]):
    pass


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SoftDeleteAuditBase(Generic[Table, TResponse], IReturn[TResponse], IUpdateDb[Table]):
    @staticmethod
    def response_type(): return TResponse


Table = TypeVar('Table')
TResponse = TypeVar('TResponse')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SoftDeleteAuditTenantBase(Generic[Table, TResponse], SoftDeleteAuditBase[Table, TResponse]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarVersion(RockstarBase):
    id: int = 0
    row_version: int = 0


# @Route("/messages/crud/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MessageCrud(IReturnVoid, ISaveDb["MessageCrud"]):
    id: int = 0
    name: Optional[str] = None


T = TypeVar('T')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryResponseAlt(Generic[T]):
    offset: int = 0
    total: int = 0
    results: List[T] = field(default_factory=list)
    meta: Dict[str, str] = field(default_factory=dict)
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TextOutput:
    """
    Output object for generated text
    """

    # @ApiMember(Description="The generated text")
    text: Optional[str] = None
    """
    The generated text
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UploadInfo:
    name: Optional[str] = None
    file_name: Optional[str] = None
    content_length: int = 0
    content_type: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestNestedChild:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestChild:
    name: Optional[str] = None
    results: List[MetadataTestNestedChild] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MenuItemExampleItem:
    # @ApiMember()
    name1: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MenuItemExample:
    # @ApiMember()
    name1: Optional[str] = None

    menu_item_example_item: Optional[MenuItemExampleItem] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MenuExample:
    # @ApiMember()
    menu_item_example1: Optional[MenuItemExample] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListResult:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArrayResult:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloResponseBase:
    ref_id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithReturnResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloType:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InnerType:
    id: int = 0
    name: Optional[str] = None


class InnerEnum(str, Enum):
    FOO = 'Foo'
    BAR = 'Bar'
    BAZ = 'Baz'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnedDto:
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CustomUserSession(AuthUserSession):
    custom_name: Optional[str] = None
    custom_info: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnAuthInfo:
    custom_info: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnalyticsLogInfo:
    id: int = 0
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)
    browser: Optional[str] = None
    device: Optional[str] = None
    bot: Optional[str] = None
    op: Optional[str] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    api_key: Optional[str] = None
    ip: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestSummary:
    name: Optional[str] = None
    total_requests: int = 0
    total_request_length: int = 0
    min_request_length: int = 0
    max_request_length: int = 0
    total_duration: float = 0.0
    min_duration: float = 0.0
    max_duration: float = 0.0
    status: Optional[Dict[int, int]] = None
    durations: Optional[Dict[str, int]] = None
    apis: Optional[Dict[str, int]] = None
    users: Optional[Dict[str, int]] = None
    ips: Optional[Dict[str, int]] = None
    api_keys: Optional[Dict[str, int]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnalyticsReports:
    id: int = 0
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    version: Decimal = decimal.Decimal(0)
    apis: Optional[Dict[str, RequestSummary]] = None
    users: Optional[Dict[str, RequestSummary]] = None
    tags: Optional[Dict[str, RequestSummary]] = None
    status: Optional[Dict[str, RequestSummary]] = None
    days: Optional[Dict[str, RequestSummary]] = None
    api_keys: Optional[Dict[str, RequestSummary]] = None
    ips: Optional[Dict[str, RequestSummary]] = None
    browsers: Optional[Dict[str, RequestSummary]] = None
    devices: Optional[Dict[str, RequestSummary]] = None
    bots: Optional[Dict[str, RequestSummary]] = None
    durations: Optional[Dict[str, int]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TypesGroup:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatMessage:
    id: int = 0
    channel: Optional[str] = None
    from_user_id: Optional[str] = None
    from_name: Optional[str] = None
    display_name: Optional[str] = None
    message: Optional[str] = None
    user_auth_id: Optional[str] = None
    private: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatHistoryResponse:
    results: Optional[List[ChatMessage]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserDetailsResponse:
    provider: Optional[str] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    full_name: Optional[str] = None
    display_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    birth_date: Optional[datetime.datetime] = None
    birth_date_raw: Optional[str] = None
    address: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    culture: Optional[str] = None
    gender: Optional[str] = None
    language: Optional[str] = None
    mail_address: Optional[str] = None
    nickname: Optional[str] = None
    postal_code: Optional[str] = None
    time_zone: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CustomHttpErrorResponse:
    custom: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Items:
    results: List[Item] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnCustom400Response:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowTypeResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowValidationResponse:
    age: int = 0
    required: Optional[str] = None
    email: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowBusinessErrorResponse:
    response_status: Optional[ResponseStatus] = None


# @Api(Description="Response object for text generation requests")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TextGenerationResponse:
    """
    Response object for text generation requests
    """

    # @ApiMember(Description="List of generated text outputs")
    results: Optional[List[TextOutput]] = None
    """
    List of generated text outputs
    """


    # @ApiMember(Description="Detailed response status information")
    response_status: Optional[ResponseStatus] = None
    """
    Detailed response status information
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestFileUploadsResponse:
    id: Optional[int] = None
    ref_id: Optional[str] = None
    files: List[UploadInfo] = field(default_factory=list)
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestUploadWithDto(IReturn["TestUploadWithDto"], IPost):
    int_: int = field(metadata=config(field_name='int'), default=0)
    nullable_id: Optional[int] = None
    long: int = 0
    double: float = 0.0
    string: Optional[str] = None
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)
    int_array: Optional[List[int]] = None
    int_list: Optional[List[int]] = None
    string_array: Optional[List[str]] = None
    string_list: Optional[List[str]] = None
    poco_array: Optional[List[Poco]] = None
    poco_list: Optional[List[Poco]] = None
    nullable_byte_array: Optional[List[Optional[int]]] = None
    nullable_byte_list: Optional[List[int]] = None
    nullable_date_time_array: Optional[List[Optional[datetime.datetime]]] = None
    nullable_date_time_list: Optional[List[datetime.datetime]] = None
    poco_lookup: Optional[Dict[str, List[Poco]]] = None
    poco_lookup_map: Optional[Dict[str, List[Dict[str, Poco]]]] = None
    map_list: Optional[Dict[str, List[str]]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Account:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Project:
    account: Optional[str] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SecuredResponse:
    result: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateJwtResponse:
    token: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRefreshJwtResponse:
    token: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestResponse:
    id: int = 0
    results: List[MetadataTestChild] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetExampleResponse:
    response_status: Optional[ResponseStatus] = None
    # @ApiMember()
    menu_example1: Optional[MenuExample] = None


# @Route("/messages/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Message(IReturn["Message"]):
    id: int = 0
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRandomIdsResponse:
    results: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AllTypes(IReturn["AllTypes"]):
    id: int = 0
    nullable_id: Optional[int] = None
    byte: int = 0
    short: int = 0
    int_: int = field(metadata=config(field_name='int'), default=0)
    long: int = 0
    u_short: int = 0
    u_int: int = 0
    u_long: int = 0
    float_: float = field(metadata=config(field_name='float'), default=0.0)
    double: float = 0.0
    decimal: Decimal = decimal.Decimal(0)
    string: Optional[str] = None
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)
    time_span: datetime.timedelta = datetime.timedelta()
    date_time_offset: datetime.datetime = datetime.datetime(1, 1, 1)
    guid: Optional[str] = None
    char: Optional[str] = None
    key_value_pair: Optional[KeyValuePair[str, str]] = None
    nullable_date_time: Optional[datetime.datetime] = None
    nullable_time_span: Optional[datetime.timedelta] = None
    string_list: List[str] = field(default_factory=list)
    string_array: List[str] = field(default_factory=list)
    string_map: Dict[str, str] = field(default_factory=dict)
    int_string_map: Dict[int, str] = field(default_factory=dict)
    sub_type: Optional[SubType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AllCollectionTypes(IReturn["AllCollectionTypes"]):
    int_array: List[int] = field(default_factory=list)
    int_list: List[int] = field(default_factory=list)
    string_array: List[str] = field(default_factory=list)
    string_list: List[str] = field(default_factory=list)
    float_array: List[float] = field(default_factory=list)
    double_list: List[float] = field(default_factory=list)
    byte_array: bytes = field(default_factory=list)
    char_array: List[str] = field(default_factory=list)
    decimal_list: List[Decimal] = field(default_factory=list)
    poco_array: List[Poco] = field(default_factory=list)
    poco_list: List[Poco] = field(default_factory=list)
    poco_lookup: Dict[str, List[Poco]] = field(default_factory=dict)
    poco_lookup_map: Dict[str, List[Dict[str, Poco]]] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloAllTypesResponse:
    result: Optional[str] = None
    all_types: Optional[AllTypes] = None
    all_collection_types: Optional[AllCollectionTypes] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubAllTypes(AllTypesBase):
    hierarchy: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloDateTime(IReturn["HelloDateTime"]):
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDataContractResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDescriptionResponse:
    """
    Description on HelloWithDescriptionResponse type
    """

    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithInheritanceResponse(HelloResponseBase):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithAlternateReturnResponse(HelloWithReturnResponse):
    alt_result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithRouteResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithTypeResponse:
    result: Optional[HelloType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloInnerTypesResponse:
    inner_type: Optional[InnerType] = None
    inner_enum: Optional[InnerEnum] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloVerbResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnumResponse:
    operator: Optional[ScopeType] = None


# @Route("/hellotypes/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloTypes(IReturn["HelloTypes"]):
    string: Optional[str] = None
    bool_: bool = field(metadata=config(field_name='bool'), default=False)
    int_: int = field(metadata=config(field_name='int'), default=0)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloZipResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PingResponse:
    responses: Optional[Dict[str, ResponseStatus]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequiresRoleResponse:
    result: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendVerbResponse:
    id: int = 0
    path_info: Optional[str] = None
    request_method: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSessionResponse:
    result: Optional[CustomUserSession] = None
    un_auth_info: Optional[UnAuthInfo] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetStuffResponse:
    summary_date: Optional[datetime.datetime] = None
    summary_end_date: Optional[datetime.datetime] = None
    symbol: Optional[str] = None
    email: Optional[str] = None
    is_enabled: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StoreLogsResponse:
    existing_logs: List[Logger] = field(default_factory=list)
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestAuthResponse:
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    user_name: Optional[str] = None
    display_name: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequiresAdmin(IReturn["RequiresAdmin"]):
    id: int = 0


# @Route("/custom")
# @Route("/custom/{Data}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CustomRoute(IReturn["CustomRoute"]):
    data: Optional[str] = None


# @Route("/wait/{ForMs}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Wait(IReturn["Wait"]):
    for_ms: int = 0


# @Route("/echo/types")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoTypes(IReturn["EchoTypes"]):
    byte: int = 0
    short: int = 0
    int_: int = field(metadata=config(field_name='int'), default=0)
    long: int = 0
    u_short: int = 0
    u_int: int = 0
    u_long: int = 0
    float_: float = field(metadata=config(field_name='float'), default=0.0)
    double: float = 0.0
    decimal: Decimal = decimal.Decimal(0)
    string: Optional[str] = None
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)
    time_span: datetime.timedelta = datetime.timedelta()
    date_time_offset: datetime.datetime = datetime.datetime(1, 1, 1)
    guid: Optional[str] = None
    char: Optional[str] = None


# @Route("/echo/collections")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoCollections(IReturn["EchoCollections"]):
    string_list: Optional[List[str]] = None
    string_array: Optional[List[str]] = None
    string_map: Optional[Dict[str, str]] = None
    int_string_map: Optional[Dict[int, str]] = None


# @Route("/echo/complex")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoComplexTypes(IReturn["EchoComplexTypes"]):
    sub_type: Optional[SubType] = None
    sub_types: Optional[List[SubType]] = None
    sub_type_map: Optional[Dict[str, SubType]] = None
    string_map: Optional[Dict[str, str]] = None
    int_string_map: Optional[Dict[int, str]] = None


# @Route("/rockstars", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StoreRockstars(List[Rockstar], IReturn["StoreRockstars"]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdResponse:
    id: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdAndResultResponse:
    id: int = 0
    result: Optional[RockstarAuto] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdAndCountResponse:
    id: int = 0
    count: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RockstarWithIdAndRowVersionResponse:
    id: int = 0
    row_version: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAnalyticsInfoResponse:
    months: Optional[List[str]] = None
    result: Optional[AnalyticsLogInfo] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAnalyticsReportsResponse:
    result: Optional[AnalyticsReports] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryItems(QueryDb2[Item, Poco], IReturn[QueryResponse[Poco]]):
    pass


# @Route("/channels/{Channel}/raw")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostRawToChannel(IReturnVoid):
    from_: Optional[str] = field(metadata=config(field_name='from'), default=None)
    to_user_id: Optional[str] = None
    channel: Optional[str] = None
    message: Optional[str] = None
    selector: Optional[str] = None


# @Route("/channels/{Channel}/chat")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostChatToChannel(IReturn[ChatMessage]):
    from_: Optional[str] = field(metadata=config(field_name='from'), default=None)
    to_user_id: Optional[str] = None
    channel: Optional[str] = None
    message: Optional[str] = None
    selector: Optional[str] = None


# @Route("/chathistory")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatHistory(IReturn[GetChatHistoryResponse]):
    channels: Optional[List[str]] = None
    after_id: Optional[int] = None
    take: Optional[int] = None


# @Route("/reset")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ClearChatHistory(IReturnVoid):
    pass


# @Route("/reset-serverevents")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResetServerEvents(IReturnVoid):
    pass


# @Route("/channels/{Channel}/object")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostObjectToChannel(IReturnVoid):
    to_user_id: Optional[str] = None
    channel: Optional[str] = None
    selector: Optional[str] = None
    custom_type: Optional[CustomType] = None
    setter_type: Optional[SetterType] = None


# @Route("/account")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserDetails(IReturn[GetUserDetailsResponse]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CustomHttpError(IReturn[CustomHttpErrorResponse]):
    status_code: int = 0
    status_description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AltQueryItems(IReturn[QueryResponseAlt[Item]]):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetItems(IReturn[Items]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetNakedItems(IReturn[List[Item]]):
    pass


# @ValidateRequest(Validator="IsAuthenticated")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeValidationAuth:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeCollectiveValidationTest(IReturn[EmptyResponse]):
    # @Validate(Validator="NotEmpty")
    # @Validate(Validator="MaximumLength(20)")
    site: Optional[str] = None

    declarative_validations: List[DeclarativeChildValidation] = field(default_factory=list)
    fluent_validations: List[FluentChildValidation] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeclarativeSingleValidationTest(IReturn[EmptyResponse]):
    # @Validate(Validator="NotEmpty")
    # @Validate(Validator="MaximumLength(20)")
    site: Optional[str] = None

    declarative_single_validation: Optional[DeclarativeSingleValidation] = None
    fluent_single_validation: Optional[FluentSingleValidation] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DummyTypes:
    hello_responses: Optional[List[HelloResponse]] = None
    list_result: Optional[List[ListResult]] = None
    array_result: Optional[List[ArrayResult]] = None
    cancel_request: Optional[CancelRequest] = None
    cancel_request_response: Optional[CancelRequestResponse] = None
    update_event_subscriber: Optional[UpdateEventSubscriber] = None
    update_event_subscriber_response: Optional[UpdateEventSubscriberResponse] = None
    get_api_keys: Optional[GetApiKeys] = None
    get_api_keys_response: Optional[GetApiKeysResponse] = None
    regenerate_api_keys: Optional[RegenerateApiKeys] = None
    regenerate_api_keys_response: Optional[RegenerateApiKeysResponse] = None
    user_api_key: Optional[UserApiKey] = None
    convert_session_to_token: Optional[ConvertSessionToToken] = None
    convert_session_to_token_response: Optional[ConvertSessionToTokenResponse] = None
    get_access_token: Optional[GetAccessToken] = None
    get_access_token_response: Optional[GetAccessTokenResponse] = None
    nav_item: Optional[NavItem] = None
    get_nav_items: Optional[GetNavItems] = None
    get_nav_items_response: Optional[GetNavItemsResponse] = None
    empty_response: Optional[EmptyResponse] = None
    id_response: Optional[IdResponse] = None
    string_response: Optional[StringResponse] = None
    strings_response: Optional[StringsResponse] = None
    audit_base: Optional[AuditBase] = None


# @Route("/throwhttperror/{Status}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowHttpError:
    status: Optional[int] = None
    message: Optional[str] = None


# @Route("/throw404")
# @Route("/throw404/{Message}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Throw404:
    message: Optional[str] = None


# @Route("/throwcustom400")
# @Route("/throwcustom400/{Message}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowCustom400:
    message: Optional[str] = None


# @Route("/returncustom400")
# @Route("/returncustom400/{Message}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnCustom400(IReturn[ReturnCustom400Response]):
    message: Optional[str] = None


# @Route("/throw/{Type}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowType(IReturn[ThrowTypeResponse]):
    type: Optional[str] = None
    message: Optional[str] = None


# @Route("/throwvalidation")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowValidation(IReturn[ThrowValidationResponse]):
    age: int = 0
    required: Optional[str] = None
    email: Optional[str] = None


# @Route("/throwbusinesserror")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ThrowBusinessError(IReturn[ThrowBusinessErrorResponse]):
    pass


# @Api(Description="Convert speech to text")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SpeechToText(IReturn[TextGenerationResponse], IGeneration):
    """
    Convert speech to text
    """

    # @ApiMember(Description="The audio stream containing the speech to be transcribed")
    # @Required()
    audio: Optional[str] = None
    """
    The audio stream containing the speech to be transcribed
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestFileUploads(IReturn[TestFileUploadsResponse]):
    id: Optional[int] = None
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RootPathRoutes:
    path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccount(IReturn[Account]):
    account: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProject(IReturn[Project]):
    account: Optional[str] = None
    project: Optional[str] = None


# @Route("/image-stream")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsStream(IReturn[bytes]):
    format: Optional[str] = None


# @Route("/image-bytes")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsBytes(IReturn[bytes]):
    format: Optional[str] = None


# @Route("/image-custom")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsCustomResult(IReturn[bytes]):
    format: Optional[str] = None


# @Route("/image-response")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageWriteToResponse(IReturn[bytes]):
    format: Optional[str] = None


# @Route("/image-file")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsFile(IReturn[bytes]):
    format: Optional[str] = None


# @Route("/image-redirect")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageAsRedirect:
    format: Optional[str] = None


# @Route("/hello-image/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloImage(IReturn[bytes]):
    name: Optional[str] = None
    format: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    font_size: Optional[int] = None
    font_family: Optional[str] = None
    foreground: Optional[str] = None
    background: Optional[str] = None


# @Route("/secured")
# @ValidateRequest(Validator="IsAuthenticated")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Secured(IReturn[SecuredResponse]):
    name: Optional[str] = None


# @Route("/jwt")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateJwt(AuthUserSession, IReturn[CreateJwtResponse]):
    jwt_expiry: Optional[datetime.datetime] = None


# @Route("/jwt-refresh")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRefreshJwt(IReturn[CreateRefreshJwtResponse]):
    user_auth_id: Optional[str] = None
    jwt_expiry: Optional[datetime.datetime] = None


# @Route("/jwt-invalidate")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvalidateLastAccessToken(IReturn[EmptyResponse]):
    pass


# @Route("/logs")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ViewLogs(IReturn[str]):
    clear: bool = False


# @Route("/metadatatest")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTest(IReturn[MetadataTestResponse]):
    id: int = 0


# @Route("/metadatatest-array")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetadataTestArray(IReturn[List[MetadataTestChild]]):
    id: int = 0


# @Route("/example", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetExample(IReturn[GetExampleResponse]):
    pass


# @Route("/messages/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestMessage(IReturn[Message]):
    id: int = 0


# @Route("/randomids")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRandomIds(IReturn[GetRandomIdsResponse]):
    take: Optional[int] = None


# @Route("/textfile-test")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TextFileTest:
    as_attachment: bool = False


# @Route("/return/text")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnText:
    text: Optional[str] = None


# @Route("/return/html")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnHtml:
    text: Optional[str] = None


# @Route("/hello")
# @Route("/hello/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Hello(IReturn[HelloResponse]):
    # @Required()
    name: Optional[str] = None

    title: Optional[str] = None


# @Route("/hello-secure/{Name}")
# @ValidateRequest(Validator="IsAuthenticated")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloSecure(IReturn[HelloResponse]):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithNestedClass(IReturn[HelloResponse]):
    name: Optional[str] = None
    nested_class_prop: Optional[NestedClass] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloList(IReturn[List[ListResult]]):
    names: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloArray(IReturn[List[ArrayResult]]):
    names: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloMap(IReturn[Dict[str, ArrayResult]]):
    names: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloQueryResponse(IReturn[QueryResponse[str]]):
    names: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithEnum:
    enum_prop: Optional[EnumType] = None
    enum_type_flags: Optional[EnumTypeFlags] = None
    enum_with_values: Optional[EnumWithValues] = None
    nullable_enum_prop: Optional[EnumType] = None
    enum_flags: Optional[EnumFlags] = None
    enum_as_int: Optional[EnumAsInt] = None
    enum_style: Optional[EnumStyle] = None
    enum_style_members: Optional[EnumStyleMembers] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithEnumList:
    enum_prop: List[EnumType] = field(default_factory=list)
    enum_with_values: List[EnumWithValues] = field(default_factory=list)
    nullable_enum_prop: List[EnumType] = field(default_factory=list)
    enum_flags: List[EnumFlags] = field(default_factory=list)
    enum_style: List[EnumStyle] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithEnumMap:
    enum_prop: Dict[str, EnumType] = field(default_factory=dict)
    enum_with_values: Dict[str, EnumWithValues] = field(default_factory=dict)
    nullable_enum_prop: Dict[str, EnumType] = field(default_factory=dict)
    enum_flags: Dict[str, EnumFlags] = field(default_factory=dict)
    enum_style: Dict[str, EnumStyle] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloExternal:
    name: Optional[str] = None


# @Route("/allowed-attributes", "GET")
# @Api(Description="AllowedAttributes Description")
# @ApiResponse(Description="Your request was not understood", StatusCode=400)
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AllowedAttributes:
    """
    AllowedAttributes Description
    """

    # @ApiMember(DataType="double", Description="Range Description", IsRequired=true, ParameterType="path")
    range: float = 0.0
    """
    Range Description
    """


# @Route("/all-types")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloAllTypes(IReturn[HelloAllTypesResponse]):
    name: Optional[str] = None
    all_types: Optional[AllTypes] = None
    all_collection_types: Optional[AllCollectionTypes] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloSubAllTypes(AllTypesBase, IReturn[SubAllTypes]):
    hierarchy: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloString(IReturn[str]):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloVoid:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDataContract(IReturn[HelloWithDataContractResponse]):
    name: Optional[str] = None
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithDescription(IReturn[HelloWithDescriptionResponse]):
    """
    Description on HelloWithDescription type
    """

    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithInheritance(HelloBase, IReturn[HelloWithInheritanceResponse]):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithGenericInheritance(HelloBase1[Poco]):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithGenericInheritance2(HelloBase1[Hello]):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithReturn(IReturn[HelloWithAlternateReturnResponse]):
    name: Optional[str] = None


# @Route("/helloroute")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithRoute(IReturn[HelloWithRouteResponse]):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloWithType(IReturn[HelloWithTypeResponse]):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloInterface:
    poco: Optional[IPoco] = None
    empty_interface: Optional[IEmptyInterface] = None
    empty_class: Optional[EmptyClass] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloInnerTypes(IReturn[HelloInnerTypesResponse]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloBuiltin:
    day_of_week: Optional[DayOfWeek] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloGet(IReturn[HelloVerbResponse], IGet):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloPost(HelloBase, IReturn[HelloVerbResponse], IPost):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloPut(IReturn[HelloVerbResponse], IPut):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloDelete(IReturn[HelloVerbResponse], IDelete):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloPatch(IReturn[HelloVerbResponse], IPatch):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloReturnVoid(IReturnVoid):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnumRequest(IReturn[EnumResponse], IPut):
    operator: Optional[ScopeType] = None


# @Route("/hellozip")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloZip(IReturn[HelloZipResponse]):
    name: Optional[str] = None
    test: List[str] = field(default_factory=list)


# @Route("/ping")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Ping(IReturn[PingResponse]):
    pass


# @Route("/reset-connections")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResetConnections:
    pass


# @Route("/requires-role")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequiresRole(IReturn[RequiresRoleResponse]):
    pass


# @Route("/return/string")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnString(IReturn[str]):
    data: Optional[str] = None


# @Route("/return/bytes")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnBytes(IReturn[bytes]):
    data: bytes = field(default_factory=list)


# @Route("/return/stream")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnStream(IReturn[bytes]):
    data: bytes = field(default_factory=list)


# @Route("/return/json")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnJson:
    pass


# @Route("/return/json/header")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReturnJsonHeader:
    pass


# @Route("/write/json")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WriteJson:
    pass


# @Route("/Request1", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRequest1(IReturn[List[ReturnedDto]], IGet):
    pass


# @Route("/Request2", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRequest2(IReturn[List[ReturnedDto]], IGet):
    pass


# @Route("/sendjson")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendJson(IReturn[str]):
    id: int = 0
    name: Optional[str] = None
    request_stream: Optional[bytes] = None


# @Route("/sendtext")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendText(IReturn[str]):
    id: int = 0
    name: Optional[str] = None
    content_type: Optional[str] = None
    request_stream: Optional[bytes] = None


# @Route("/sendraw")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendRaw(IReturn[bytes]):
    id: int = 0
    name: Optional[str] = None
    content_type: Optional[str] = None
    request_stream: Optional[bytes] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendDefault(IReturn[SendVerbResponse]):
    id: int = 0


# @Route("/sendrestget/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendRestGet(IReturn[SendVerbResponse], IGet):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendGet(IReturn[SendVerbResponse], IGet):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendPost(IReturn[SendVerbResponse], IPost):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendPut(IReturn[SendVerbResponse], IPut):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendReturnVoid(IReturnVoid):
    id: int = 0


# @Route("/session")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSession(IReturn[GetSessionResponse]):
    pass


# @Route("/session/edit/{CustomName}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateSession(IReturn[GetSessionResponse]):
    custom_name: Optional[str] = None


# @Route("/Stuff")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetStuff(IReturn[GetStuffResponse]):
    # @ApiMember(DataType="DateTime", Name="Summary Date")
    summary_date: Optional[datetime.datetime] = None

    # @ApiMember(DataType="DateTime", Name="Summary End Date")
    summary_end_date: Optional[datetime.datetime] = None

    # @ApiMember(DataType="string", Name="Symbol")
    symbol: Optional[str] = None

    # @ApiMember(DataType="string", Name="Email")
    email: Optional[str] = None

    # @ApiMember(DataType="bool", Name="Is Enabled")
    is_enabled: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StoreLogs(IReturn[StoreLogsResponse]):
    loggers: List[Logger] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloAuth(IReturn[HelloResponse]):
    name: Optional[str] = None


# @Route("/testauth")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestAuth(IReturn[TestAuthResponse]):
    pass


# @Route("/testdata/AllTypes")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDataAllTypes(IReturn[AllTypes]):
    pass


# @Route("/testdata/AllCollectionTypes")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDataAllCollectionTypes(IReturn[AllCollectionTypes]):
    pass


# @Route("/void-response")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestVoidResponse:
    pass


# @Route("/null-response")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestNullResponse:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryRockstarAudit(QueryDbTenant[RockstarAuditTenant, RockstarAuto], IReturn[QueryResponse[RockstarAuto]]):
    id: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryRockstarAuditSubOr(QueryDb2[RockstarAuditTenant, RockstarAuto], IReturn[QueryResponse[RockstarAuto]]):
    first_name_starts_with: Optional[str] = None
    age_older_than: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryPocoBase(QueryDb[OnlyDefinedInGenericType], IReturn[QueryResponse[OnlyDefinedInGenericType]]):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryPocoIntoBase(QueryDb2[OnlyDefinedInGenericTypeFrom, OnlyDefinedInGenericTypeInto], IReturn[QueryResponse[OnlyDefinedInGenericTypeInto]]):
    id: int = 0


# @Route("/message/query/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MessageQuery(QueryDb["MessageQuery"], IReturn[QueryResponse["MessageQuery"]]):
    id: int = 0


# @Route("/rockstars", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryRockstars(QueryDb[Rockstar], IReturn[QueryResponse[Rockstar]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarAudit(RockstarBase, IReturn[RockstarWithIdResponse], ICreateDb[RockstarAudit]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarAuditTenant(CreateAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse], IReturn[RockstarWithIdAndResultResponse], IHasSessionId):
    session_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: datetime.datetime = datetime.datetime(1, 1, 1)
    date_died: Optional[datetime.datetime] = None
    living_status: Optional[LivingStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateRockstarAuditTenant(UpdateAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse], IReturn[RockstarWithIdAndResultResponse], IHasSessionId):
    session_id: Optional[str] = None
    id: int = 0
    first_name: Optional[str] = None
    living_status: Optional[LivingStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PatchRockstarAuditTenant(PatchAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse], IReturn[RockstarWithIdAndResultResponse], IHasSessionId):
    session_id: Optional[str] = None
    id: int = 0
    first_name: Optional[str] = None
    living_status: Optional[LivingStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SoftDeleteAuditTenant(SoftDeleteAuditTenantBase[RockstarAuditTenant, RockstarWithIdAndResultResponse], IReturn[RockstarWithIdAndResultResponse]):
    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarAuditMqToken(RockstarBase, IReturn[RockstarWithIdResponse], ICreateDb[RockstarAudit], IHasBearerToken):
    bearer_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RealDeleteAuditTenant(IReturn[RockstarWithIdAndCountResponse], IDeleteDb[RockstarAuditTenant], IHasSessionId):
    session_id: Optional[str] = None
    id: int = 0
    age: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRockstarVersion(RockstarBase, IReturn[RockstarWithIdAndRowVersionResponse], ICreateDb[RockstarVersion]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAnalyticsInfo(IReturn[GetAnalyticsInfoResponse], IGet):
    month: Optional[datetime.datetime] = None
    type: Optional[str] = None
    op: Optional[str] = None
    api_key: Optional[str] = None
    user_id: Optional[str] = None
    ip: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAnalyticsReports(IReturn[GetAnalyticsReportsResponse], IGet):
    month: Optional[datetime.datetime] = None
    filter: Optional[str] = None
    value: Optional[str] = None
    force: Optional[bool] = None

