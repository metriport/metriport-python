# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .evidence_variable_characteristic import EvidenceVariableCharacteristic
from .evidence_variable_status import EvidenceVariableStatus
from .evidence_variable_type import EvidenceVariableType
from .identifier import Identifier
from .markdown import Markdown
from .period import Period
from .related_artifact import RelatedArtifact
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EvidenceVariable(BaseResource):
    """
    The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    """

    resource_type: typing_extensions.Literal["EvidenceVariable"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        description="An absolute URI that is used to identify this evidence variable when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this evidence variable is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the evidence variable is stored on different servers."
    )
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="A formal identifier that is used to identify this evidence variable when it is represented in other formats, or referenced in a specification, model, design or an instance."
    )
    version: typing.Optional[str] = pydantic.Field(
        description="The identifier that is used to identify this version of the evidence variable when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the evidence variable author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. To provide a version consistent with the Decision Support Service specification, use the format Major.Minor.Revision (e.g. 1.0.0). For more information on versioning knowledge assets, refer to the Decision Support Service specification. Note that a version is required for non-experimental active artifacts."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the evidence variable. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    title: typing.Optional[str] = pydantic.Field(
        description="A short, descriptive, user-friendly title for the evidence variable."
    )
    short_title: typing.Optional[str] = pydantic.Field(
        alias="shortTitle",
        description="The short title provides an alternate title for use in informal descriptive contexts where the full, formal title is not necessary.",
    )
    subtitle: typing.Optional[str] = pydantic.Field(
        description="An explanatory or alternate title for the EvidenceVariable giving additional information about its content."
    )
    status: typing.Optional[EvidenceVariableStatus] = pydantic.Field(
        description="The status of this evidence variable. Enables tracking the life-cycle of the content."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the evidence variable was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the evidence variable changes."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the evidence variable."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the evidence variable from a consumer's perspective."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="A human-readable string to clarify or explain concepts about the resource."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate evidence variable instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the evidence variable is intended to be used."
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        description="A copyright statement relating to the evidence variable and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the evidence variable."
    )
    approval_date: typing.Optional[dt.date] = pydantic.Field(
        alias="approvalDate",
        description="The date on which the resource content was approved by the publisher. Approval happens once when the content is officially approved for usage.",
    )
    last_review_date: typing.Optional[dt.date] = pydantic.Field(
        alias="lastReviewDate",
        description="The date on which the resource content was last reviewed. Review happens periodically after approval but does not change the original approval date.",
    )
    effective_period: typing.Optional[Period] = pydantic.Field(
        alias="effectivePeriod",
        description="The period during which the evidence variable content was or is planned to be in active use.",
    )
    topic: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Descriptive topics related to the content of the EvidenceVariable. Topics provide a high-level categorization grouping types of EvidenceVariables that can be useful for filtering and searching."
    )
    author: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="An individiual or organization primarily involved in the creation and maintenance of the content."
    )
    editor: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="An individual or organization primarily responsible for internal coherence of the content."
    )
    reviewer: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="An individual or organization primarily responsible for review of some aspect of the content."
    )
    endorser: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="An individual or organization responsible for officially endorsing the content for use in some setting."
    )
    related_artifact: typing.Optional[typing.List[RelatedArtifact]] = pydantic.Field(
        alias="relatedArtifact",
        description="Related artifacts such as additional documentation, justification, or bibliographic references.",
    )
    type: typing.Optional[EvidenceVariableType] = pydantic.Field(
        description="The type of evidence element, a population, an exposure, or an outcome."
    )
    characteristic: typing.List[EvidenceVariableCharacteristic] = pydantic.Field(
        description='A characteristic that defines the members of the evidence element. Multiple characteristics are applied with "and" semantics.'
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
