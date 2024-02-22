# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .data_requirement import DataRequirement
from .duration import Duration
from .expression import Expression
from .extension import Extension
from .period import Period
from .research_element_definition_characteristic_participant_effective_group_measure import (
    ResearchElementDefinitionCharacteristicParticipantEffectiveGroupMeasure,
)
from .research_element_definition_characteristic_study_effective_group_measure import (
    ResearchElementDefinitionCharacteristicStudyEffectiveGroupMeasure,
)
from .timing import Timing
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ResearchElementDefinitionCharacteristic(pydantic.BaseModel):
    """
    The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    definition_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="definitionCodeableConcept",
        default=None,
        description="Define members of the research element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_canonical: typing.Optional[str] = pydantic.Field(
        alias="definitionCanonical",
        default=None,
        description="Define members of the research element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_expression: typing.Optional[Expression] = pydantic.Field(
        alias="definitionExpression",
        default=None,
        description="Define members of the research element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_data_requirement: typing.Optional[DataRequirement] = pydantic.Field(
        alias="definitionDataRequirement",
        default=None,
        description="Define members of the research element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    usage_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="usageContext",
        default=None,
        description="Use UsageContext to define the members of the population, such as Age Ranges, Genders, Settings.",
    )
    exclude: typing.Optional[bool] = pydantic.Field(
        default=None, description="When true, members with this characteristic are excluded from the element."
    )
    unit_of_measure: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="unitOfMeasure", default=None, description="Specifies the UCUM unit for the outcome."
    )
    study_effective_description: typing.Optional[str] = pydantic.Field(
        alias="studyEffectiveDescription",
        default=None,
        description="A narrative description of the time period the study covers.",
    )
    study_effective_date_time: typing.Optional[str] = pydantic.Field(
        alias="studyEffectiveDateTime", default=None, description="Indicates what effective period the study covers."
    )
    study_effective_period: typing.Optional[Period] = pydantic.Field(
        alias="studyEffectivePeriod", default=None, description="Indicates what effective period the study covers."
    )
    study_effective_duration: typing.Optional[Duration] = pydantic.Field(
        alias="studyEffectiveDuration", default=None, description="Indicates what effective period the study covers."
    )
    study_effective_timing: typing.Optional[Timing] = pydantic.Field(
        alias="studyEffectiveTiming", default=None, description="Indicates what effective period the study covers."
    )
    study_effective_time_from_start: typing.Optional[Duration] = pydantic.Field(
        alias="studyEffectiveTimeFromStart", default=None, description="Indicates duration from the study initiation."
    )
    study_effective_group_measure: typing.Optional[
        ResearchElementDefinitionCharacteristicStudyEffectiveGroupMeasure
    ] = pydantic.Field(
        alias="studyEffectiveGroupMeasure",
        default=None,
        description="Indicates how elements are aggregated within the study effective period.",
    )
    participant_effective_description: typing.Optional[str] = pydantic.Field(
        alias="participantEffectiveDescription",
        default=None,
        description="A narrative description of the time period the study covers.",
    )
    participant_effective_date_time: typing.Optional[str] = pydantic.Field(
        alias="participantEffectiveDateTime",
        default=None,
        description="Indicates what effective period the study covers.",
    )
    participant_effective_period: typing.Optional[Period] = pydantic.Field(
        alias="participantEffectivePeriod",
        default=None,
        description="Indicates what effective period the study covers.",
    )
    participant_effective_duration: typing.Optional[Duration] = pydantic.Field(
        alias="participantEffectiveDuration",
        default=None,
        description="Indicates what effective period the study covers.",
    )
    participant_effective_timing: typing.Optional[Timing] = pydantic.Field(
        alias="participantEffectiveTiming",
        default=None,
        description="Indicates what effective period the study covers.",
    )
    participant_effective_time_from_start: typing.Optional[Duration] = pydantic.Field(
        alias="participantEffectiveTimeFromStart",
        default=None,
        description="Indicates duration from the participant's study entry.",
    )
    participant_effective_group_measure: typing.Optional[
        ResearchElementDefinitionCharacteristicParticipantEffectiveGroupMeasure
    ] = pydantic.Field(
        alias="participantEffectiveGroupMeasure",
        default=None,
        description="Indicates how elements are aggregated within the study effective period.",
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
