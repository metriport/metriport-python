# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .decimal import Decimal
from .positive_int import PositiveInt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SampledData(pydantic.BaseModel):
    """
    A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    origin: Quantity = pydantic.Field(
        description="The base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement series."
    )
    period: typing.Optional[Decimal] = pydantic.Field(
        description="The length of time between sampling times, measured in milliseconds."
    )
    factor: typing.Optional[Decimal] = pydantic.Field(
        description="A correction factor that is applied to the sampled data points before they are added to the origin."
    )
    lower_limit: typing.Optional[Decimal] = pydantic.Field(
        alias="lowerLimit",
        description='The lower limit of detection of the measured points. This is needed if any of the data points have the value "L" (lower than detection limit).',
    )
    upper_limit: typing.Optional[Decimal] = pydantic.Field(
        alias="upperLimit",
        description='The upper limit of detection of the measured points. This is needed if any of the data points have the value "U" (higher than detection limit).',
    )
    dimensions: typing.Optional[PositiveInt] = pydantic.Field(
        description="The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at once."
    )
    data: typing.Optional[str] = pydantic.Field(
        description='A series of data points which are decimal values separated by a single space (character u20). The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can also be used in place of a decimal value.'
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}


from .extension import Extension  # noqa: E402
from .quantity import Quantity  # noqa: E402

SampledData.update_forward_refs()
