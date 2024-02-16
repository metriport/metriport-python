# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .address import Address
from .age import Age
from .annotation import Annotation
from .attachment import Attachment
from .codeable_concept import CodeableConcept
from .coding import Coding
from .contact_detail import ContactDetail
from .contact_point import ContactPoint
from .contributor import Contributor
from .count import Count
from .data_requirement import DataRequirement
from .distance import Distance
from .dosage import Dosage
from .duration import Duration
from .expression import Expression
from .extension import Extension
from .human_name import HumanName
from .identifier import Identifier
from .meta import Meta
from .money import Money
from .parameter_definition import ParameterDefinition
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .reference import Reference
from .related_artifact import RelatedArtifact
from .sampled_data import SampledData
from .signature import Signature
from .timing import Timing
from .trigger_definition import TriggerDefinition
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ParametersParameter(pydantic.BaseModel):
    """
    This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    name: typing.Optional[str] = pydantic.Field(
        description="The name of the parameter (reference to the operation definition)."
    )
    value_base_64_binary: typing.Optional[str] = pydantic.Field(
        alias="valueBase64Binary", description="If the parameter is a data type."
    )
    value_boolean: typing.Optional[bool] = pydantic.Field(
        alias="valueBoolean", description="If the parameter is a data type."
    )
    value_canonical: typing.Optional[str] = pydantic.Field(
        alias="valueCanonical", description="If the parameter is a data type."
    )
    value_code: typing.Optional[str] = pydantic.Field(alias="valueCode", description="If the parameter is a data type.")
    value_date: typing.Optional[str] = pydantic.Field(alias="valueDate", description="If the parameter is a data type.")
    value_date_time: typing.Optional[str] = pydantic.Field(
        alias="valueDateTime", description="If the parameter is a data type."
    )
    value_decimal: typing.Optional[float] = pydantic.Field(
        alias="valueDecimal", description="If the parameter is a data type."
    )
    value_id: typing.Optional[str] = pydantic.Field(alias="valueId", description="If the parameter is a data type.")
    value_instant: typing.Optional[str] = pydantic.Field(
        alias="valueInstant", description="If the parameter is a data type."
    )
    value_integer: typing.Optional[float] = pydantic.Field(
        alias="valueInteger", description="If the parameter is a data type."
    )
    value_markdown: typing.Optional[str] = pydantic.Field(
        alias="valueMarkdown", description="If the parameter is a data type."
    )
    value_oid: typing.Optional[str] = pydantic.Field(alias="valueOid", description="If the parameter is a data type.")
    value_positive_int: typing.Optional[float] = pydantic.Field(
        alias="valuePositiveInt", description="If the parameter is a data type."
    )
    value_string: typing.Optional[str] = pydantic.Field(
        alias="valueString", description="If the parameter is a data type."
    )
    value_time: typing.Optional[str] = pydantic.Field(alias="valueTime", description="If the parameter is a data type.")
    value_unsigned_int: typing.Optional[float] = pydantic.Field(
        alias="valueUnsignedInt", description="If the parameter is a data type."
    )
    value_uri: typing.Optional[str] = pydantic.Field(alias="valueUri", description="If the parameter is a data type.")
    value_url: typing.Optional[str] = pydantic.Field(alias="valueUrl", description="If the parameter is a data type.")
    value_uuid: typing.Optional[str] = pydantic.Field(alias="valueUuid", description="If the parameter is a data type.")
    value_address: typing.Optional[Address] = pydantic.Field(
        alias="valueAddress", description="If the parameter is a data type."
    )
    value_age: typing.Optional[Age] = pydantic.Field(alias="valueAge", description="If the parameter is a data type.")
    value_annotation: typing.Optional[Annotation] = pydantic.Field(
        alias="valueAnnotation", description="If the parameter is a data type."
    )
    value_attachment: typing.Optional[Attachment] = pydantic.Field(
        alias="valueAttachment", description="If the parameter is a data type."
    )
    value_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="valueCodeableConcept", description="If the parameter is a data type."
    )
    value_coding: typing.Optional[Coding] = pydantic.Field(
        alias="valueCoding", description="If the parameter is a data type."
    )
    value_contact_point: typing.Optional[ContactPoint] = pydantic.Field(
        alias="valueContactPoint", description="If the parameter is a data type."
    )
    value_count: typing.Optional[Count] = pydantic.Field(
        alias="valueCount", description="If the parameter is a data type."
    )
    value_distance: typing.Optional[Distance] = pydantic.Field(
        alias="valueDistance", description="If the parameter is a data type."
    )
    value_duration: typing.Optional[Duration] = pydantic.Field(
        alias="valueDuration", description="If the parameter is a data type."
    )
    value_human_name: typing.Optional[HumanName] = pydantic.Field(
        alias="valueHumanName", description="If the parameter is a data type."
    )
    value_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="valueIdentifier", description="If the parameter is a data type."
    )
    value_money: typing.Optional[Money] = pydantic.Field(
        alias="valueMoney", description="If the parameter is a data type."
    )
    value_period: typing.Optional[Period] = pydantic.Field(
        alias="valuePeriod", description="If the parameter is a data type."
    )
    value_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="valueQuantity", description="If the parameter is a data type."
    )
    value_range: typing.Optional[Range] = pydantic.Field(
        alias="valueRange", description="If the parameter is a data type."
    )
    value_ratio: typing.Optional[Ratio] = pydantic.Field(
        alias="valueRatio", description="If the parameter is a data type."
    )
    value_reference: typing.Optional[Reference] = pydantic.Field(
        alias="valueReference", description="If the parameter is a data type."
    )
    value_sampled_data: typing.Optional[SampledData] = pydantic.Field(
        alias="valueSampledData", description="If the parameter is a data type."
    )
    value_signature: typing.Optional[Signature] = pydantic.Field(
        alias="valueSignature", description="If the parameter is a data type."
    )
    value_timing: typing.Optional[Timing] = pydantic.Field(
        alias="valueTiming", description="If the parameter is a data type."
    )
    value_contact_detail: typing.Optional[ContactDetail] = pydantic.Field(
        alias="valueContactDetail", description="If the parameter is a data type."
    )
    value_contributor: typing.Optional[Contributor] = pydantic.Field(
        alias="valueContributor", description="If the parameter is a data type."
    )
    value_data_requirement: typing.Optional[DataRequirement] = pydantic.Field(
        alias="valueDataRequirement", description="If the parameter is a data type."
    )
    value_expression: typing.Optional[Expression] = pydantic.Field(
        alias="valueExpression", description="If the parameter is a data type."
    )
    value_parameter_definition: typing.Optional[ParameterDefinition] = pydantic.Field(
        alias="valueParameterDefinition", description="If the parameter is a data type."
    )
    value_related_artifact: typing.Optional[RelatedArtifact] = pydantic.Field(
        alias="valueRelatedArtifact", description="If the parameter is a data type."
    )
    value_trigger_definition: typing.Optional[TriggerDefinition] = pydantic.Field(
        alias="valueTriggerDefinition", description="If the parameter is a data type."
    )
    value_usage_context: typing.Optional[UsageContext] = pydantic.Field(
        alias="valueUsageContext", description="If the parameter is a data type."
    )
    value_dosage: typing.Optional[Dosage] = pydantic.Field(
        alias="valueDosage", description="If the parameter is a data type."
    )
    value_meta: typing.Optional[Meta] = pydantic.Field(
        alias="valueMeta", description="If the parameter is a data type."
    )
    resource: typing.Any = pydantic.Field(description="If the parameter is a whole resource.")
    part: typing.Optional[typing.List[ParametersParameter]] = pydantic.Field(
        description="A named part of a multi-part parameter."
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


ParametersParameter.update_forward_refs()