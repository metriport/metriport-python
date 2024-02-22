# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .data_requirement import DataRequirement
from .duration import Duration
from .evidence_variable_characteristic_group_measure import EvidenceVariableCharacteristicGroupMeasure
from .expression import Expression
from .extension import Extension
from .period import Period
from .reference import Reference
from .timing import Timing
from .trigger_definition import TriggerDefinition
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EvidenceVariableCharacteristic(pydantic.BaseModel):
    """
    The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
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
    description: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A short, natural language description of the characteristic that could be used to communicate the criteria to an end-user.",
    )
    definition_reference: typing.Optional[Reference] = pydantic.Field(
        alias="definitionReference",
        default=None,
        description="Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_canonical: typing.Optional[str] = pydantic.Field(
        alias="definitionCanonical",
        default=None,
        description="Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="definitionCodeableConcept",
        default=None,
        description="Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_expression: typing.Optional[Expression] = pydantic.Field(
        alias="definitionExpression",
        default=None,
        description="Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_data_requirement: typing.Optional[DataRequirement] = pydantic.Field(
        alias="definitionDataRequirement",
        default=None,
        description="Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    definition_trigger_definition: typing.Optional[TriggerDefinition] = pydantic.Field(
        alias="definitionTriggerDefinition",
        default=None,
        description="Define members of the evidence element using Codes (such as condition, medication, or observation), Expressions ( using an expression language such as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in the last year).",
    )
    usage_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="usageContext",
        default=None,
        description="Use UsageContext to define the members of the population, such as Age Ranges, Genders, Settings.",
    )
    exclude: typing.Optional[bool] = pydantic.Field(
        default=None, description="When true, members with this characteristic are excluded from the element."
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
    time_from_start: typing.Optional[Duration] = pydantic.Field(
        alias="timeFromStart", default=None, description="Indicates duration from the participant's study entry."
    )
    group_measure: typing.Optional[EvidenceVariableCharacteristicGroupMeasure] = pydantic.Field(
        alias="groupMeasure",
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
