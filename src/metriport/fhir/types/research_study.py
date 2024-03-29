# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .identifier import Identifier
from .markdown import Markdown
from .period import Period
from .reference import Reference
from .related_artifact import RelatedArtifact
from .research_study_arm import ResearchStudyArm
from .research_study_objective import ResearchStudyObjective
from .research_study_status import ResearchStudyStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ResearchStudy(BaseResource):
    """
    A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge. This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques. A ResearchStudy involves the gathering of information about human or animal subjects.
    """

    resource_type: typing.Literal["ResearchStudy"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="Identifiers assigned to this research study by the sponsor or other systems."
    )
    title: typing.Optional[str] = pydantic.Field(
        default=None, description="A short, descriptive user-friendly label for the study."
    )
    protocol: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="The set of steps expected to be performed as part of the execution of the study."
    )
    part_of: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="partOf",
        default=None,
        description="A larger research study of which this particular study is a component or step.",
    )
    status: typing.Optional[ResearchStudyStatus] = pydantic.Field(
        default=None, description="The current state of the study."
    )
    primary_purpose_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="primaryPurposeType",
        default=None,
        description="The type of study based upon the intent of the study's activities. A classification of the intent of the study.",
    )
    phase: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="The stage in the progression of a therapy from initial experimental use in humans in clinical trials to post-market evaluation.",
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="Codes categorizing the type of study such as investigational vs. observational, type of blinding, type of randomization, safety vs. efficacy, etc.",
    )
    focus: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="The medication(s), food(s), therapy(ies), device(s) or other concerns or interventions that the study is seeking to gain more information about.",
    )
    condition: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description='The condition that is the focus of the study. For example, In a study to examine risk factors for Lupus, might have as an inclusion criterion "healthy volunteer", but the target condition code would be a Lupus SNOMED code.',
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        default=None, description="Contact details to assist a user in learning more about or engaging with the study."
    )
    related_artifact: typing.Optional[typing.List[RelatedArtifact]] = pydantic.Field(
        alias="relatedArtifact", default=None, description="Citations, references and other related documents."
    )
    keyword: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="Key terms to aid in searching for or filtering the study."
    )
    location: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="Indicates a country, state or other region where the study is taking place."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        default=None, description="A full description of how the study is being conducted."
    )
    enrollment: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description='Reference to a Group that defines the criteria for and quantity of subjects participating in the study. E.g. " 200 female Europeans between the ages of 20 and 45 with early onset diabetes".',
    )
    period: typing.Optional[Period] = pydantic.Field(
        default=None,
        description="Identifies the start date and the expected (or actual, depending on status) end date for the study.",
    )
    sponsor: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="An organization that initiates the investigation and is legally responsible for the study.",
    )
    principal_investigator: typing.Optional[Reference] = pydantic.Field(
        alias="principalInvestigator",
        default=None,
        description="A researcher in a study who oversees multiple aspects of the study, such as concept development, protocol writing, protocol submission for IRB approval, participant recruitment, informed consent, data collection, analysis, interpretation and presentation.",
    )
    site: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="A facility in which study activities are conducted."
    )
    reason_stopped: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="reasonStopped",
        default=None,
        description="A description and/or code explaining the premature termination of the study.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None, description="Comments made about the study by the performer, subject or other participants."
    )
    arm: typing.Optional[typing.List[ResearchStudyArm]] = pydantic.Field(
        default=None,
        description="Describes an expected sequence of events for one of the participants of a study. E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out, follow-up.",
    )
    objective: typing.Optional[typing.List[ResearchStudyObjective]] = pydantic.Field(
        default=None,
        description="A goal that the study is aiming to achieve in terms of a scientific question to be answered by the analysis of data collected during the study.",
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
