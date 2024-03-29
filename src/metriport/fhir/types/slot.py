# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .instant import Instant
from .reference import Reference
from .slot_status import SlotStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Slot(BaseResource):
    """
    A slot of time on a schedule that may be available for booking appointments.
    """

    resource_type: typing.Literal["Slot"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="External Ids for this item."
    )
    service_category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="serviceCategory",
        default=None,
        description="A broad categorization of the service that is to be performed during this appointment.",
    )
    service_type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="serviceType",
        default=None,
        description="The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource.",
    )
    specialty: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="The specialty of a practitioner that would be required to perform the service requested in this appointment.",
    )
    appointment_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="appointmentType",
        default=None,
        description="The style of appointment or patient that may be booked in the slot (not service type).",
    )
    schedule: Reference = pydantic.Field(
        description="The schedule resource that this slot defines an interval of status information."
    )
    status: typing.Optional[SlotStatus] = pydantic.Field(
        default=None,
        description=("busy \n" " free \n" " busy-unavailable \n" " busy-tentative \n" " entered-in-error.\n"),
    )
    start: typing.Optional[Instant] = pydantic.Field(default=None, description="Date/Time that the slot is to begin.")
    end: typing.Optional[Instant] = pydantic.Field(default=None, description="Date/Time that the slot is to conclude.")
    overbooked: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="This slot has already been overbooked, appointments are unlikely to be accepted for this time.",
    )
    comment: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Comments on the slot to describe any extended information. Such as custom constraints on the slot.",
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
