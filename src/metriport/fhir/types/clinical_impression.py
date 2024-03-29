# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .clinical_impression_finding import ClinicalImpressionFinding
from .clinical_impression_investigation import ClinicalImpressionInvestigation
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClinicalImpression(BaseResource):
    """
    A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter, but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
    """

    resource_type: typing.Literal["ClinicalImpression"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Business identifiers assigned to this clinical impression by the performer or other systems which remain constant as the resource is updated and propagates from server to server.",
    )
    status: typing.Optional[Code] = pydantic.Field(
        default=None, description="Identifies the workflow status of the assessment."
    )
    status_reason: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="statusReason",
        default=None,
        description="Captures the reason for the current state of the ClinicalImpression.",
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="Categorizes the type of clinical assessment performed."
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A summary of the context and/or cause of the assessment - why / where it was performed, and what patient events/status prompted it.",
    )
    subject: Reference = pydantic.Field(
        description="The patient or group of individuals assessed as part of this record."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The Encounter during which this ClinicalImpression was created or to which the creation of this record is tightly associated.",
    )
    effective_date_time: typing.Optional[str] = pydantic.Field(
        alias="effectiveDateTime",
        default=None,
        description="The point in time or period over which the subject was assessed.",
    )
    effective_period: typing.Optional[Period] = pydantic.Field(
        alias="effectivePeriod",
        default=None,
        description="The point in time or period over which the subject was assessed.",
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        default=None, description="Indicates when the documentation of the assessment was complete."
    )
    assessor: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The clinician performing the assessment."
    )
    previous: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="A reference to the last assessment that was conducted on this patient. Assessments are often/usually ongoing in nature; a care provider (practitioner or team) will make new assessments on an ongoing basis as new data arises or the patient's conditions changes.",
    )
    problem: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="A list of the relevant problems/conditions for a patient."
    )
    investigation: typing.Optional[typing.List[ClinicalImpressionInvestigation]] = pydantic.Field(
        default=None,
        description="One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomes.",
    )
    protocol: typing.Optional[typing.List[Uri]] = pydantic.Field(
        default=None,
        description="Reference to a specific published clinical protocol that was followed during this assessment, and/or that provides evidence in support of the diagnosis.",
    )
    summary: typing.Optional[str] = pydantic.Field(
        default=None, description="A text summary of the investigations and the diagnosis."
    )
    finding: typing.Optional[typing.List[ClinicalImpressionFinding]] = pydantic.Field(
        default=None,
        description="Specific findings or diagnoses that were considered likely or relevant to ongoing treatment.",
    )
    prognosis_codeable_concept: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="prognosisCodeableConcept", default=None, description="Estimate of likely outcome."
    )
    prognosis_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="prognosisReference", default=None, description="RiskAssessment expressing likely outcome."
    )
    supporting_info: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="supportingInfo", default=None, description="Information supporting the clinical impression."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None,
        description="Commentary about the impression, typically recorded after the impression itself was made, though supplemental notes by the original author could also appear.",
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
