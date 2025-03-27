# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .conversation_deletion_settings import ConversationDeletionSettings
from .conversation_history_feedback_common_model import (
    ConversationHistoryFeedbackCommonModel,
)
from .authorization_method import AuthorizationMethod
from .conversation_charging_common_model import ConversationChargingCommonModel
from .conversation_history_metadata_common_model_phone_call import (
    ConversationHistoryMetadataCommonModelPhoneCall,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ConversationHistoryMetadataCommonModel(UncheckedBaseModel):
    start_time_unix_secs: int
    call_duration_secs: int
    cost: typing.Optional[int] = None
    deletion_settings: typing.Optional[ConversationDeletionSettings] = None
    feedback: typing.Optional[ConversationHistoryFeedbackCommonModel] = None
    authorization_method: typing.Optional[AuthorizationMethod] = None
    charging: typing.Optional[ConversationChargingCommonModel] = None
    phone_call: typing.Optional[ConversationHistoryMetadataCommonModelPhoneCall] = None
    termination_reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
