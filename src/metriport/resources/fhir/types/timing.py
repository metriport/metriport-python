# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .date_time import DateTime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Timing(pydantic.BaseModel):
    """
    Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    event: typing.Optional[typing.List[DateTime]] = pydantic.Field(
        description="Identifies specific times when the event occurs."
    )
    repeat: typing.Optional[TimingRepeat] = pydantic.Field(
        description="A set of rules that describe when the event is scheduled."
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code)."
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


from .codeable_concept import CodeableConcept  # noqa: E402
from .extension import Extension  # noqa: E402
from .timing_repeat import TimingRepeat  # noqa: E402

Timing.update_forward_refs()
