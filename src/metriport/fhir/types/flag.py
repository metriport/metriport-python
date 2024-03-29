# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .flag_status import FlagStatus
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Flag(BaseResource):
    """
    Prospective warnings of potential issues when providing care to the patient.
    """

    resource_type: typing.Literal["Flag"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Business identifiers assigned to this flag by the performer or other systems which remain constant as the resource is updated and propagates from server to server.",
    )
    status: typing.Optional[FlagStatus] = pydantic.Field(default=None, description="Supports basic workflow.")
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="Allows a flag to be divided into different categories like clinical, administrative etc. Intended to be used as a means of filtering which flags are displayed to particular user or in a given context.",
    )
    code: CodeableConcept = pydantic.Field(
        description="The coded value or textual component of the flag to display to the user."
    )
    subject: Reference = pydantic.Field(
        description="The patient, location, group, organization, or practitioner etc. this is about record this flag is associated with."
    )
    period: typing.Optional[Period] = pydantic.Field(
        default=None,
        description="The period of time from the activation of the flag to inactivation of the flag. If the flag is active, the end of the period should be unspecified.",
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        default=None, description="This alert is only relevant during the encounter."
    )
    author: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The person, organization or device that created the flag."
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
