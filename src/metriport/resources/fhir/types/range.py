# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Range(pydantic.BaseModel):
    """
    A set of ordered Quantities defined by a low and high limit.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    low: typing.Optional[Quantity] = pydantic.Field(description="The low limit. The boundary is inclusive.")
    high: typing.Optional[Quantity] = pydantic.Field(description="The high limit. The boundary is inclusive.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}


from .extension import Extension  # noqa: E402
from .quantity import Quantity  # noqa: E402

Range.update_forward_refs()
