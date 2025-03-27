# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .knowledge_base_document_metadata_response_model import (
    KnowledgeBaseDocumentMetadataResponseModel,
)
from .resource_access_info import ResourceAccessInfo
import typing
from .get_knowledge_base_summary_url_response_model_dependent_agents_item import (
    GetKnowledgeBaseSummaryUrlResponseModelDependentAgentsItem,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GetKnowledgeBaseSummaryUrlResponseModel(UncheckedBaseModel):
    id: str
    name: str
    metadata: KnowledgeBaseDocumentMetadataResponseModel
    prompt_injectable: bool
    access_info: ResourceAccessInfo
    dependent_agents: typing.List[GetKnowledgeBaseSummaryUrlResponseModelDependentAgentsItem]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
