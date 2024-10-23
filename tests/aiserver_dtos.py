""" Options:
Date: 2024-10-23 07:43:31
Version: 8.41
Tip: To override a DTO option, remove "#" prefix before updating
BaseUrl: https://openai.servicestack.net

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


class AudioFormat(str, Enum):
    M_P3 = 'mp3'
    WAV = 'wav'
    FLAC = 'flac'
    OGG = 'ogg'


class IMediaTransform:
    ref_id: Optional[str] = None
    tag: Optional[str] = None


class IQueueMediaTransform:
    ref_id: Optional[str] = None
    tag: Optional[str] = None
    reply_to: Optional[str] = None


class IGeneration:
    ref_id: Optional[str] = None
    tag: Optional[str] = None


class IQueueGeneration:
    """
    Base class for queue generation requests
    """

    ref_id: Optional[str] = None
    reply_to: Optional[str] = None
    tag: Optional[str] = None
    state: Optional[str] = None


class ImageOutputFormat(str, Enum):
    JPG = 'jpg'
    PNG = 'png'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'
    WEBP = 'webp'


class WatermarkPosition(str, Enum):
    TOP_LEFT = 'TopLeft'
    TOP_RIGHT = 'TopRight'
    BOTTOM_LEFT = 'BottomLeft'
    BOTTOM_RIGHT = 'BottomRight'
    CENTER = 'Center'


class AiServiceProvider(str, Enum):
    REPLICATE = 'Replicate'
    COMFY = 'Comfy'
    OPEN_AI = 'OpenAi'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MediaType:
    id: Optional[str] = None
    api_base_url: Optional[str] = None
    api_key_header: Optional[str] = None
    website: Optional[str] = None
    icon: Optional[str] = None
    api_models: Optional[Dict[str, str]] = None
    provider: Optional[AiServiceProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MediaProvider:
    id: int = 0
    name: Optional[str] = None
    api_key_var: Optional[str] = None
    api_url_var: Optional[str] = None
    api_key: Optional[str] = None
    api_key_header: Optional[str] = None
    api_base_url: Optional[str] = None
    heartbeat_url: Optional[str] = None
    concurrency: int = 0
    priority: int = 0
    enabled: bool = False
    offline_date: Optional[datetime.datetime] = None
    created_date: datetime.datetime = datetime.datetime(1, 1, 1)
    media_type_id: Optional[str] = None
    # @Ignore()
    media_type: Optional[MediaType] = None

    models: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TextToSpeechVoice:
    id: Optional[str] = None
    model: Optional[str] = None


class ComfySampler(str, Enum):
    EULER = 'euler'
    EULER_CFG_PP = 'euler_cfg_pp'
    EULER_ANCESTRAL = 'euler_ancestral'
    EULER_ANCESTRAL_CFG_PP = 'euler_ancestral_cfg_pp'
    HUEN = 'huen'
    HUENPP2 = 'huenpp2'
    DPM_2 = 'dpm_2'
    DPM_2_ANCESTRAL = 'dpm_2_ancestral'
    LMS = 'lms'
    DPM_FAST = 'dpm_fast'
    DPM_ADAPTIVE = 'dpm_adaptive'
    DPMPP_2S_ANCESTRAL = 'dpmpp_2s_ancestral'
    DPMPP_SDE = 'dpmpp_sde'
    DPMPP_SDE_GPU = 'dpmpp_sde_gpu'
    DPMPP_2M = 'dpmpp_2m'
    DPMPP_2M_SDE = 'dpmpp_2m_sde'
    DPMPP_2M_SDE_GPU = 'dpmpp_2m_sde_gpu'
    DPMPP_3M_SDE = 'dpmpp_3m_sde'
    DPMPP_3M_SDE_GPU = 'dpmpp_3m_sde_gpu'
    DDPM = 'ddpm'
    LCM = 'lcm'
    DDIM = 'ddim'
    UNI_PC = 'uni_pc'
    UNI_PC_BH2 = 'uni_pc_bh2'


class AiTaskType(IntEnum):
    TEXT_TO_IMAGE = 1
    IMAGE_TO_IMAGE = 2
    IMAGE_UPSCALE = 3
    IMAGE_WITH_MASK = 4
    IMAGE_TO_TEXT = 5
    TEXT_TO_AUDIO = 6
    TEXT_TO_SPEECH = 7
    SPEECH_TO_TEXT = 8


class ComfyMaskSource(str, Enum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    ALPHA = 'alpha'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GenerationArgs:
    model: Optional[str] = None
    steps: Optional[int] = None
    batch_size: Optional[int] = None
    seed: Optional[int] = None
    positive_prompt: Optional[str] = None
    negative_prompt: Optional[str] = None
    image_input: Optional[bytes] = None
    mask_input: Optional[bytes] = None
    audio_input: Optional[bytes] = None
    sampler: Optional[ComfySampler] = None
    scheduler: Optional[str] = None
    cfg_scale: Optional[float] = None
    denoise: Optional[float] = None
    upscale_model: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    task_type: Optional[AiTaskType] = None
    clip: Optional[str] = None
    sample_length: Optional[float] = None
    mask_channel: Optional[ComfyMaskSource] = None
    aspect_ratio: Optional[str] = None
    quality: Optional[float] = None
    voice: Optional[str] = None
    language: Optional[str] = None


class ModelType(str, Enum):
    TEXT_TO_IMAGE = 'TextToImage'
    TEXT_ENCODER = 'TextEncoder'
    IMAGE_UPSCALE = 'ImageUpscale'
    TEXT_TO_SPEECH = 'TextToSpeech'
    TEXT_TO_AUDIO = 'TextToAudio'
    SPEECH_TO_TEXT = 'SpeechToText'
    IMAGE_TO_TEXT = 'ImageToText'
    IMAGE_TO_IMAGE = 'ImageToImage'
    IMAGE_WITH_MASK = 'ImageWithMask'
    VAE = 'VAE'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MediaModel:
    id: Optional[str] = None
    api_models: Optional[Dict[str, str]] = None
    url: Optional[str] = None
    quality: Optional[float] = None
    aspect_ratio: Optional[str] = None
    cfg_scale: Optional[float] = None
    scheduler: Optional[str] = None
    sampler: Optional[ComfySampler] = None
    width: Optional[int] = None
    height: Optional[int] = None
    steps: Optional[int] = None
    negative_prompt: Optional[str] = None
    model_type: Optional[ModelType] = None


class MediaTransformTaskType(str, Enum):
    IMAGE_SCALE = 'ImageScale'
    VIDEO_SCALE = 'VideoScale'
    IMAGE_CONVERT = 'ImageConvert'
    AUDIO_CONVERT = 'AudioConvert'
    VIDEO_CONVERT = 'VideoConvert'
    IMAGE_CROP = 'ImageCrop'
    VIDEO_CROP = 'VideoCrop'
    VIDEO_CUT = 'VideoCut'
    AUDIO_CUT = 'AudioCut'
    WATERMARK_IMAGE = 'WatermarkImage'
    WATERMARK_VIDEO = 'WatermarkVideo'


class MediaOutputFormat(str, Enum):
    M_P4 = 'mp4'
    AVI = 'avi'
    MKV = 'mkv'
    MOV = 'mov'
    WEB_M = 'webm'
    GIF = 'gif'
    M_P3 = 'mp3'
    WAV = 'wav'
    FLAC = 'flac'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MediaTransformArgs:
    task_type: Optional[MediaTransformTaskType] = None
    video_input: Optional[bytes] = None
    audio_input: Optional[bytes] = None
    image_input: Optional[bytes] = None
    watermark_input: Optional[bytes] = None
    video_file_name: Optional[str] = None
    audio_file_name: Optional[str] = None
    image_file_name: Optional[str] = None
    watermark_file_name: Optional[str] = None
    output_format: Optional[MediaOutputFormat] = None
    image_output_format: Optional[ImageOutputFormat] = None
    scale_width: Optional[int] = None
    scale_height: Optional[int] = None
    crop_x: Optional[int] = None
    crop_y: Optional[int] = None
    crop_width: Optional[int] = None
    crop_height: Optional[int] = None
    cut_start: Optional[float] = None
    cut_end: Optional[float] = None
    watermark_file: Optional[bytes] = None
    watermark_position: Optional[str] = None
    watermark_scale: Optional[str] = None
    audio_codec: Optional[str] = None
    video_codec: Optional[str] = None
    audio_bitrate: Optional[str] = None
    audio_sample_rate: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiModel:
    id: Optional[str] = None
    tags: Optional[List[str]] = None
    latest: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None


class AiProviderType(str, Enum):
    OPEN_AI_PROVIDER = 'OpenAiProvider'
    GOOGLE_AI_PROVIDER = 'GoogleAiProvider'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiType:
    id: Optional[str] = None
    provider: Optional[AiProviderType] = None
    website: Optional[str] = None
    api_base_url: Optional[str] = None
    heartbeat_url: Optional[str] = None
    icon: Optional[str] = None
    api_models: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiProviderModel:
    model: Optional[str] = None
    api_model: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiProvider:
    id: int = 0
    name: Optional[str] = None
    api_base_url: Optional[str] = None
    api_key_var: Optional[str] = None
    api_key: Optional[str] = None
    api_key_header: Optional[str] = None
    heartbeat_url: Optional[str] = None
    concurrency: int = 0
    priority: int = 0
    enabled: bool = False
    offline_date: Optional[datetime.datetime] = None
    created_date: datetime.datetime = datetime.datetime(1, 1, 1)
    models: Optional[List[AiProviderModel]] = None
    ai_type_id: Optional[str] = None
    # @Ignore()
    ai_type: Optional[AiType] = None

    # @Ignore()
    selected_models: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ToolCall:
    """
    The tool calls generated by the model, such as function calls.
    """

    id: Optional[str] = None
    """
    The ID of the tool call.
    """

    type: Optional[str] = None
    """
    The type of the tool. Currently, only `function` is supported.
    """

    function: Optional[str] = None
    """
    The function that the model called.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiMessage:
    """
    A list of messages comprising the conversation so far.
    """

    content: Optional[str] = None
    """
    The contents of the message.
    """

    role: Optional[str] = None
    """
    The role of the author of this message. Valid values are `system`, `user`, `assistant` and `tool`.
    """

    name: Optional[str] = None
    """
    An optional name for the participant. Provides the model information to differentiate between participants of the same role.
    """

    tool_calls: Optional[List[ToolCall]] = None
    """
    The tool calls generated by the model, such as function calls.
    """

    tool_call_id: Optional[str] = None
    """
    Tool call that this message is responding to.
    """


class ResponseFormat(str, Enum):
    TEXT = 'text'
    JSON_OBJECT = 'json_object'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiResponseFormat:
    type: Optional[ResponseFormat] = None
    """
    An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106.
    """


class OpenAiToolType(str, Enum):
    FUNCTION = 'function'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiTools:
    type: Optional[OpenAiToolType] = None
    """
    The type of the tool. Currently, only function is supported.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiChat:
    """
    Given a list of messages comprising a conversation, the model will return a response.
    """

    messages: Optional[List[OpenAiMessage]] = None
    """
    A list of messages comprising the conversation so far.
    """

    model: Optional[str] = None
    """
    ID of the model to use. See the model endpoint compatibility table for details on which models work with the Chat API
    """

    frequency_penalty: Optional[float] = None
    """
    Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    logit_bias: Optional[Dict[int, int]] = None
    """
    Modify the likelihood of specified tokens appearing in the completion.
    """

    log_probs: Optional[bool] = None
    """
    Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the content of message.
    """

    top_log_probs: Optional[int] = None
    """
    An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.
    """

    max_tokens: Optional[int] = None
    """
    The maximum number of tokens that can be generated in the chat completion.
    """

    n: Optional[int] = None
    """
    How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.
    """

    presence_penalty: Optional[float] = None
    """
    Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
    """

    response_format: Optional[OpenAiResponseFormat] = None
    """
    An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`. Setting Type to ResponseFormat.JsonObject enables JSON mode, which guarantees the message the model generates is valid JSON.
    """

    seed: Optional[int] = None
    """
    This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed, and you should refer to the system_fingerprint response parameter to monitor changes in the backend.
    """

    stop: Optional[List[str]] = None
    """
    Up to 4 sequences where the API will stop generating further tokens.
    """

    stream: Optional[bool] = None
    """
    If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a `data: [DONE]` message.
    """

    temperature: Optional[float] = None
    """
    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    """

    top_p: Optional[float] = None
    """
    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
    """

    tools: Optional[List[OpenAiTools]] = None
    """
    A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.
    """

    user: Optional[str] = None
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
    """


class TaskType(IntEnum):
    OPEN_AI_CHAT = 1
    COMFY = 2


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Prompt:
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None


class ConvertVideoOutputFormat(str, Enum):
    M_P4 = 'mp4'
    AVI = 'avi'
    MOV = 'mov'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PageStats:
    label: Optional[str] = None
    total: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArtifactOutput:
    """
    Output object for generated artifacts
    """

    # @ApiMember(Description="URL to access the generated image")
    url: Optional[str] = None
    """
    URL to access the generated image
    """


    # @ApiMember(Description="Filename of the generated image")
    file_name: Optional[str] = None
    """
    Filename of the generated image
    """


    # @ApiMember(Description="Provider used for image generation")
    provider: Optional[str] = None
    """
    Provider used for image generation
    """


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


class BackgroundJobState(str, Enum):
    QUEUED = 'Queued'
    STARTED = 'Started'
    EXECUTED = 'Executed'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    CANCELLED = 'Cancelled'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SummaryStats:
    name: Optional[str] = None
    total: int = 0
    total_prompt_tokens: int = 0
    total_completion_tokens: int = 0
    total_minutes: float = 0.0
    tokens_per_second: float = 0.0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiProviderTextOutput:
    text: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiProviderFileOutput:
    file_name: Optional[str] = None
    url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GenerationResult:
    text_outputs: Optional[List[AiProviderTextOutput]] = None
    outputs: Optional[List[AiProviderFileOutput]] = None
    error: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OllamaModelDetails:
    parent_model: Optional[str] = None
    format: Optional[str] = None
    family: Optional[str] = None
    families: Optional[List[str]] = None
    parameter_size: Optional[str] = None
    quantization_level: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OllamaModel:
    name: Optional[str] = None
    model: Optional[str] = None
    modified_at: datetime.datetime = datetime.datetime(1, 1, 1)
    size: int = 0
    digest: Optional[str] = None
    details: Optional[OllamaModelDetails] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChoiceMessage:
    content: Optional[str] = None
    """
    The contents of the message.
    """

    tool_calls: Optional[List[ToolCall]] = None
    """
    The tool calls generated by the model, such as function calls.
    """

    role: Optional[str] = None
    """
    The role of the author of this message.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Choice:
    finish_reason: Optional[str] = None
    """
    The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence, length if the maximum number of tokens specified in the request was reached, content_filter if content was omitted due to a flag from our content filters, tool_calls if the model called a tool
    """

    index: int = 0
    """
    The index of the choice in the list of choices.
    """

    message: Optional[ChoiceMessage] = None
    """
    A chat completion message generated by the model.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiUsage:
    """
    Usage statistics for the completion request.
    """

    completion_tokens: int = 0
    """
    Number of tokens in the generated completion.
    """

    prompt_tokens: int = 0
    """
    Number of tokens in the prompt.
    """

    total_tokens: int = 0
    """
    Total number of tokens used in the request (prompt + completion).
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdminDataResponse:
    page_stats: Optional[List[PageStats]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MediaTransformResponse:
    """
    Response object for transform requests
    """

    # @ApiMember(Description="List of generated outputs")
    outputs: Optional[List[ArtifactOutput]] = None
    """
    List of generated outputs
    """


    # @ApiMember(Description="List of generated text outputs")
    text_outputs: Optional[List[TextOutput]] = None
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
class QueueMediaTransformResponse:
    """
    Base class for queueable transformation requests
    """

    # @ApiMember(Description="Unique identifier of the background job")
    job_id: int = 0
    """
    Unique identifier of the background job
    """


    # @ApiMember(Description="Client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Client-provided identifier for the request
    """


    # @ApiMember(Description="Current state of the background job")
    job_state: Optional[BackgroundJobState] = None
    """
    Current state of the background job
    """


    # @ApiMember(Description="Current status of the transformation request")
    status: Optional[str] = None
    """
    Current status of the transformation request
    """


    # @ApiMember(Description="Detailed response status information")
    response_status: Optional[ResponseStatus] = None
    """
    Detailed response status information
    """


    # @ApiMember(Description="URL to check the status of the request")
    status_url: Optional[str] = None
    """
    URL to check the status of the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSummaryStatsResponse:
    provider_stats: Optional[List[SummaryStats]] = None
    model_stats: Optional[List[SummaryStats]] = None
    month_stats: Optional[List[SummaryStats]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComfyModelsResponse:
    results: Optional[List[str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComfyModelMappingsResponse:
    models: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetJobStatusResponse:
    # @ApiMember(Description="Unique identifier of the background job")
    job_id: int = 0
    """
    Unique identifier of the background job
    """


    # @ApiMember(Description="Client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Client-provided identifier for the request
    """


    # @ApiMember(Description="Current state of the background job")
    job_state: Optional[BackgroundJobState] = None
    """
    Current state of the background job
    """


    # @ApiMember(Description="Current status of the generation request")
    status: Optional[str] = None
    """
    Current status of the generation request
    """


    # @ApiMember(Description="List of generated outputs")
    outputs: Optional[List[ArtifactOutput]] = None
    """
    List of generated outputs
    """


    # @ApiMember(Description="List of generated text outputs")
    text_outputs: Optional[List[TextOutput]] = None
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
class GenerationResponse:
    """
    Response object for generation requests
    """

    # @ApiMember(Description="List of generated outputs")
    outputs: Optional[List[ArtifactOutput]] = None
    """
    List of generated outputs
    """


    # @ApiMember(Description="List of generated text outputs")
    text_outputs: Optional[List[TextOutput]] = None
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
class QueueGenerationResponse:
    # @ApiMember(Description="Unique identifier of the background job")
    job_id: int = 0
    """
    Unique identifier of the background job
    """


    # @ApiMember(Description="Client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Client-provided identifier for the request
    """


    # @ApiMember(Description="Current state of the background job")
    job_state: Optional[BackgroundJobState] = None
    """
    Current state of the background job
    """


    # @ApiMember(Description="Current status of the generation request")
    status: Optional[str] = None
    """
    Current status of the generation request
    """


    # @ApiMember(Description="Detailed response status information")
    response_status: Optional[ResponseStatus] = None
    """
    Detailed response status information
    """


    # @ApiMember(Description="URL to check the status of the generation request")
    status_url: Optional[str] = None
    """
    URL to check the status of the generation request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateGenerationResponse:
    id: int = 0
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetGenerationResponse:
    request: Optional[GenerationArgs] = None
    result: Optional[GenerationResult] = None
    outputs: Optional[List[AiProviderFileOutput]] = None
    text_outputs: Optional[List[AiProviderTextOutput]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTransformResponse:
    id: int = 0
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HelloResponse:
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOllamaModelsResponse:
    results: Optional[List[OllamaModel]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWorkerStatsResponse:
    results: Optional[List[WorkerStats]] = None
    queue_counts: Optional[Dict[str, int]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiChatResponse:
    id: Optional[str] = None
    """
    A unique identifier for the chat completion.
    """

    choices: Optional[List[Choice]] = None
    """
    A list of chat completion choices. Can be more than one if n is greater than 1.
    """

    created: int = 0
    """
    The Unix timestamp (in seconds) of when the chat completion was created.
    """

    model: Optional[str] = None
    """
    The model used for the chat completion.
    """

    system_fingerprint: Optional[str] = None
    """
    This fingerprint represents the backend configuration that the model runs with.
    """

    object: Optional[str] = None
    """
    The object type, which is always chat.completion.
    """

    usage: Optional[OpenAiUsage] = None
    """
    Usage statistics for the completion request.
    """

    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueOpenAiChatResponse:
    id: int = 0
    ref_id: Optional[str] = None
    status_url: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOpenAiChatResponse:
    result: Optional[BackgroundJobBase] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOpenAiChatStatusResponse:
    # @ApiMember(Description="Unique identifier of the background job")
    job_id: int = 0
    """
    Unique identifier of the background job
    """


    # @ApiMember(Description="Client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Client-provided identifier for the request
    """


    # @ApiMember(Description="Current state of the background job")
    job_state: Optional[BackgroundJobState] = None
    """
    Current state of the background job
    """


    # @ApiMember(Description="Current status of the generation request")
    status: Optional[str] = None
    """
    Current status of the generation request
    """


    # @ApiMember(Description="Detailed response status information")
    response_status: Optional[ResponseStatus] = None
    """
    Detailed response status information
    """


    # @ApiMember(Description="Chat response")
    chat_response: Optional[OpenAiChatResponse] = None
    """
    Chat response
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetActiveProvidersResponse:
    results: Optional[List[AiProvider]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateApiKeyResponse:
    id: int = 0
    key: Optional[str] = None
    name: Optional[str] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    visible_key: Optional[str] = None
    created_date: datetime.datetime = datetime.datetime(1, 1, 1)
    expiry_date: Optional[datetime.datetime] = None
    cancelled_date: Optional[datetime.datetime] = None
    notes: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFilesResponse:
    deleted: Optional[List[str]] = None
    missing: Optional[List[str]] = None
    failed: Optional[List[str]] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MigrateArtifactResponse:
    file_path: Optional[str] = None
    response_status: Optional[ResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdminData(IReturn[AdminDataResponse], IGet):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConvertAudio(IReturn[MediaTransformResponse], IMediaTransform):
    """
    Convert an audio file to a different format
    """

    # @ApiMember(Description="The desired output format for the converted audio")
    # @Required()
    output_format: Optional[AudioFormat] = None
    """
    The desired output format for the converted audio
    """


    # @Required()
    audio: Optional[bytes] = None

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
class QueueConvertAudio(IReturn[QueueMediaTransformResponse], IQueueMediaTransform):
    """
    Convert an audio file to a different format
    """

    # @ApiMember(Description="The desired output format for the converted audio")
    # @Required()
    output_format: Optional[AudioFormat] = None
    """
    The desired output format for the converted audio
    """


    # @Required()
    audio: Optional[bytes] = None

    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSummaryStats(IReturn[GetSummaryStatsResponse], IGet):
    from_: Optional[datetime.datetime] = field(metadata=config(field_name='from'), default=None)
    to: Optional[datetime.datetime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PopulateChatSummary(IReturn[StringsResponse], IGet):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComfyModels(IReturn[GetComfyModelsResponse]):
    api_base_url: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComfyModelMappings(IReturn[GetComfyModelMappingsResponse]):
    pass


# @Api(Description="Get job status")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetJobStatus(IReturn[GetJobStatusResponse], IGet):
    """
    Get job status
    """

    # @ApiMember(Description="Unique identifier of the background job")
    job_id: Optional[int] = None
    """
    Unique identifier of the background job
    """


    # @ApiMember(Description="Client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Client-provided identifier for the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActiveMediaModels(IReturn[StringsResponse], IGet):
    """
    Active Media Worker Models available in AI Server
    """

    pass


# @Api(Description="Generate image from text description")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TextToImage(IReturn[GenerationResponse], IGeneration):
    """
    Generate image from text description
    """

    # @ApiMember(Description="The main prompt describing the desired image")
    # @Validate(Validator="NotEmpty")
    positive_prompt: Optional[str] = None
    """
    The main prompt describing the desired image
    """


    # @ApiMember(Description="Optional prompt specifying what should not be in the image")
    negative_prompt: Optional[str] = None
    """
    Optional prompt specifying what should not be in the image
    """


    # @ApiMember(Description="Desired width of the generated image")
    width: Optional[int] = None
    """
    Desired width of the generated image
    """


    # @ApiMember(Description="Desired height of the generated image")
    height: Optional[int] = None
    """
    Desired height of the generated image
    """


    # @ApiMember(Description="Number of images to generate in a single batch")
    batch_size: Optional[int] = None
    """
    Number of images to generate in a single batch
    """


    # @ApiMember(Description="The AI model to use for image generation")
    model: Optional[str] = None
    """
    The AI model to use for image generation
    """


    # @ApiMember(Description="Optional seed for reproducible results")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results
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


# @Api(Description="Generate image from another image")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageToImage(IReturn[GenerationResponse], IGeneration):
    """
    Generate image from another image
    """

    # @ApiMember(Description="The image to use as input")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to use as input
    """


    # @ApiMember(Description="Prompt describing the desired output")
    # @Validate(Validator="NotEmpty")
    positive_prompt: Optional[str] = None
    """
    Prompt describing the desired output
    """


    # @ApiMember(Description="Negative prompt describing what should not be in the image")
    negative_prompt: Optional[str] = None
    """
    Negative prompt describing what should not be in the image
    """


    # @ApiMember(Description="The AI model to use for image generation")
    model: Optional[str] = None
    """
    The AI model to use for image generation
    """


    # @ApiMember(Description="Optional specific amount of denoise to apply")
    denoise: Optional[float] = None
    """
    Optional specific amount of denoise to apply
    """


    # @ApiMember(Description="Number of images to generate in a single batch")
    batch_size: Optional[int] = None
    """
    Number of images to generate in a single batch
    """


    # @ApiMember(Description="Optional seed for reproducible results in image generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in image generation
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


# @Api(Description="Upscale an image")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageUpscale(IReturn[GenerationResponse], IGeneration):
    """
    Upscale an image
    """

    # @ApiMember(Description="The image to upscale")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to upscale
    """


    # @ApiMember(Description="Optional seed for reproducible results in image generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in image generation
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


# @Api(Description="Generate image with masked area")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageWithMask(IReturn[GenerationResponse], IGeneration):
    """
    Generate image with masked area
    """

    # @ApiMember(Description="Prompt describing the desired output in the masked area")
    # @Validate(Validator="NotEmpty")
    positive_prompt: Optional[str] = None
    """
    Prompt describing the desired output in the masked area
    """


    # @ApiMember(Description="Negative prompt describing what should not be in the masked area")
    negative_prompt: Optional[str] = None
    """
    Negative prompt describing what should not be in the masked area
    """


    # @ApiMember(Description="The image to use as input")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to use as input
    """


    # @ApiMember(Description="The mask to use as input")
    # @Required()
    mask: Optional[bytes] = None
    """
    The mask to use as input
    """


    # @ApiMember(Description="Optional specific amount of denoise to apply")
    denoise: Optional[float] = None
    """
    Optional specific amount of denoise to apply
    """


    # @ApiMember(Description="Optional seed for reproducible results in image generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in image generation
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


# @Api(Description="Convert image to text")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImageToText(IReturn[GenerationResponse], IGeneration):
    """
    Convert image to text
    """

    # @ApiMember(Description="The image to convert to text")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to convert to text
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


# @Api(Description="Generate image from text description")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueTextToImage(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Generate image from text description
    """

    # @ApiMember(Description="The main prompt describing the desired image")
    # @Validate(Validator="NotEmpty")
    positive_prompt: Optional[str] = None
    """
    The main prompt describing the desired image
    """


    # @ApiMember(Description="Optional prompt specifying what should not be in the image")
    negative_prompt: Optional[str] = None
    """
    Optional prompt specifying what should not be in the image
    """


    # @ApiMember(Description="Desired width of the generated image")
    width: Optional[int] = None
    """
    Desired width of the generated image
    """


    # @ApiMember(Description="Desired height of the generated image")
    height: Optional[int] = None
    """
    Desired height of the generated image
    """


    # @ApiMember(Description="Number of images to generate in a single batch")
    batch_size: Optional[int] = None
    """
    Number of images to generate in a single batch
    """


    # @ApiMember(Description="The AI model to use for image generation")
    model: Optional[str] = None
    """
    The AI model to use for image generation
    """


    # @ApiMember(Description="Optional seed for reproducible results")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


# @Api(Description="Upscale an image")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueImageUpscale(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Upscale an image
    """

    # @ApiMember(Description="The image to upscale")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to upscale
    """


    # @ApiMember(Description="Optional seed for reproducible results in image generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in image generation
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


# @Api(Description="Generate image from another image")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueImageToImage(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Generate image from another image
    """

    # @ApiMember(Description="The image to use as input")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to use as input
    """


    # @ApiMember(Description="Prompt describing the desired output")
    # @Validate(Validator="NotEmpty")
    positive_prompt: Optional[str] = None
    """
    Prompt describing the desired output
    """


    # @ApiMember(Description="Negative prompt describing what should not be in the image")
    negative_prompt: Optional[str] = None
    """
    Negative prompt describing what should not be in the image
    """


    # @ApiMember(Description="The AI model to use for image generation")
    model: Optional[str] = None
    """
    The AI model to use for image generation
    """


    # @ApiMember(Description="Optional specific amount of denoise to apply")
    denoise: Optional[float] = None
    """
    Optional specific amount of denoise to apply
    """


    # @ApiMember(Description="Number of images to generate in a single batch")
    batch_size: Optional[int] = None
    """
    Number of images to generate in a single batch
    """


    # @ApiMember(Description="Optional seed for reproducible results in image generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in image generation
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


# @Api(Description="Generate image with masked area")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueImageWithMask(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Generate image with masked area
    """

    # @ApiMember(Description="Prompt describing the desired output in the masked area")
    # @Validate(Validator="NotEmpty")
    positive_prompt: Optional[str] = None
    """
    Prompt describing the desired output in the masked area
    """


    # @ApiMember(Description="Negative prompt describing what should not be in the masked area")
    negative_prompt: Optional[str] = None
    """
    Negative prompt describing what should not be in the masked area
    """


    # @ApiMember(Description="The image to use as input")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to use as input
    """


    # @ApiMember(Description="The mask to use as input")
    # @Required()
    mask: Optional[bytes] = None
    """
    The mask to use as input
    """


    # @ApiMember(Description="Optional specific amount of denoise to apply")
    denoise: Optional[float] = None
    """
    Optional specific amount of denoise to apply
    """


    # @ApiMember(Description="Optional seed for reproducible results in image generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in image generation
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


# @Api(Description="Convert image to text")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueImageToText(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Convert image to text
    """

    # @ApiMember(Description="The image to convert to text")
    # @Required()
    image: Optional[bytes] = None
    """
    The image to convert to text
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConvertImage(IReturn[MediaTransformResponse], IMediaTransform, IPost):
    """
    Convert an image to a different format
    """

    # @ApiMember(Description="The image file to be converted")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be converted
    """


    # @ApiMember(Description="The desired output format for the converted image")
    # @Required()
    output_format: Optional[ImageOutputFormat] = None
    """
    The desired output format for the converted image
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
class CropImage(IReturn[MediaTransformResponse], IMediaTransform, IPost):
    """
    Crop an image to a specified area
    """

    # @ApiMember(Description="The X-coordinate of the top-left corner of the crop area")
    x: int = 0
    """
    The X-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The Y-coordinate of the top-left corner of the crop area")
    y: int = 0
    """
    The Y-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The width of the crop area")
    width: int = 0
    """
    The width of the crop area
    """


    # @ApiMember(Description="The height of the crop area")
    height: int = 0
    """
    The height of the crop area
    """


    # @ApiMember(Description="The image file to be cropped")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be cropped
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
class WatermarkImage(IReturn[MediaTransformResponse], IMediaTransform, IPost):
    """
    Add a watermark to an image
    """

    # @ApiMember(Description="The image file to be watermarked")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be watermarked
    """


    # @ApiMember(Description="The position of the watermark on the image")
    position: Optional[WatermarkPosition] = None
    """
    The position of the watermark on the image
    """


    # @ApiMember(Description="Scale of the watermark relative")
    watermark_scale: float = 0.0
    """
    Scale of the watermark relative
    """


    # @ApiMember(Description="The opacity of the watermark (0.0 to 1.0)")
    opacity: float = 0.0
    """
    The opacity of the watermark (0.0 to 1.0)
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
class ScaleImage(IReturn[MediaTransformResponse], IMediaTransform, IPost):
    """
    Scale an image to a specified size
    """

    # @ApiMember(Description="The image file to be scaled")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be scaled
    """


    # @ApiMember(Description="Desired width of the scaled image")
    width: Optional[int] = None
    """
    Desired width of the scaled image
    """


    # @ApiMember(Description="Desired height of the scaled image")
    height: Optional[int] = None
    """
    Desired height of the scaled image
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
class QueueCropImage(IReturn[QueueMediaTransformResponse], IQueueMediaTransform, IPost):
    """
    Crop an image to a specified area
    """

    # @ApiMember(Description="The X-coordinate of the top-left corner of the crop area")
    x: int = 0
    """
    The X-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The Y-coordinate of the top-left corner of the crop area")
    y: int = 0
    """
    The Y-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The width of the crop area")
    width: int = 0
    """
    The width of the crop area
    """


    # @ApiMember(Description="The height of the crop area")
    height: int = 0
    """
    The height of the crop area
    """


    # @ApiMember(Description="The image file to be cropped")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be cropped
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueScaleImage(IReturn[MediaTransformResponse], IQueueMediaTransform, IPost):
    """
    Scale an image to a specified size
    """

    # @ApiMember(Description="The image file to be scaled")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be scaled
    """


    # @ApiMember(Description="Desired width of the scaled image")
    width: Optional[int] = None
    """
    Desired width of the scaled image
    """


    # @ApiMember(Description="Desired height of the scaled image")
    height: Optional[int] = None
    """
    Desired height of the scaled image
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueWatermarkImage(IReturn[QueueMediaTransformResponse], IQueueMediaTransform, IPost):
    """
    Add a watermark to an image
    """

    # @ApiMember(Description="The image file to be watermarked")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be watermarked
    """


    # @ApiMember(Description="The position of the watermark on the image")
    position: Optional[WatermarkPosition] = None
    """
    The position of the watermark on the image
    """


    # @ApiMember(Description="The opacity of the watermark (0.0 to 1.0)")
    opacity: float = 0.0
    """
    The opacity of the watermark (0.0 to 1.0)
    """


    # @ApiMember(Description="Scale of the watermark relative")
    watermark_scale: float = 0.0
    """
    Scale of the watermark relative
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueConvertImage(IReturn[QueueMediaTransformResponse], IQueueMediaTransform, IPost):
    """
    Convert an image to a different format
    """

    # @ApiMember(Description="The image file to be converted")
    # @Required()
    image: Optional[bytes] = None
    """
    The image file to be converted
    """


    # @ApiMember(Description="The desired output format for the converted image")
    # @Required()
    output_format: Optional[ImageOutputFormat] = None
    """
    The desired output format for the converted image
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryMediaTypes(QueryDb[MediaType], IReturn[QueryResponse[MediaType]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryMediaProviders(QueryDb[MediaProvider], IReturn[QueryResponse[MediaProvider]]):
    """
    Media Providers
    """

    id: Optional[int] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryTextToSpeechVoices(QueryDb[TextToSpeechVoice], IReturn[QueryResponse[TextToSpeechVoice]]):
    """
    Text to Speech Voice models
    """

    pass


# @Route("/generate", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateGeneration(IReturn[CreateGenerationResponse]):
    # @Validate(Validator="NotNull")
    request: Optional[GenerationArgs] = None

    provider: Optional[str] = None
    state: Optional[str] = None
    reply_to: Optional[str] = None
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryMediaModels(QueryDb[MediaModel], IReturn[QueryResponse[MediaModel]]):
    """
    Media Models
    """

    id: Optional[str] = None


# @Route("/generation/{Id}", "GET")
# @Route("/generation/ref/{RefId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetGeneration(IReturn[GetGenerationResponse]):
    id: Optional[int] = None
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateMediaProvider(IReturn[IdResponse], IPatchDb[MediaProvider]):
    """
    Update a Generation API Provider
    """

    id: int = 0
    api_key: Optional[str] = None
    """
    The API Key to use for this Provider
    """

    api_key_header: Optional[str] = None
    """
    Send the API Key in the Header instead of Authorization Bearer
    """

    api_base_url: Optional[str] = None
    """
    Override Base URL for the Generation Provider
    """

    heartbeat_url: Optional[str] = None
    """
    Url to check if the API is online
    """

    concurrency: Optional[int] = None
    """
    How many requests should be made concurrently
    """

    priority: Optional[int] = None
    """
    What priority to give this Provider to use for processing models
    """

    enabled: Optional[bool] = None
    """
    Whether the Provider is enabled
    """

    models: Optional[List[str]] = None
    """
    The models this API Provider should process
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateMediaProvider(IReturn[IdResponse], ICreateDb[MediaProvider]):
    """
    Add an API Provider to Generation API Providers
    """

    name: Optional[str] = None
    """
    The name of the API Provider
    """

    api_key: Optional[str] = None
    """
    The API Key to use for this Provider
    """

    api_key_header: Optional[str] = None
    """
    Send the API Key in the Header instead of Authorization Bearer
    """

    api_base_url: Optional[str] = None
    """
    Base URL for the Generation Provider
    """

    heartbeat_url: Optional[str] = None
    """
    Url to check if the API is online
    """

    concurrency: int = 0
    """
    How many requests should be made concurrently
    """

    priority: int = 0
    """
    What priority to give this Provider to use for processing models
    """

    enabled: bool = False
    """
    Whether the Provider is enabled
    """

    offline_date: Optional[datetime.datetime] = None
    """
    The date the Provider was last online
    """

    models: Optional[List[str]] = None
    """
    Models this API Provider should process
    """

    media_type_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateMediaTransform(IReturn[CreateTransformResponse]):
    # @Validate(Validator="NotNull")
    request: Optional[MediaTransformArgs] = None

    provider: Optional[str] = None
    state: Optional[str] = None
    reply_to: Optional[str] = None
    ref_id: Optional[str] = None


# @Route("/hello/{Name}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Hello(IReturn[HelloResponse], IGet):
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOllamaModels(IReturn[GetOllamaModelsResponse], IGet):
    # @Validate(Validator="NotEmpty")
    api_base_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryAiModels(QueryDb[AiModel], IReturn[QueryResponse[AiModel]]):
    """
    Different Models available in AI Server
    """

    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryAiTypes(QueryDb[AiType], IReturn[QueryResponse[AiType]]):
    """
    The Type and behavior of different API Providers
    """

    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActiveAiModels(IReturn[StringsResponse], IGet):
    """
    Active AI Worker Models available in AI Server
    """

    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryAiProviders(QueryDb[AiProvider], IReturn[QueryResponse[AiProvider]]):
    """
    AI Providers
    """

    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWorkerStats(IReturn[GetWorkerStatsResponse], IGet):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CancelWorker(IReturn[EmptyResponse]):
    # @Validate(Validator="NotEmpty")
    worker: Optional[str] = None


# @Route("/icons/models/{Model}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetModelImage(IReturn[bytes], IGet):
    model: Optional[str] = None


# @Route("/v1/chat/completions", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiChatCompletion(OpenAiChat, IReturn[OpenAiChatResponse], IPost):
    """
    Given a list of messages comprising a conversation, the model will return a response.
    """

    ref_id: Optional[str] = None
    """
    Provide a unique identifier to track requests
    """

    provider: Optional[str] = None
    """
    Specify which AI Provider to use
    """

    tag: Optional[str] = None
    """
    Categorize like requests under a common group
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueOpenAiChatCompletion(IReturn[QueueOpenAiChatResponse]):
    ref_id: Optional[str] = None
    provider: Optional[str] = None
    reply_to: Optional[str] = None
    tag: Optional[str] = None
    request: Optional[OpenAiChat] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WaitForOpenAiChat(IReturn[GetOpenAiChatResponse], IGet):
    id: Optional[int] = None
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOpenAiChat(IReturn[GetOpenAiChatResponse], IGet):
    id: Optional[int] = None
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetOpenAiChatStatus(IReturn[GetOpenAiChatStatusResponse], IGet):
    job_id: int = 0
    ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetActiveProviders(IReturn[GetActiveProvidersResponse], IGet):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatAiProvider(IReturn[OpenAiChatResponse], IPost):
    provider: Optional[str] = None
    model: Optional[str] = None
    request: Optional[OpenAiChat] = None
    prompt: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateApiKey(IReturn[CreateApiKeyResponse], IPost):
    key: Optional[str] = None
    name: Optional[str] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    scopes: Optional[List[str]] = None
    notes: Optional[str] = None
    ref_id: Optional[int] = None
    ref_id_str: Optional[str] = None
    meta: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAiProvider(IReturn[IdResponse], ICreateDb[AiProvider]):
    """
    Add an AI Provider to process AI Requests
    """

    # @Validate(Validator="GreaterThan(0)")
    ai_type_id: Optional[str] = None
    """
    The Type of this API Provider
    """


    api_base_url: Optional[str] = None
    """
    The Base URL for the API Provider
    """

    # @Validate(Validator="NotEmpty")
    name: Optional[str] = None
    """
    The unique name for this API Provider
    """


    api_key_var: Optional[str] = None
    """
    The API Key to use for this Provider
    """

    api_key: Optional[str] = None
    """
    The API Key to use for this Provider
    """

    api_key_header: Optional[str] = None
    """
    Send the API Key in the Header instead of Authorization Bearer
    """

    heartbeat_url: Optional[str] = None
    """
    The URL to check if the API Provider is still online
    """

    task_paths: Optional[Dict[str, str]] = None
    """
    Override API Paths for different AI Requests
    """

    concurrency: int = 0
    """
    How many requests should be made concurrently
    """

    priority: int = 0
    """
    What priority to give this Provider to use for processing models
    """

    enabled: bool = False
    """
    Whether the Provider is enabled
    """

    models: Optional[List[AiProviderModel]] = None
    """
    The models this API Provider should process
    """

    selected_models: Optional[List[str]] = None
    """
    The selected models this API Provider should process
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAiProvider(IReturn[IdResponse], IPatchDb[AiProvider]):
    id: int = 0
    ai_type_id: Optional[str] = None
    """
    The Type of this API Provider
    """

    api_base_url: Optional[str] = None
    """
    The Base URL for the API Provider
    """

    name: Optional[str] = None
    """
    The unique name for this API Provider
    """

    api_key_var: Optional[str] = None
    """
    The API Key to use for this Provider
    """

    api_key: Optional[str] = None
    """
    The API Key to use for this Provider
    """

    api_key_header: Optional[str] = None
    """
    Send the API Key in the Header instead of Authorization Bearer
    """

    heartbeat_url: Optional[str] = None
    """
    The URL to check if the API Provider is still online
    """

    task_paths: Optional[Dict[str, str]] = None
    """
    Override API Paths for different AI Requests
    """

    concurrency: Optional[int] = None
    """
    How many requests should be made concurrently
    """

    priority: Optional[int] = None
    """
    What priority to give this Provider to use for processing models
    """

    enabled: Optional[bool] = None
    """
    Whether the Provider is enabled
    """

    models: Optional[List[AiProviderModel]] = None
    """
    The models this API Provider should process
    """

    selected_models: Optional[List[str]] = None
    """
    The selected models this API Provider should process
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteAiProvider(IReturnVoid, IDeleteDb[AiProvider]):
    """
    Delete API Provider
    """

    id: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryPrompts(QueryData[Prompt], IReturn[QueryResponse[Prompt]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Reload(IReturn[EmptyResponse], IPost):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChangeAiProviderStatus(IReturn[StringResponse], IPost):
    provider: Optional[str] = None
    online: bool = False


# @Api(Description="Convert text to speech")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueTextToSpeech(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Convert text to speech
    """

    # @ApiMember(Description="The text to be converted to speech")
    # @Required()
    text: Optional[str] = None
    """
    The text to be converted to speech
    """


    # @ApiMember(Description="Optional seed for reproducible results in speech generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in speech generation
    """


    # @ApiMember(Description="The AI model to use for speech generation")
    model: Optional[str] = None
    """
    The AI model to use for speech generation
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


# @Api(Description="Convert speech to text")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueSpeechToText(IReturn[QueueGenerationResponse], IQueueGeneration):
    """
    Convert speech to text
    """

    # @ApiMember(Description="The audio stream containing the speech to be transcribed")
    # @Required()
    audio: Optional[bytes] = None
    """
    The audio stream containing the speech to be transcribed
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


    # @ApiMember(Description="Optional state to associate with the request")
    state: Optional[str] = None
    """
    Optional state to associate with the request
    """


# @Api(Description="Convert text to speech")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TextToSpeech(IReturn[GenerationResponse], IGeneration):
    """
    Convert text to speech
    """

    # @ApiMember(Description="The text to be converted to speech")
    # @Validate(Validator="NotEmpty")
    input: Optional[str] = None
    """
    The text to be converted to speech
    """


    # @ApiMember(Description="Optional specific model and voice to use for speech generation")
    model: Optional[str] = None
    """
    Optional specific model and voice to use for speech generation
    """


    # @ApiMember(Description="Optional seed for reproducible results in speech generation")
    seed: Optional[int] = None
    """
    Optional seed for reproducible results in speech generation
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


# @Api(Description="Convert speech to text")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SpeechToText(IReturn[GenerationResponse], IGeneration):
    """
    Convert speech to text
    """

    # @ApiMember(Description="The audio stream containing the speech to be transcribed")
    # @Required()
    audio: Optional[bytes] = None
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


# @Api(Description="Scale video")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ScaleVideo(IReturn[MediaTransformResponse], IMediaTransform):
    """
    Scale video
    """

    # @ApiMember(Description="The video file to be scaled")
    # @Required()
    video: Optional[bytes] = None
    """
    The video file to be scaled
    """


    # @ApiMember(Description="Desired width of the scaled video")
    width: Optional[int] = None
    """
    Desired width of the scaled video
    """


    # @ApiMember(Description="Desired height of the scaled video")
    height: Optional[int] = None
    """
    Desired height of the scaled video
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


# @Api(Description="Watermark video")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WatermarkVideo(IReturn[MediaTransformResponse], IMediaTransform):
    """
    Watermark video
    """

    # @ApiMember(Description="The video file to be watermarked")
    # @Required()
    video: Optional[bytes] = None
    """
    The video file to be watermarked
    """


    # @ApiMember(Description="The image file to use as a watermark")
    # @Required()
    watermark: Optional[bytes] = None
    """
    The image file to use as a watermark
    """


    # @ApiMember(Description="Position of the watermark")
    position: Optional[WatermarkPosition] = None
    """
    Position of the watermark
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
class ConvertVideo(IReturn[MediaTransformResponse], IMediaTransform):
    """
    Convert a video to a different format
    """

    # @ApiMember(Description="The desired output format for the converted video")
    # @Required()
    output_format: Optional[ConvertVideoOutputFormat] = None
    """
    The desired output format for the converted video
    """


    # @Required()
    video: Optional[bytes] = None

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
class CropVideo(IReturn[MediaTransformResponse], IMediaTransform):
    """
    Crop a video to a specified area
    """

    # @ApiMember(Description="The X-coordinate of the top-left corner of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    x: int = 0
    """
    The X-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The Y-coordinate of the top-left corner of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    y: int = 0
    """
    The Y-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The width of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    width: int = 0
    """
    The width of the crop area
    """


    # @ApiMember(Description="The height of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    height: int = 0
    """
    The height of the crop area
    """


    # @Required()
    video: Optional[bytes] = None

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
class TrimVideo(IReturn[MediaTransformResponse], IMediaTransform):
    """
    Trim a video to a specified duration via start and end times
    """

    # @ApiMember(Description="The start time of the trimmed video (format: MM:SS)")
    # @Required()
    start_time: Optional[str] = None
    """
    The start time of the trimmed video (format: MM:SS)
    """


    # @ApiMember(Description="The end time of the trimmed video (format: MM:SS)")
    end_time: Optional[str] = None
    """
    The end time of the trimmed video (format: MM:SS)
    """


    # @Required()
    video: Optional[bytes] = None

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


# @Api(Description="Scale video")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueScaleVideo(IReturn[QueueMediaTransformResponse], IQueueMediaTransform):
    """
    Scale video
    """

    # @ApiMember(Description="The video file to be scaled")
    # @Required()
    video: Optional[bytes] = None
    """
    The video file to be scaled
    """


    # @ApiMember(Description="Desired width of the scaled video")
    width: Optional[int] = None
    """
    Desired width of the scaled video
    """


    # @ApiMember(Description="Desired height of the scaled video")
    height: Optional[int] = None
    """
    Desired height of the scaled video
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


# @Api(Description="Watermark video")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueWatermarkVideo(IReturn[QueueMediaTransformResponse], IQueueMediaTransform):
    """
    Watermark video
    """

    # @ApiMember(Description="The video file to be watermarked")
    # @Required()
    video: Optional[bytes] = None
    """
    The video file to be watermarked
    """


    # @ApiMember(Description="The image file to use as a watermark")
    # @Required()
    watermark: Optional[bytes] = None
    """
    The image file to use as a watermark
    """


    # @ApiMember(Description="Position of the watermark")
    position: Optional[WatermarkPosition] = None
    """
    Position of the watermark
    """


    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueConvertVideo(IReturn[QueueMediaTransformResponse], IQueueMediaTransform):
    """
    Convert a video to a different format
    """

    # @ApiMember(Description="The desired output format for the converted video")
    # @Required()
    output_format: Optional[ConvertVideoOutputFormat] = None
    """
    The desired output format for the converted video
    """


    # @Required()
    video: Optional[bytes] = None

    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueCropVideo(IReturn[QueueMediaTransformResponse], IQueueMediaTransform):
    """
    Crop a video to a specified area
    """

    # @ApiMember(Description="The X-coordinate of the top-left corner of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    x: int = 0
    """
    The X-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The Y-coordinate of the top-left corner of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    y: int = 0
    """
    The Y-coordinate of the top-left corner of the crop area
    """


    # @ApiMember(Description="The width of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    width: int = 0
    """
    The width of the crop area
    """


    # @ApiMember(Description="The height of the crop area")
    # @Validate(Validator="GreaterThan(0)")
    # @Required()
    height: int = 0
    """
    The height of the crop area
    """


    # @Required()
    video: Optional[bytes] = None

    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueueTrimVideo(IReturn[QueueMediaTransformResponse], IQueueMediaTransform):
    """
    Trim a video to a specified duration via start and end times
    """

    # @ApiMember(Description="The start time of the trimmed video (format: HH:MM:SS)")
    # @Required()
    start_time: Optional[str] = None
    """
    The start time of the trimmed video (format: HH:MM:SS)
    """


    # @ApiMember(Description="The end time of the trimmed video (format: HH:MM:SS)")
    end_time: Optional[str] = None
    """
    The end time of the trimmed video (format: HH:MM:SS)
    """


    # @Required()
    video: Optional[bytes] = None

    # @ApiMember(Description="Optional client-provided identifier for the request")
    ref_id: Optional[str] = None
    """
    Optional client-provided identifier for the request
    """


    # @ApiMember(Description="Optional queue or topic to reply to")
    reply_to: Optional[str] = None
    """
    Optional queue or topic to reply to
    """


    # @ApiMember(Description="Tag to identify the request")
    tag: Optional[str] = None
    """
    Tag to identify the request
    """


# @Route("/artifacts/{**Path}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetArtifact(IReturn[bytes], IGet):
    # @Validate(Validator="NotEmpty")
    path: Optional[str] = None

    download: Optional[bool] = None


# @Route("/files/{**Path}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFile(IReturn[EmptyResponse], IDelete):
    # @Validate(Validator="NotEmpty")
    path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFiles(IReturn[DeleteFilesResponse], IPost):
    paths: Optional[List[str]] = None


# @Route("/variants/{Variant}/{**Path}")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetVariant(IReturn[bytes], IGet):
    # @Validate(Validator="NotEmpty")
    variant: Optional[str] = None

    # @Validate(Validator="NotEmpty")
    path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MigrateArtifact(IReturn[MigrateArtifactResponse], IPost):
    path: Optional[str] = None
    date: Optional[datetime.datetime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryMediaTypesData(QueryData[MediaType], IReturn[QueryResponse[MediaType]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryTextToSpeechVoicesData(QueryData[TextToSpeechVoice], IReturn[QueryResponse[TextToSpeechVoice]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryAiModelsData(QueryData[AiModel], IReturn[QueryResponse[AiModel]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryAiTypesData(QueryData[AiType], IReturn[QueryResponse[AiType]]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMediaProvider(IReturn[IdResponse], IDeleteDb[MediaProvider]):
    """
    Delete a Generation API Provider
    """

    id: Optional[int] = None
    name: Optional[str] = None

