# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .code import Code
from .count_comparator import CountComparator
from .decimal import Decimal
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Count(pydantic.BaseModel):
    """
    A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    value: typing.Optional[Decimal] = pydantic.Field(
        description="The value of the measured amount. The value includes an implicit precision in the presentation of the value."
    )
    comparator: typing.Optional[CountComparator] = pydantic.Field(
        description='How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.'
    )
    unit: typing.Optional[str] = pydantic.Field(description="A human-readable form of the unit.")
    system: typing.Optional[Uri] = pydantic.Field(
        description="The identification of the system that provides the coded form of the unit."
    )
    code: typing.Optional[Code] = pydantic.Field(
        description="A computer processable form of the unit in some unit representation system."
    )

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

Count.update_forward_refs()
