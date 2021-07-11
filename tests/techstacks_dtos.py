""" Options:
Date: 2021-07-11 17:01:34
Version: 5.111
Tip: To override a DTO option, remove "//" prefix before updating
BaseUrl: https://techstacks.io

#GlobalNamespace: 
#MakePropertiesOptional: False
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


class PostType(str, Enum):
    ANNOUNCEMENT = 'Announcement'
    POST = 'Post'
    SHOWCASE = 'Showcase'
    QUESTION = 'Question'
    REQUEST = 'Request'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Post:
    id: int = 0
    organization_id: int = 0
    user_id: int = 0
    type: Optional[PostType] = None
    category_id: int = 0
    title: Optional[str] = None
    slug: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    # @StringLength(2147483647)
    content: Optional[str] = None

    # @StringLength(2147483647)
    content_html: Optional[str] = None

    pin_comment_id: Optional[int] = None
    technology_ids: Optional[List[int]] = None
    from_date: Optional[datetime.datetime] = None
    to_date: Optional[datetime.datetime] = None
    location: Optional[str] = None
    meta_type: Optional[str] = None
    meta: Optional[str] = None
    approved: bool = False
    up_votes: int = 0
    down_votes: int = 0
    points: int = 0
    views: int = 0
    favorites: int = 0
    subscribers: int = 0
    reply_count: int = 0
    comments_count: int = 0
    word_count: int = 0
    report_count: int = 0
    links_count: int = 0
    linked_to_count: int = 0
    score: int = 0
    rank: int = 0
    labels: Optional[List[str]] = None
    ref_user_ids: Optional[List[int]] = None
    ref_links: Optional[List[str]] = None
    mute_user_ids: Optional[List[int]] = None
    last_comment_date: Optional[datetime.datetime] = None
    last_comment_id: Optional[int] = None
    last_comment_user_id: Optional[int] = None
    deleted: Optional[datetime.datetime] = None
    deleted_by: Optional[str] = None
    locked: Optional[datetime.datetime] = None
    locked_by: Optional[str] = None
    hidden: Optional[datetime.datetime] = None
    hidden_by: Optional[str] = None
    status: Optional[str] = None
    status_date: Optional[datetime.datetime] = None
    status_by: Optional[str] = None
    archived: bool = False
    bumped: Optional[datetime.datetime] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    created_by: Optional[str] = None
    modified: datetime.datetime = datetime.datetime(1, 1, 1)
    modified_by: Optional[str] = None
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    ref_urn: Optional[str] = None


class ReportAction(str, Enum):
    DISMISS = 'Dismiss'
    DELETE = 'Delete'


class FlagType(str, Enum):
    VIOLATION = 'Violation'
    SPAM = 'Spam'
    ABUSIVE = 'Abusive'
    CONFIDENTIAL = 'Confidential'
    OFF_TOPIC = 'OffTopic'
    OTHER = 'Other'


class Frequency(IntEnum):
    DAILY = 1
    WEEKLY = 7
    MONTHLY = 30
    QUARTERLY = 90


class TechnologyTier(str, Enum):
    PROGRAMMING_LANGUAGE = 'ProgrammingLanguage'
    CLIENT = 'Client'
    HTTP = 'Http'
    SERVER = 'Server'
    DATA = 'Data'
    SOFTWARE_INFRASTRUCTURE = 'SoftwareInfrastructure'
    OPERATING_SYSTEM = 'OperatingSystem'
    HARDWARE_INFRASTRUCTURE = 'HardwareInfrastructure'
    THIRD_PARTY_SERVICES = 'ThirdPartyServices'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyBase:
    id: int = 0
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_url: Optional[str] = None
    product_url: Optional[str] = None
    logo_url: Optional[str] = None
    description: Optional[str] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    created_by: Optional[str] = None
    last_modified: datetime.datetime = datetime.datetime(1, 1, 1)
    last_modified_by: Optional[str] = None
    owner_id: Optional[str] = None
    slug: Optional[str] = None
    logo_approved: bool = False
    is_locked: bool = False
    tier: Optional[TechnologyTier] = None
    last_status_update: Optional[datetime.datetime] = None
    organization_id: Optional[int] = None
    comments_post_id: Optional[int] = None
    view_count: int = 0
    fav_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Technology(TechnologyBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyView:
    id: Optional[int] = None
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_url: Optional[str] = None
    product_url: Optional[str] = None
    logo_url: Optional[str] = None
    description: Optional[str] = None
    created: Optional[datetime.datetime] = None
    created_by: Optional[str] = None
    last_modified: Optional[datetime.datetime] = None
    last_modified_by: Optional[str] = None
    owner_id: Optional[str] = None
    slug: Optional[str] = None
    logo_approved: Optional[bool] = None
    is_locked: Optional[bool] = None
    tier: Optional[TechnologyTier] = None
    last_status_update: Optional[datetime.datetime] = None
    organization_id: Optional[int] = None
    comments_post_id: Optional[int] = None
    view_count: Optional[int] = None
    fav_count: Optional[int] = None


class IRegisterStats:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyStackBase:
    id: int = 0
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    description: Optional[str] = None
    app_url: Optional[str] = None
    screenshot_url: Optional[str] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    created_by: Optional[str] = None
    last_modified: datetime.datetime = datetime.datetime(1, 1, 1)
    last_modified_by: Optional[str] = None
    is_locked: bool = False
    owner_id: Optional[str] = None
    slug: Optional[str] = None
    # @StringLength(2147483647)
    details: Optional[str] = None

    # @StringLength(2147483647)
    details_html: Optional[str] = None

    last_status_update: Optional[datetime.datetime] = None
    organization_id: Optional[int] = None
    comments_post_id: Optional[int] = None
    view_count: int = 0
    fav_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyStack(TechnologyStackBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyStackView:
    id: Optional[int] = None
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    description: Optional[str] = None
    app_url: Optional[str] = None
    screenshot_url: Optional[str] = None
    created: Optional[datetime.datetime] = None
    created_by: Optional[str] = None
    last_modified: Optional[datetime.datetime] = None
    last_modified_by: Optional[str] = None
    is_locked: Optional[bool] = None
    owner_id: Optional[str] = None
    slug: Optional[str] = None
    details: Optional[str] = None
    details_html: Optional[str] = None
    last_status_update: Optional[datetime.datetime] = None
    organization_id: Optional[int] = None
    comments_post_id: Optional[int] = None
    view_count: Optional[int] = None
    fav_count: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserVoiceUser:
    id: int = 0
    name: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime(1, 1, 1)
    updated_at: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserVoiceComment:
    text: Optional[str] = None
    formatted_text: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime(1, 1, 1)
    creator: Optional[UserVoiceUser] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostComment:
    id: int = 0
    post_id: int = 0
    user_id: int = 0
    reply_id: Optional[int] = None
    # @StringLength(2147483647)
    content: Optional[str] = None

    # @StringLength(2147483647)
    content_html: Optional[str] = None

    score: int = 0
    rank: int = 0
    up_votes: int = 0
    down_votes: int = 0
    favorites: int = 0
    word_count: int = 0
    report_count: int = 0
    deleted: Optional[datetime.datetime] = None
    hidden: Optional[datetime.datetime] = None
    modified: datetime.datetime = datetime.datetime(1, 1, 1)
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    created_by: Optional[str] = None
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    ref_urn: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Organization:
    id: int = 0
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    description_html: Optional[str] = None
    color: Optional[str] = None
    text_color: Optional[str] = None
    link_color: Optional[str] = None
    background_color: Optional[str] = None
    background_url: Optional[str] = None
    logo_url: Optional[str] = None
    hero_url: Optional[str] = None
    lang: Optional[str] = None
    default_post_type: Optional[str] = None
    default_subscription_post_types: Optional[List[str]] = None
    post_types: Optional[List[str]] = None
    moderator_post_types: Optional[List[str]] = None
    delete_posts_with_report_count: int = 0
    disable_invites: Optional[bool] = None
    up_votes: int = 0
    down_votes: int = 0
    views: int = 0
    favorites: int = 0
    subscribers: int = 0
    comments_count: int = 0
    posts_count: int = 0
    score: int = 0
    rank: int = 0
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    hidden: Optional[datetime.datetime] = None
    hidden_by: Optional[str] = None
    locked: Optional[datetime.datetime] = None
    locked_by: Optional[str] = None
    deleted: Optional[datetime.datetime] = None
    deleted_by: Optional[str] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    created_by: Optional[str] = None
    modified: datetime.datetime = datetime.datetime(1, 1, 1)
    modified_by: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OrganizationLabel:
    slug: Optional[str] = None
    organization_id: int = 0
    description: Optional[str] = None
    color: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Category:
    id: int = 0
    organization_id: int = 0
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None
    technology_ids: Optional[List[int]] = None
    comments_count: int = 0
    posts_count: int = 0
    score: int = 0
    rank: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OrganizationMember:
    id: int = 0
    organization_id: int = 0
    user_id: int = 0
    user_name: Optional[str] = None
    is_owner: bool = False
    is_moderator: bool = False
    deny_all: bool = False
    deny_posts: bool = False
    deny_comments: bool = False
    notes: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OrganizationMemberInvite:
    id: int = 0
    organization_id: int = 0
    user_id: int = 0
    user_name: Optional[str] = None
    dismissed: Optional[datetime.datetime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostReportInfo:
    id: int = 0
    organization_id: int = 0
    post_id: int = 0
    user_id: int = 0
    user_name: Optional[str] = None
    flag_type: Optional[FlagType] = None
    report_notes: Optional[str] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    acknowledged: Optional[datetime.datetime] = None
    acknowledged_by: Optional[str] = None
    dismissed: Optional[datetime.datetime] = None
    dismissed_by: Optional[str] = None
    title: Optional[str] = None
    report_count: int = 0
    created_by: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostCommentReportInfo:
    id: int = 0
    organization_id: int = 0
    post_id: int = 0
    post_comment_id: int = 0
    user_id: int = 0
    user_name: Optional[str] = None
    flag_type: Optional[FlagType] = None
    report_notes: Optional[str] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    acknowledged: Optional[datetime.datetime] = None
    acknowledged_by: Optional[str] = None
    dismissed: Optional[datetime.datetime] = None
    dismissed_by: Optional[str] = None
    content_html: Optional[str] = None
    report_count: int = 0
    created_by: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserRef:
    id: int = 0
    user_name: Optional[str] = None
    email: Optional[str] = None
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    ref_urn: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OrganizationSubscription:
    id: int = 0
    organization_id: int = 0
    user_id: int = 0
    user_name: Optional[str] = None
    post_types: Optional[List[str]] = None
    frequency_days: Optional[int] = None
    last_synced_id: Optional[int] = None
    last_synced: Optional[datetime.datetime] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserActivity:
    id: int = 0
    user_name: Optional[str] = None
    karma: int = 0
    technology_count: int = 0
    tech_stacks_count: int = 0
    posts_count: int = 0
    post_up_votes: int = 0
    post_down_votes: int = 0
    comment_up_votes: int = 0
    comment_down_votes: int = 0
    post_comments_count: int = 0
    pinned_comment_count: int = 0
    post_report_count: int = 0
    post_comment_report_count: int = 0
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    modified: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyHistory(TechnologyBase):
    technology_id: int = 0
    operation: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyStackHistory(TechnologyStackBase):
    technology_stack_id: int = 0
    operation: Optional[str] = None
    technology_ids: Optional[List[int]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserInfo:
    user_name: Optional[str] = None
    avatar_url: Optional[str] = None
    stacks_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyInfo:
    tier: Optional[TechnologyTier] = None
    slug: Optional[str] = None
    name: Optional[str] = None
    logo_url: Optional[str] = None
    stacks_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechnologyInStack(TechnologyBase):
    technology_id: int = 0
    technology_stack_id: int = 0
    justification: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TechStackDetails(TechnologyStackBase):
    technology_choices: Optional[List[TechnologyInStack]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LabelInfo:
    slug: Optional[str] = None
    color: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CategoryInfo:
    id: int = 0
    name: Optional[str] = None
    slug: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OrganizationInfo:
    id: int = 0
    name: Optional[str] = None
    slug: Optional[str] = None
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    up_votes: Optional[int] = None
    down_votes: Optional[int] = None
    members_count: int = 0
    rank: int = 0
    disable_invites: Optional[bool] = None
    lang: Optional[str] = None
    post_types: Optional[List[str]] = None
    moderator_post_types: Optional[List[str]] = None
    locked: Optional[datetime.datetime] = None
    labels: Optional[List[LabelInfo]] = None
    categories: Optional[List[CategoryInfo]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Option:
    name: Optional[str] = None
    title: Optional[str] = None
    value: Optional[TechnologyTier] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationResponse:
    cache: int = 0
    id: int = 0
    slug: Optional[str] = None
    organization: Optional[Organization] = None
    labels: Optional[List[OrganizationLabel]] = None
    categories: Optional[List[Category]] = None
    owners: Optional[List[OrganizationMember]] = None
    moderators: Optional[List[OrganizationMember]] = None
    members_count: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationMembersResponse:
    organization_id: int = 0
    results: Optional[List[OrganizationMember]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationAdminResponse:
    labels: Optional[List[OrganizationLabel]] = None
    members: Optional[List[OrganizationMember]] = None
    member_invites: Optional[List[OrganizationMemberInvite]] = None
    reported_posts: Optional[List[PostReportInfo]] = None
    reported_post_comments: Optional[List[PostCommentReportInfo]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateOrganizationForTechnologyResponse:
    organization_id: int = 0
    organization_slug: Optional[str] = None
    comments_post_id: int = 0
    comments_post_slug: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateOrganizationResponse:
    id: int = 0
    slug: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OrganizationLabelResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddOrganizationCategoryResponse:
    id: int = 0
    slug: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationCategoryResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddOrganizationMemberResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationMemberResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetOrganizationMembersResponse:
    user_ids_added: Optional[List[int]] = None
    user_ids_removed: Optional[List[int]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationMemberInvitesResponse:
    results: Optional[List[OrganizationMemberInvite]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestOrganizationMemberInviteResponse:
    organization_id: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationMemberInviteResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPostResponse:
    cache: int = 0
    post: Optional[Post] = None
    comments: Optional[List[PostComment]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePostResponse:
    id: int = 0
    slug: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePostResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePostResponse:
    id: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePostCommentResponse:
    id: int = 0
    post_id: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePostCommentResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePostCommentResponse:
    id: int = 0
    post_id: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPostCommentVotesResponse:
    post_id: int = 0
    up_voted_comment_ids: Optional[List[int]] = None
    down_voted_comment_ids: Optional[List[int]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PinPostCommentResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersByEmailsResponse:
    results: Optional[List[UserRef]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPostActivityResponse:
    up_voted_post_ids: Optional[List[int]] = None
    down_voted_post_ids: Optional[List[int]] = None
    favorite_post_ids: Optional[List[int]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserOrganizationsResponse:
    members: Optional[List[OrganizationMember]] = None
    member_invites: Optional[List[OrganizationMemberInvite]] = None
    subscriptions: Optional[List[OrganizationSubscription]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostVoteResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostFavoriteResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostReportResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostCommentVoteResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostCommentReportResponse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SessionInfoResponse:
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    id: Optional[str] = None
    referrer_url: Optional[str] = None
    user_auth_id: Optional[str] = None
    user_auth_name: Optional[str] = None
    user_name: Optional[str] = None
    display_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime(1, 1, 1)
    last_modified: datetime.datetime = datetime.datetime(1, 1, 1)
    roles: Optional[List[str]] = None
    permissions: Optional[List[str]] = None
    is_authenticated: bool = False
    auth_provider: Optional[str] = None
    profile_url: Optional[str] = None
    github_profile_url: Optional[str] = None
    twitter_profile_url: Optional[str] = None
    access_token: Optional[str] = None
    avatar_url: Optional[str] = None
    tech_stacks: Optional[List[TechnologyStack]] = None
    favorite_tech_stacks: Optional[List[TechnologyStack]] = None
    favorite_technologies: Optional[List[Technology]] = None
    user_activity: Optional[UserActivity] = None
    members: Optional[List[OrganizationMember]] = None
    member_invites: Optional[List[OrganizationMemberInvite]] = None
    subscriptions: Optional[List[OrganizationSubscription]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyPreviousVersionsResponse:
    results: Optional[List[TechnologyHistory]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllTechnologiesResponse:
    results: Optional[List[Technology]] = None
    total: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyResponse:
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    technology: Optional[Technology] = None
    technology_stacks: Optional[List[TechnologyStack]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyFavoriteDetailsResponse:
    users: Optional[List[str]] = None
    favorite_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTechnologyResponse:
    result: Optional[Technology] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateTechnologyResponse:
    result: Optional[Technology] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteTechnologyResponse:
    result: Optional[Technology] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyStackPreviousVersionsResponse:
    results: Optional[List[TechnologyStackHistory]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPageStatsResponse:
    type: Optional[str] = None
    slug: Optional[str] = None
    view_count: int = 0
    fav_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HourlyTaskResponse:
    meta: Optional[Dict[str, str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OverviewResponse:
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    top_users: Optional[List[UserInfo]] = None
    top_technologies: Optional[List[TechnologyInfo]] = None
    latest_tech_stacks: Optional[List[TechStackDetails]] = None
    popular_tech_stacks: Optional[List[TechnologyStack]] = None
    all_organizations: Optional[List[OrganizationInfo]] = None
    top_technologies_by_tier: Optional[Dict[str, List[TechnologyInfo]]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppOverviewResponse:
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    all_tiers: Optional[List[Option]] = None
    top_technologies: Optional[List[TechnologyInfo]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllTechnologyStacksResponse:
    results: Optional[List[TechnologyStack]] = None
    total: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyStackResponse:
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    result: Optional[TechStackDetails] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyStackFavoriteDetailsResponse:
    users: Optional[List[str]] = None
    favorite_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetConfigResponse:
    all_tiers: Optional[List[Option]] = None
    all_post_types: Optional[List[Option]] = None
    all_flag_types: Optional[List[Option]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTechnologyStackResponse:
    result: Optional[TechStackDetails] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateTechnologyStackResponse:
    result: Optional[TechStackDetails] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteTechnologyStackResponse:
    result: Optional[TechStackDetails] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFavoriteTechStackResponse:
    results: Optional[List[TechnologyStack]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FavoriteTechStackResponse:
    result: Optional[TechnologyStack] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFavoriteTechnologiesResponse:
    results: Optional[List[Technology]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FavoriteTechnologyResponse:
    result: Optional[Technology] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserFeedResponse:
    results: Optional[List[TechStackDetails]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersKarmaResponse:
    results: Optional[Dict[int, int]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserInfoResponse:
    id: int = 0
    user_name: Optional[str] = None
    created: datetime.datetime = datetime.datetime(1, 1, 1)
    avatar_url: Optional[str] = None
    tech_stacks: Optional[List[TechnologyStack]] = None
    favorite_tech_stacks: Optional[List[TechnologyStack]] = None
    favorite_technologies: Optional[List[Technology]] = None
    user_activity: Optional[UserActivity] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SyncDiscourseSiteResponse:
    time_taken: Optional[str] = None
    user_logs: Optional[List[str]] = None
    posts_logs: Optional[List[str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LogoUrlApprovalResponse:
    result: Optional[Technology] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LockStackResponse:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTestRespoonse:
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportUserResponse:
    id: int = 0
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportUserVoiceSuggestionResponse:
    post_id: int = 0
    post_slug: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


# @Route("/ping")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Ping:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DummyTypes:
    post: Optional[List[Post]] = None


# @Route("/orgs/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganization(IReturn[GetOrganizationResponse], IGet):
    id: Optional[int] = None


# @Route("/organizations/{Slug}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationBySlug(IReturn[GetOrganizationResponse], IGet):
    slug: Optional[str] = None


# @Route("/orgs/{Id}/members", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationMembers(IReturn[GetOrganizationMembersResponse], IGet):
    id: int = 0


# @Route("/orgs/{Id}/admin", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationAdmin(IReturn[GetOrganizationAdminResponse], IGet):
    id: int = 0


# @Route("/orgs/posts/new", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateOrganizationForTechnology(IReturn[CreateOrganizationForTechnologyResponse], IPost):
    technology_id: Optional[int] = None
    tech_stack_id: Optional[int] = None


# @Route("/orgs", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateOrganization(IReturn[CreateOrganizationResponse], IPost):
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    ref_urn: Optional[str] = None


# @Route("/orgs/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganization(IReturn[UpdateOrganizationResponse], IPut):
    id: int = 0
    slug: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None
    text_color: Optional[str] = None
    link_color: Optional[str] = None
    background_color: Optional[str] = None
    background_url: Optional[str] = None
    logo_url: Optional[str] = None
    hero_url: Optional[str] = None
    lang: Optional[str] = None
    delete_posts_with_report_count: int = 0
    disable_invites: Optional[bool] = None
    default_post_type: Optional[str] = None
    default_subscription_post_types: Optional[List[str]] = None
    post_types: Optional[List[str]] = None
    moderator_post_types: Optional[List[str]] = None
    technology_ids: Optional[List[int]] = None


# @Route("/orgs/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteOrganization(IReturnVoid, IDelete):
    id: int = 0


# @Route("/orgs/{Id}/lock", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LockOrganization(IReturnVoid, IPut):
    id: int = 0
    lock: bool = False
    reason: Optional[str] = None


# @Route("/orgs/{OrganizationId}/labels", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddOrganizationLabel(IReturn[OrganizationLabelResponse], IPost):
    organization_id: int = 0
    slug: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None


# @Route("/orgs/{OrganizationId}/members/{Slug}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationLabel(IReturn[OrganizationLabelResponse], IPut):
    organization_id: int = 0
    slug: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None


# @Route("/orgs/{OrganizationId}/labels/{Slug}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveOrganizationLabel(IReturnVoid, IDelete):
    organization_id: int = 0
    slug: Optional[str] = None


# @Route("/orgs/{OrganizationId}/categories", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddOrganizationCategory(IReturn[AddOrganizationCategoryResponse], IPost):
    organization_id: int = 0
    slug: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    technology_ids: Optional[List[int]] = None


# @Route("/orgs/{OrganizationId}/categories/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationCategory(IReturn[UpdateOrganizationCategoryResponse], IPut):
    organization_id: int = 0
    id: int = 0
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    technology_ids: Optional[List[int]] = None


# @Route("/orgs/{OrganizationId}/categories/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteOrganizationCategory(IReturnVoid, IDelete):
    organization_id: int = 0
    id: int = 0


# @Route("/orgs/{OrganizationId}/members", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddOrganizationMember(IReturn[AddOrganizationMemberResponse], IPost):
    organization_id: int = 0
    user_name: Optional[str] = None
    is_owner: bool = False
    is_moderator: bool = False
    deny_posts: bool = False
    deny_comments: bool = False
    deny_all: bool = False
    notes: Optional[str] = None


# @Route("/orgs/{OrganizationId}/members/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationMember(IReturn[UpdateOrganizationMemberResponse], IPut):
    organization_id: int = 0
    user_id: int = 0
    is_owner: bool = False
    is_moderator: bool = False
    deny_posts: bool = False
    deny_comments: bool = False
    deny_all: bool = False
    notes: Optional[str] = None


# @Route("/orgs/{OrganizationId}/members/{UserId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveOrganizationMember(IReturnVoid, IDelete):
    organization_id: int = 0
    user_id: int = 0


# @Route("/orgs/{OrganizationId}/members/set", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetOrganizationMembers(IReturn[SetOrganizationMembersResponse], IPost):
    organization_id: int = 0
    github_user_names: Optional[List[str]] = None
    twitter_user_names: Optional[List[str]] = None
    emails: Optional[List[str]] = None
    remove_unspecified_members: bool = False
    is_owner: bool = False
    is_moderator: bool = False
    deny_posts: bool = False
    deny_comments: bool = False
    deny_all: bool = False


# @Route("/orgs/{OrganizationId}/invites", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOrganizationMemberInvites(IReturn[GetOrganizationMemberInvitesResponse], IGet):
    organization_id: int = 0


# @Route("/orgs/{OrganizationId}/invites", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestOrganizationMemberInvite(IReturn[RequestOrganizationMemberInviteResponse], IPost):
    organization_id: int = 0


# @Route("/orgs/{OrganizationId}/invites/{UserId}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOrganizationMemberInvite(IReturn[UpdateOrganizationMemberInviteResponse], IPut):
    organization_id: int = 0
    user_name: Optional[str] = None
    approve: bool = False
    dismiss: bool = False


# @Route("/posts", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryPosts(QueryDb[Post], IReturn[QueryResponse[Post]], IGet):
    ids: Optional[List[int]] = None
    organization_id: Optional[int] = None
    organization_ids: Optional[List[int]] = None
    types: Optional[List[str]] = None
    any_technology_ids: Optional[List[int]] = None
    is_: Optional[List[str]] = field(metadata=config(field_name='is'), default=None)


# @Route("/posts/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPost(IReturn[GetPostResponse], IGet):
    id: int = 0
    include: Optional[str] = None


# @Route("/posts", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePost(IReturn[CreatePostResponse], IPost):
    organization_id: int = 0
    type: Optional[PostType] = None
    category_id: int = 0
    title: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    content: Optional[str] = None
    lock: Optional[bool] = None
    technology_ids: Optional[List[int]] = None
    labels: Optional[List[str]] = None
    from_date: Optional[datetime.datetime] = None
    to_date: Optional[datetime.datetime] = None
    meta_type: Optional[str] = None
    meta: Optional[str] = None
    ref_id: Optional[int] = None
    ref_source: Optional[str] = None
    ref_urn: Optional[str] = None


# @Route("/posts/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePost(IReturn[UpdatePostResponse], IPut):
    id: int = 0
    organization_id: int = 0
    type: Optional[PostType] = None
    category_id: int = 0
    title: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    content: Optional[str] = None
    lock: Optional[bool] = None
    technology_ids: Optional[List[int]] = None
    labels: Optional[List[str]] = None
    from_date: Optional[datetime.datetime] = None
    to_date: Optional[datetime.datetime] = None
    meta_type: Optional[str] = None
    meta: Optional[str] = None


# @Route("/posts/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePost(IReturn[DeletePostResponse], IDelete):
    id: int = 0


# @Route("/posts/{Id}/lock", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LockPost(IReturnVoid, IPut):
    id: int = 0
    lock: bool = False
    reason: Optional[str] = None


# @Route("/posts/{Id}/hide", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HidePost(IReturnVoid, IPut):
    id: int = 0
    hide: bool = False
    reason: Optional[str] = None


# @Route("/posts/{Id}/status/{Status}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChangeStatusPost(IReturnVoid, IPut):
    id: int = 0
    status: Optional[str] = None
    reason: Optional[str] = None


# @Route("/posts/{PostId}/report/{Id}", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActionPostReport(IReturnVoid, IPost):
    post_id: int = 0
    id: int = 0
    report_action: Optional[ReportAction] = None


# @Route("/posts/{PostId}/comments", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePostComment(IReturn[CreatePostCommentResponse], IPost):
    post_id: int = 0
    reply_id: Optional[int] = None
    content: Optional[str] = None


# @Route("/posts/{PostId}/comments/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePostComment(IReturn[UpdatePostCommentResponse], IPut):
    id: int = 0
    post_id: int = 0
    content: Optional[str] = None


# @Route("/posts/{PostId}/comments/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePostComment(IReturn[DeletePostCommentResponse], IDelete):
    id: int = 0
    post_id: int = 0


# @Route("/posts/{PostId}/comments/{PostCommentId}/report/{Id}", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActionPostCommentReport(IReturnVoid, IPost):
    id: int = 0
    post_comment_id: int = 0
    post_id: int = 0
    report_action: Optional[ReportAction] = None


# @Route("/user/comments/votes")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPostCommentVotes(IReturn[GetUserPostCommentVotesResponse], IGet):
    post_id: int = 0


# @Route("/posts/{PostId}/comments/{Id}/pin", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PinPostComment(IReturn[PinPostCommentResponse], IPut):
    id: int = 0
    post_id: int = 0
    pin: bool = False


# @Route("/users/by-email")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersByEmails(IReturn[GetUsersByEmailsResponse], IGet):
    emails: Optional[List[str]] = None


# @Route("/user/posts/activity")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPostActivity(IReturn[GetUserPostActivityResponse], IGet):
    pass


# @Route("/user/organizations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserOrganizations(IReturn[GetUserOrganizationsResponse], IGet):
    pass


# @Route("/posts/{Id}/vote", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostVote(IReturn[UserPostVoteResponse], IPut):
    id: int = 0
    weight: int = 0


# @Route("/posts/{Id}/favorite", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostFavorite(IReturn[UserPostFavoriteResponse], IPut):
    id: int = 0


# @Route("/posts/{Id}/report", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostReport(IReturn[UserPostReportResponse], IPut):
    id: int = 0
    flag_type: Optional[FlagType] = None
    report_notes: Optional[str] = None


# @Route("/posts/{PostId}/comments/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostCommentVote(IReturn[UserPostCommentVoteResponse], IGet):
    id: int = 0
    post_id: int = 0
    weight: int = 0


# @Route("/posts/{PostId}/comments/{Id}/report", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserPostCommentReport(IReturn[UserPostCommentReportResponse], IPut):
    id: int = 0
    post_id: int = 0
    flag_type: Optional[FlagType] = None
    report_notes: Optional[str] = None


# @Route("/prerender/{Path*}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StorePreRender(IReturnVoid, IPut):
    path: Optional[str] = None


# @Route("/prerender/{Path*}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPreRender(IReturn[str], IGet):
    path: Optional[str] = None


# @Route("/my-session")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SessionInfo(IReturn[SessionInfoResponse], IGet):
    pass


# @Route("/orgs/{OrganizationId}/subscribe", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubscribeToOrganization(IReturnVoid, IPut):
    organization_id: int = 0
    post_types: Optional[List[PostType]] = None
    frequency: Optional[Frequency] = None


# @Route("/posts/{PostId}/subscribe", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubscribeToPost(IReturnVoid, IPut):
    post_id: int = 0


# @Route("/orgs/{OrganizationId}/subscribe", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteOrganizationSubscription(IReturnVoid, IDelete):
    organization_id: int = 0


# @Route("/posts/{PostId}/subscribe", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePostSubscription(IReturnVoid, IDelete):
    post_id: int = 0


# @Route("/technology/{Slug}/previous-versions", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyPreviousVersions(IReturn[GetTechnologyPreviousVersionsResponse], IGet):
    slug: Optional[str] = None


# @Route("/technology", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllTechnologies(IReturn[GetAllTechnologiesResponse], IGet):
    pass


# @Route("/technology/search")
# @AutoQueryViewer(DefaultSearchField="Tier", DefaultSearchText="Data", DefaultSearchType="=", Description="Explore different Technologies", IconUrl="octicon:database", Title="Find Technologies")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTechnologies(QueryDb2[Technology, TechnologyView], IReturn[QueryResponse[TechnologyView]], IGet):
    ids: Optional[List[int]] = None
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    name_contains: Optional[str] = None
    vendor_name_contains: Optional[str] = None
    description_contains: Optional[str] = None


# @Route("/technology/query")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryTechnology(QueryDb2[Technology, TechnologyView], IReturn[QueryResponse[TechnologyView]], IGet):
    ids: Optional[List[int]] = None
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    name_contains: Optional[str] = None
    vendor_name_contains: Optional[str] = None
    description_contains: Optional[str] = None


# @Route("/technology/{Slug}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnology(IReturn[GetTechnologyResponse], IRegisterStats, IGet):
    slug: Optional[str] = None


# @Route("/technology/{Slug}/favorites")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyFavoriteDetails(IReturn[GetTechnologyFavoriteDetailsResponse], IGet):
    slug: Optional[str] = None


# @Route("/technology", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTechnology(IReturn[CreateTechnologyResponse], IPost):
    name: Optional[str] = None
    slug: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_url: Optional[str] = None
    product_url: Optional[str] = None
    logo_url: Optional[str] = None
    description: Optional[str] = None
    is_locked: bool = False
    tier: Optional[TechnologyTier] = None


# @Route("/technology/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateTechnology(IReturn[UpdateTechnologyResponse], IPut):
    id: int = 0
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_url: Optional[str] = None
    product_url: Optional[str] = None
    logo_url: Optional[str] = None
    description: Optional[str] = None
    is_locked: bool = False
    tier: Optional[TechnologyTier] = None


# @Route("/technology/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteTechnology(IReturn[DeleteTechnologyResponse], IDelete):
    id: int = 0


# @Route("/techstacks/{Slug}/previous-versions", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyStackPreviousVersions(IReturn[GetTechnologyStackPreviousVersionsResponse], IGet):
    slug: Optional[str] = None


# @Route("/pagestats/{Type}/{Slug}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPageStats(IReturn[GetPageStatsResponse], IGet):
    type: Optional[str] = None
    slug: Optional[str] = None
    id: Optional[int] = None


# @Route("/cache/clear")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ClearCache(IReturn[str], IGet):
    pass


# @Route("/tasks/hourly")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HourlyTask(IReturn[HourlyTaskResponse], IGet):
    force: bool = False


# @Route("/techstacks/search")
# @AutoQueryViewer(DefaultSearchField="Description", DefaultSearchText="ServiceStack", DefaultSearchType="Contains", Description="Explore different Technology Stacks", IconUrl="material-icons:cloud", Title="Find Technology Stacks")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTechStacks(QueryDb2[TechnologyStack, TechnologyStackView], IReturn[QueryResponse[TechnologyStackView]], IGet):
    ids: Optional[List[int]] = None
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    name_contains: Optional[str] = None
    vendor_name_contains: Optional[str] = None
    description_contains: Optional[str] = None


# @Route("/techstacks/query")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryTechStacks(QueryDb2[TechnologyStack, TechnologyStackView], IReturn[QueryResponse[TechnologyStackView]], IGet):
    ids: Optional[List[int]] = None
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    name_contains: Optional[str] = None
    vendor_name_contains: Optional[str] = None
    description_contains: Optional[str] = None


# @Route("/overview")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Overview(IReturn[OverviewResponse], IGet):
    reload: bool = False


# @Route("/app-overview")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppOverview(IReturn[AppOverviewResponse], IGet):
    reload: bool = False


# @Route("/techstacks", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllTechnologyStacks(IReturn[GetAllTechnologyStacksResponse], IGet):
    pass


# @Route("/techstacks/{Slug}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyStack(IReturn[GetTechnologyStackResponse], IRegisterStats, IGet):
    slug: Optional[str] = None


# @Route("/techstacks/{Slug}/favorites")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTechnologyStackFavoriteDetails(IReturn[GetTechnologyStackFavoriteDetailsResponse], IGet):
    slug: Optional[str] = None


# @Route("/config")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetConfig(IReturn[GetConfigResponse], IGet):
    pass


# @Route("/techstacks", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTechnologyStack(IReturn[CreateTechnologyStackResponse], IPost):
    name: Optional[str] = None
    slug: Optional[str] = None
    vendor_name: Optional[str] = None
    app_url: Optional[str] = None
    screenshot_url: Optional[str] = None
    description: Optional[str] = None
    details: Optional[str] = None
    is_locked: bool = False
    technology_ids: Optional[List[int]] = None


# @Route("/techstacks/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateTechnologyStack(IReturn[UpdateTechnologyStackResponse], IPut):
    id: int = 0
    name: Optional[str] = None
    vendor_name: Optional[str] = None
    app_url: Optional[str] = None
    screenshot_url: Optional[str] = None
    description: Optional[str] = None
    details: Optional[str] = None
    is_locked: bool = False
    technology_ids: Optional[List[int]] = None


# @Route("/techstacks/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteTechnologyStack(IReturn[DeleteTechnologyStackResponse], IDelete):
    id: int = 0


# @Route("/favorites/techtacks", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFavoriteTechStack(IReturn[GetFavoriteTechStackResponse], IGet):
    technology_stack_id: int = 0


# @Route("/favorites/techtacks/{TechnologyStackId}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddFavoriteTechStack(IReturn[FavoriteTechStackResponse], IPut):
    technology_stack_id: int = 0


# @Route("/favorites/techtacks/{TechnologyStackId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveFavoriteTechStack(IReturn[FavoriteTechStackResponse], IDelete):
    technology_stack_id: int = 0


# @Route("/favorites/technology", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFavoriteTechnologies(IReturn[GetFavoriteTechnologiesResponse], IGet):
    technology_id: int = 0


# @Route("/favorites/technology/{TechnologyId}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddFavoriteTechnology(IReturn[FavoriteTechnologyResponse], IPut):
    technology_id: int = 0


# @Route("/favorites/technology/{TechnologyId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveFavoriteTechnology(IReturn[FavoriteTechnologyResponse], IDelete):
    technology_id: int = 0


# @Route("/my-feed")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserFeed(IReturn[GetUserFeedResponse], IGet):
    pass


# @Route("/users/karma", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersKarma(IReturn[GetUsersKarmaResponse], IGet):
    user_ids: Optional[List[int]] = None


# @Route("/userinfo/{UserName}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserInfo(IReturn[GetUserInfoResponse], IGet):
    user_name: Optional[str] = None


# @Route("/users/{UserName}/avatar", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserAvatar(IGet):
    user_name: Optional[str] = None


# @Route("/mq/start")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MqStart(IReturn[str]):
    pass


# @Route("/mq/stop")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MqStop(IReturn[str]):
    pass


# @Route("/mq/stats")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MqStats(IReturn[str]):
    pass


# @Route("/mq/status")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MqStatus(IReturn[str]):
    pass


# @Route("/sync/discourse/{Site}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SyncDiscourseSite(IReturn[SyncDiscourseSiteResponse], IPost):
    site: Optional[str] = None


# @Route("/admin/technology/{TechnologyId}/logo")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LogoUrlApproval(IReturn[LogoUrlApprovalResponse], IPut):
    technology_id: int = 0
    approved: bool = False


# @Route("/admin/techstacks/{TechnologyStackId}/lock")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LockTechStack(IReturn[LockStackResponse], IPut):
    technology_stack_id: int = 0
    is_locked: bool = False


# @Route("/admin/technology/{TechnologyId}/lock")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LockTech(IReturn[LockStackResponse], IPut):
    technology_id: int = 0
    is_locked: bool = False


# @Route("/email/post/{PostId}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTest(IReturn[EmailTestRespoonse]):
    post_id: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportUser(IReturn[ImportUserResponse], IPost):
    user_name: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    company: Optional[str] = None
    ref_source: Optional[str] = None
    ref_id: Optional[int] = None
    ref_id_str: Optional[str] = None
    ref_urn: Optional[str] = None
    default_profile_url: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


# @Route("/import/uservoice/suggestion")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportUserVoiceSuggestion(IReturn[ImportUserVoiceSuggestionResponse], IPost):
    organization_id: int = 0
    url: Optional[str] = None
    id: int = 0
    topic_id: int = 0
    state: Optional[str] = None
    title: Optional[str] = None
    slug: Optional[str] = None
    category: Optional[str] = None
    text: Optional[str] = None
    formatted_text: Optional[str] = None
    vote_count: int = 0
    closed_at: Optional[datetime.datetime] = None
    status_key: Optional[str] = None
    status_hex_color: Optional[str] = None
    status_changed_by: Optional[UserVoiceUser] = None
    creator: Optional[UserVoiceUser] = None
    response: Optional[UserVoiceComment] = None
    created_at: datetime.datetime = datetime.datetime(1, 1, 1)
    updated_at: datetime.datetime = datetime.datetime(1, 1, 1)


# @Route("/posts/comment", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryPostComments(QueryDb[PostComment], IReturn[QueryResponse[PostComment]], IGet):
    id: Optional[int] = None
    user_id: Optional[int] = None
    post_id: Optional[int] = None
    content_contains: Optional[str] = None
    up_votes_above: Optional[int] = None
    up_votes_below: Optional[int] = None
    down_votes_above: Optional[int] = None
    down_votes: Optional[int] = None
    favorites_above: Optional[int] = None
    favorites_below: Optional[int] = None
    word_count_above: Optional[int] = None
    word_count_below: Optional[int] = None
    report_count_above: Optional[int] = None
    report_count_below: Optional[int] = None

