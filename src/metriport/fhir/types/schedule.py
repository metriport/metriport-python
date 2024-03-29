# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Schedule(BaseResource):
    """
    A container for slots of time that may be available for booking appointments.
    """

    resource_type: typing.Literal["Schedule"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="External Ids for this item."
    )
    active: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="Whether this schedule record is in active use or should not be used (such as was entered in error).",
    )
    service_category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="serviceCategory",
        default=None,
        description="A broad categorization of the service that is to be performed during this appointment.",
    )
    service_type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="serviceType",
        default=None,
        description="The specific service that is to be performed during this appointment.",
    )
    specialty: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="The specialty of a practitioner that would be required to perform the service requested in this appointment.",
    )
    actor: typing.List[Reference] = pydantic.Field(
        description="Slots that reference this schedule resource provide the availability details to these referenced resource(s)."
    )
    planning_horizon: typing.Optional[Period] = pydantic.Field(
        alias="planningHorizon",
        default=None,
        description='The period of time that the slots that reference this Schedule resource cover (even if none exist). These cover the amount of time that an organization\'s planning horizon; the interval for which they are currently accepting appointments. This does not define a "template" for planning outside these dates.',
    )
    comment: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Comments on the availability to describe any extended information. Such as custom constraints on the slots that may be associated.",
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
