# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TxtExportOptions(UncheckedBaseModel):
    max_characters_per_line: typing.Optional[int] = None
    include_speakers: typing.Optional[bool] = None
    include_timestamps: typing.Optional[bool] = None
    segment_on_silence_longer_than_s: typing.Optional[float] = None
    max_segment_duration_s: typing.Optional[float] = None
    max_segment_chars: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
