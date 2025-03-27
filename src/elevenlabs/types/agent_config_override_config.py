# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .prompt_agent_override_config import PromptAgentOverrideConfig
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AgentConfigOverrideConfig(UncheckedBaseModel):
    prompt: typing.Optional[PromptAgentOverrideConfig] = pydantic.Field(default=None)
    """
    Overrides for the prompt configuration
    """

    first_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to allow overriding the first message
    """

    language: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to allow overriding the language
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
