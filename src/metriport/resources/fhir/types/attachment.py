# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .base_64_binary import Base64Binary
from .code import Code
from .date_time import DateTime
from .unsigned_int import UnsignedInt
from .url import Url

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Attachment(pydantic.BaseModel):
    """
    For referring to data content defined in other formats.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    content_type: typing.Optional[Code] = pydantic.Field(
        alias="contentType",
        description="Identifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriate.",
    )
    language: typing.Optional[Code] = pydantic.Field(
        description="The human language of the content. The value can be any valid value according to BCP 47."
    )
    data: typing.Optional[Base64Binary] = pydantic.Field(
        description="The actual data of the attachment - a sequence of bytes, base64 encoded."
    )
    url: typing.Optional[Url] = pydantic.Field(description="A location where the data can be accessed.")
    size: typing.Optional[UnsignedInt] = pydantic.Field(
        description="The number of bytes of data that make up this attachment (before base64 encoding, if that is done)."
    )
    hash: typing.Optional[Base64Binary] = pydantic.Field(
        description="The calculated hash of the data using SHA-1. Represented using base64."
    )
    title: typing.Optional[str] = pydantic.Field(description="A label or set of text to display in place of the data.")
    creation: typing.Optional[DateTime] = pydantic.Field(description="The date that the attachment was first created.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}


from .extension import Extension  # noqa: E402

Attachment.update_forward_refs()
