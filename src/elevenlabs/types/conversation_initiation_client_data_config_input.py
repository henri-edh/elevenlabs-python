# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .conversation_config_client_override_config_input import (
    ConversationConfigClientOverrideConfigInput,
)
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ConversationInitiationClientDataConfigInput(UncheckedBaseModel):
    conversation_config_override: typing.Optional[ConversationConfigClientOverrideConfigInput] = pydantic.Field(
        default=None
    )
    """
    Overrides for the conversation configuration
    """

    custom_llm_extra_body: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to include custom LLM extra body
    """

    enable_conversation_initiation_client_data_from_webhook: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable conversation initiation client data from webhooks
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
