# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .age import Age
from .annotation import Annotation
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .condition_evidence import ConditionEvidence
from .condition_stage import ConditionStage
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .range import Range
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Condition(BaseResource):
    """
    A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.
    """

    resource_type: typing.Literal["Condition"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Business identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to server.",
    )
    clinical_status: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="clinicalStatus", default=None, description="The clinical status of the condition."
    )
    verification_status: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="verificationStatus",
        default=None,
        description="The verification status to support the clinical status of the condition.",
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="A category assigned to the condition."
    )
    severity: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="A subjective assessment of the severity of the condition as evaluated by the clinician.",
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="Identification of the condition, problem or diagnosis."
    )
    body_site: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="bodySite", default=None, description="The anatomical location where this condition manifests itself."
    )
    subject: Reference = pydantic.Field(
        description="Indicates the patient or group who the condition record is associated with."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The Encounter during which this Condition was created or to which the creation of this record is tightly associated.",
    )
    onset_date_time: typing.Optional[str] = pydantic.Field(
        alias="onsetDateTime",
        default=None,
        description="Estimated or actual date or date-time the condition began, in the opinion of the clinician.",
    )
    onset_age: typing.Optional[Age] = pydantic.Field(
        alias="onsetAge",
        default=None,
        description="Estimated or actual date or date-time the condition began, in the opinion of the clinician.",
    )
    onset_period: typing.Optional[Period] = pydantic.Field(
        alias="onsetPeriod",
        default=None,
        description="Estimated or actual date or date-time the condition began, in the opinion of the clinician.",
    )
    onset_range: typing.Optional[Range] = pydantic.Field(
        alias="onsetRange",
        default=None,
        description="Estimated or actual date or date-time the condition began, in the opinion of the clinician.",
    )
    onset_string: typing.Optional[str] = pydantic.Field(
        alias="onsetString",
        default=None,
        description="Estimated or actual date or date-time the condition began, in the opinion of the clinician.",
    )
    abatement_date_time: typing.Optional[str] = pydantic.Field(
        alias="abatementDateTime",
        default=None,
        description='The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.',
    )
    abatement_age: typing.Optional[Age] = pydantic.Field(
        alias="abatementAge",
        default=None,
        description='The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.',
    )
    abatement_period: typing.Optional[Period] = pydantic.Field(
        alias="abatementPeriod",
        default=None,
        description='The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.',
    )
    abatement_range: typing.Optional[Range] = pydantic.Field(
        alias="abatementRange",
        default=None,
        description='The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.',
    )
    abatement_string: typing.Optional[str] = pydantic.Field(
        alias="abatementString",
        default=None,
        description='The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abate.',
    )
    recorded_date: typing.Optional[DateTime] = pydantic.Field(
        alias="recordedDate",
        default=None,
        description="The recordedDate represents when this particular Condition record was created in the system, which is often a system-generated date.",
    )
    recorder: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Individual who recorded the record and takes responsibility for its content."
    )
    asserter: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Individual who is making the condition statement."
    )
    stage: typing.Optional[typing.List[ConditionStage]] = pydantic.Field(
        default=None, description="Clinical stage or grade of a condition. May include formal severity assessments."
    )
    evidence: typing.Optional[typing.List[ConditionEvidence]] = pydantic.Field(
        default=None,
        description="Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None,
        description="Additional information about the Condition. This is a general notes/comments entry for description of the Condition, its diagnosis and prognosis.",
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
