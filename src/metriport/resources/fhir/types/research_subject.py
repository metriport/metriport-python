# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .identifier import Identifier
from .period import Period
from .reference import Reference
from .research_subject_status import ResearchSubjectStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ResearchSubject(BaseResource):
    """
    A physical entity which is the primary unit of operational and/or administrative interest in a study.
    """

    resource_type: typing_extensions.Literal["ResearchSubject"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifiers assigned to this research subject for a study."
    )
    status: typing.Optional[ResearchSubjectStatus] = pydantic.Field(description="The current state of the subject.")
    period: typing.Optional[Period] = pydantic.Field(
        description="The dates the subject began and ended their participation in the study."
    )
    study: Reference = pydantic.Field(description="Reference to the study the subject is participating in.")
    individual: Reference = pydantic.Field(
        description="The record of the person or animal who is involved in the study."
    )
    assigned_arm: typing.Optional[str] = pydantic.Field(
        alias="assignedArm",
        description="The name of the arm in the study the subject is expected to follow as part of this study.",
    )
    actual_arm: typing.Optional[str] = pydantic.Field(
        alias="actualArm",
        description="The name of the arm in the study the subject actually followed as part of this study.",
    )
    consent: typing.Optional[Reference] = pydantic.Field(
        description="A record of the patient's informed agreement to participate in the study."
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
