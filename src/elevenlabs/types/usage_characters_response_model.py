# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UsageCharactersResponseModel(UncheckedBaseModel):
    time: typing.List[int] = pydantic.Field()
    """
    The time axis with unix timestamps for each day.
    """

    usage: typing.Dict[str, typing.List[int]] = pydantic.Field()
    """
    The usage of each breakdown type along the time axis.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
