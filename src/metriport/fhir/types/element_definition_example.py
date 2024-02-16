# This file was auto-generated by Fern from our API Definition.

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


class ElementDefinitionExample(pydantic.BaseModel):
    """
    Captures constraints on each element within the resource, profile, or extension.
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
    label: typing.Optional[str] = pydantic.Field(
        description="Describes the purpose of this example amoung the set of examples."
    )
    value_base_64_binary: typing.Optional[str] = pydantic.Field(
        alias="valueBase64Binary",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_boolean: typing.Optional[bool] = pydantic.Field(
        alias="valueBoolean",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_canonical: typing.Optional[str] = pydantic.Field(
        alias="valueCanonical",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_code: typing.Optional[str] = pydantic.Field(
        alias="valueCode",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_date: typing.Optional[str] = pydantic.Field(
        alias="valueDate",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_date_time: typing.Optional[str] = pydantic.Field(
        alias="valueDateTime",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_decimal: typing.Optional[float] = pydantic.Field(
        alias="valueDecimal",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_id: typing.Optional[str] = pydantic.Field(
        alias="valueId",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_instant: typing.Optional[str] = pydantic.Field(
        alias="valueInstant",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_integer: typing.Optional[float] = pydantic.Field(
        alias="valueInteger",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_markdown: typing.Optional[str] = pydantic.Field(
        alias="valueMarkdown",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_oid: typing.Optional[str] = pydantic.Field(
        alias="valueOid",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_positive_int: typing.Optional[float] = pydantic.Field(
        alias="valuePositiveInt",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_string: typing.Optional[str] = pydantic.Field(
        alias="valueString",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_time: typing.Optional[str] = pydantic.Field(
        alias="valueTime",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_unsigned_int: typing.Optional[float] = pydantic.Field(
        alias="valueUnsignedInt",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_uri: typing.Optional[str] = pydantic.Field(
        alias="valueUri",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_url: typing.Optional[str] = pydantic.Field(
        alias="valueUrl",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_uuid: typing.Optional[str] = pydantic.Field(
        alias="valueUuid",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_address: typing.Optional[Address] = pydantic.Field(
        alias="valueAddress",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_age: typing.Optional[Age] = pydantic.Field(
        alias="valueAge",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_annotation: typing.Optional[Annotation] = pydantic.Field(
        alias="valueAnnotation",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_attachment: typing.Optional[Attachment] = pydantic.Field(
        alias="valueAttachment",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="valueCodeableConcept",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_coding: typing.Optional[Coding] = pydantic.Field(
        alias="valueCoding",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_contact_point: typing.Optional[ContactPoint] = pydantic.Field(
        alias="valueContactPoint",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_count: typing.Optional[Count] = pydantic.Field(
        alias="valueCount",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_distance: typing.Optional[Distance] = pydantic.Field(
        alias="valueDistance",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_duration: typing.Optional[Duration] = pydantic.Field(
        alias="valueDuration",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_human_name: typing.Optional[HumanName] = pydantic.Field(
        alias="valueHumanName",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="valueIdentifier",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_money: typing.Optional[Money] = pydantic.Field(
        alias="valueMoney",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_period: typing.Optional[Period] = pydantic.Field(
        alias="valuePeriod",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="valueQuantity",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_range: typing.Optional[Range] = pydantic.Field(
        alias="valueRange",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_ratio: typing.Optional[Ratio] = pydantic.Field(
        alias="valueRatio",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_reference: typing.Optional[Reference] = pydantic.Field(
        alias="valueReference",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_sampled_data: typing.Optional[SampledData] = pydantic.Field(
        alias="valueSampledData",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_signature: typing.Optional[Signature] = pydantic.Field(
        alias="valueSignature",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_timing: typing.Optional[Timing] = pydantic.Field(
        alias="valueTiming",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_contact_detail: typing.Optional[ContactDetail] = pydantic.Field(
        alias="valueContactDetail",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_contributor: typing.Optional[Contributor] = pydantic.Field(
        alias="valueContributor",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_data_requirement: typing.Optional[DataRequirement] = pydantic.Field(
        alias="valueDataRequirement",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_expression: typing.Optional[Expression] = pydantic.Field(
        alias="valueExpression",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_parameter_definition: typing.Optional[ParameterDefinition] = pydantic.Field(
        alias="valueParameterDefinition",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_related_artifact: typing.Optional[RelatedArtifact] = pydantic.Field(
        alias="valueRelatedArtifact",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_trigger_definition: typing.Optional[TriggerDefinition] = pydantic.Field(
        alias="valueTriggerDefinition",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_usage_context: typing.Optional[UsageContext] = pydantic.Field(
        alias="valueUsageContext",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_dosage: typing.Optional[Dosage] = pydantic.Field(
        alias="valueDosage",
        description="The actual value for the element, which must be one of the types allowed for this element.",
    )
    value_meta: typing.Optional[Meta] = pydantic.Field(
        alias="valueMeta",
        description="The actual value for the element, which must be one of the types allowed for this element.",
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