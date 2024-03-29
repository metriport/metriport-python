# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .instant import Instant
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AppointmentResponse(BaseResource):
    """
    A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    """

    resource_type: typing.Literal["AppointmentResponse"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="This records identifiers associated with this appointment response concern that are defined by business processes and/ or used to refer to it when a direct URL reference to the resource itself is not appropriate.",
    )
    appointment: Reference = pydantic.Field(description="Appointment that this response is replying to.")
    start: typing.Optional[Instant] = pydantic.Field(
        default=None, description="Date/Time that the appointment is to take place, or requested new start time."
    )
    end: typing.Optional[Instant] = pydantic.Field(
        default=None,
        description="This may be either the same as the appointment request to confirm the details of the appointment, or alternately a new time to request a re-negotiation of the end time.",
    )
    participant_type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="participantType", default=None, description="Role of participant in the appointment."
    )
    actor: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="A Person, Location, HealthcareService, or Device that is participating in the appointment.",
    )
    participant_status: typing.Optional[Code] = pydantic.Field(
        alias="participantStatus",
        default=None,
        description="Participation status of the participant. When the status is declined or tentative if the start/end times are different to the appointment, then these times should be interpreted as a requested time change. When the status is accepted, the times can either be the time of the appointment (as a confirmation of the time) or can be empty.",
    )
    comment: typing.Optional[str] = pydantic.Field(
        default=None, description="Additional comments about the appointment."
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
