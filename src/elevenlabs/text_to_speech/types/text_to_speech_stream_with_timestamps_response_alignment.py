# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TextToSpeechStreamWithTimestampsResponseAlignment(UncheckedBaseModel):
    characters: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array of individual characters from the input text
    """

    character_start_times_seconds: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    Array of start times (in seconds) for each character
    """

    character_end_times_seconds: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    Array of end times (in seconds) for each character
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow