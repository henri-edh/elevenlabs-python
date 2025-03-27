# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
import typing_extensions
from ..core.unchecked_base_model import UnionMetadata


class WidgetConfigResponseModelAvatar_Orb(UncheckedBaseModel):
    """
    The avatar of the widget
    """

    type: typing.Literal["orb"] = "orb"
    color_1: typing.Optional[str] = None
    color_2: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WidgetConfigResponseModelAvatar_Url(UncheckedBaseModel):
    """
    The avatar of the widget
    """

    type: typing.Literal["url"] = "url"
    custom_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WidgetConfigResponseModelAvatar_Image(UncheckedBaseModel):
    """
    The avatar of the widget
    """

    type: typing.Literal["image"] = "image"
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


WidgetConfigResponseModelAvatar = typing_extensions.Annotated[
    typing.Union[
        WidgetConfigResponseModelAvatar_Orb,
        WidgetConfigResponseModelAvatar_Url,
        WidgetConfigResponseModelAvatar_Image,
    ],
    UnionMetadata(discriminant="type"),
]
