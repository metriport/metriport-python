# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .code import Code
from .decimal import Decimal
from .positive_int import PositiveInt
from .time import Time
from .timing_repeat_duration_unit import TimingRepeatDurationUnit
from .timing_repeat_period_unit import TimingRepeatPeriodUnit
from .timing_repeat_when_item import TimingRepeatWhenItem
from .unsigned_int import UnsignedInt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TimingRepeat(pydantic.BaseModel):
    """
    Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    bounds_duration: typing.Optional[Duration] = pydantic.Field(
        alias="boundsDuration",
        default=None,
        description="Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.",
    )
    bounds_range: typing.Optional[Range] = pydantic.Field(
        alias="boundsRange",
        default=None,
        description="Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.",
    )
    bounds_period: typing.Optional[Period] = pydantic.Field(
        alias="boundsPeriod",
        default=None,
        description="Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.",
    )
    count: typing.Optional[PositiveInt] = pydantic.Field(
        default=None,
        description="A total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count values.",
    )
    count_max: typing.Optional[PositiveInt] = pydantic.Field(
        alias="countMax",
        default=None,
        description="If present, indicates that the count is a range - so to perform the action between [count] and [countMax] times.",
    )
    duration: typing.Optional[Decimal] = pydantic.Field(
        default=None,
        description="How long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the duration.",
    )
    duration_max: typing.Optional[Decimal] = pydantic.Field(
        alias="durationMax",
        default=None,
        description="If present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time length.",
    )
    duration_unit: typing.Optional[TimingRepeatDurationUnit] = pydantic.Field(
        alias="durationUnit", default=None, description="The units of time for the duration, in UCUM units."
    )
    frequency: typing.Optional[PositiveInt] = pydantic.Field(
        default=None,
        description="The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequency.",
    )
    frequency_max: typing.Optional[PositiveInt] = pydantic.Field(
        alias="frequencyMax",
        default=None,
        description="If present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period range.",
    )
    period: typing.Optional[Decimal] = pydantic.Field(
        default=None,
        description='Indicates the duration of time over which repetitions are to occur; e.g. to express "3 times per day", 3 would be the frequency and "1 day" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period length.',
    )
    period_max: typing.Optional[Decimal] = pydantic.Field(
        alias="periodMax",
        default=None,
        description='If present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as "do this once every 3-5 days.',
    )
    period_unit: typing.Optional[TimingRepeatPeriodUnit] = pydantic.Field(
        alias="periodUnit", default=None, description="The units of time for the period in UCUM units."
    )
    day_of_week: typing.Optional[typing.List[Code]] = pydantic.Field(
        alias="dayOfWeek",
        default=None,
        description="If one or more days of week is provided, then the action happens only on the specified day(s).",
    )
    time_of_day: typing.Optional[typing.List[Time]] = pydantic.Field(
        alias="timeOfDay", default=None, description="Specified time of day for action to take place."
    )
    when: typing.Optional[typing.List[TimingRepeatWhenItem]] = pydantic.Field(
        default=None,
        description="An approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occur.",
    )
    offset: typing.Optional[UnsignedInt] = pydantic.Field(
        default=None,
        description="The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the event.",
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


from .duration import Duration  # noqa: E402
from .extension import Extension  # noqa: E402
from .period import Period  # noqa: E402
from .range import Range  # noqa: E402

TimingRepeat.update_forward_refs()
