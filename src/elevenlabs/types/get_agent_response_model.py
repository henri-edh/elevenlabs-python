# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
from .array_json_schema_property import ArrayJsonSchemaProperty
from .object_json_schema_property import ObjectJsonSchemaProperty
from .conversational_config import ConversationalConfig
from .agent_metadata_response_model import AgentMetadataResponseModel
import typing
from .agent_platform_settings import AgentPlatformSettings
from .conv_ai_stored_secret_config import ConvAiStoredSecretConfig
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class GetAgentResponseModel(UncheckedBaseModel):
    agent_id: str
    name: str
    conversation_config: ConversationalConfig
    metadata: AgentMetadataResponseModel
    platform_settings: typing.Optional[AgentPlatformSettings] = None
    secrets: typing.List[ConvAiStoredSecretConfig]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ArrayJsonSchemaProperty, GetAgentResponseModel=GetAgentResponseModel)
update_forward_refs(ObjectJsonSchemaProperty, GetAgentResponseModel=GetAgentResponseModel)
