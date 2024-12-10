# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
from .array_json_schema_property import ArrayJsonSchemaProperty
from .object_json_schema_property import ObjectJsonSchemaProperty
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class ClientToolConfig(UncheckedBaseModel):
    """
    A client tool is one that sends an event to the user's client to trigger something client side
    """

    name: str
    description: str
    parameters: typing.Optional[ObjectJsonSchemaProperty] = None
    expects_response: typing.Optional[bool] = None
    response_timeout_secs: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ArrayJsonSchemaProperty, ClientToolConfig=ClientToolConfig)
update_forward_refs(ObjectJsonSchemaProperty, ClientToolConfig=ClientToolConfig)