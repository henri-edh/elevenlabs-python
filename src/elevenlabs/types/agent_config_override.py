# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .prompt_agent_override import PromptAgentOverride
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AgentConfigOverride(UncheckedBaseModel):
    prompt: typing.Optional[PromptAgentOverride] = pydantic.Field(default=None)
    """
    The overrides for the prompt configuration
    """

    first_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language of the agent, used for ASR and TTS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
