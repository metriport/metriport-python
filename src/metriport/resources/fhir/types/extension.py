# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Extension(pydantic.BaseModel):
    """
    Optional Extension Element - found in all resources.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    url: typing.Optional[Uri] = pydantic.Field(
        description="Source of the definition for the extension code - a logical name or a URL."
    )
    value_base_64_binary: typing.Optional[str] = pydantic.Field(
        alias="valueBase64Binary",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_boolean: typing.Optional[bool] = pydantic.Field(
        alias="valueBoolean",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_canonical: typing.Optional[str] = pydantic.Field(
        alias="valueCanonical",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_code: typing.Optional[str] = pydantic.Field(
        alias="valueCode",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_date: typing.Optional[str] = pydantic.Field(
        alias="valueDate",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_date_time: typing.Optional[str] = pydantic.Field(
        alias="valueDateTime",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_decimal: typing.Optional[float] = pydantic.Field(
        alias="valueDecimal",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_id: typing.Optional[str] = pydantic.Field(
        alias="valueId",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_instant: typing.Optional[str] = pydantic.Field(
        alias="valueInstant",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_integer: typing.Optional[float] = pydantic.Field(
        alias="valueInteger",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_markdown: typing.Optional[str] = pydantic.Field(
        alias="valueMarkdown",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_oid: typing.Optional[str] = pydantic.Field(
        alias="valueOid",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_positive_int: typing.Optional[float] = pydantic.Field(
        alias="valuePositiveInt",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_string: typing.Optional[str] = pydantic.Field(
        alias="valueString",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_time: typing.Optional[str] = pydantic.Field(
        alias="valueTime",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_unsigned_int: typing.Optional[float] = pydantic.Field(
        alias="valueUnsignedInt",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_uri: typing.Optional[str] = pydantic.Field(
        alias="valueUri",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_url: typing.Optional[str] = pydantic.Field(
        alias="valueUrl",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_uuid: typing.Optional[str] = pydantic.Field(
        alias="valueUuid",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_address: typing.Optional[Address] = pydantic.Field(
        alias="valueAddress",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_age: typing.Optional[Age] = pydantic.Field(
        alias="valueAge",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_annotation: typing.Optional[Annotation] = pydantic.Field(
        alias="valueAnnotation",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_attachment: typing.Optional[Attachment] = pydantic.Field(
        alias="valueAttachment",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="valueCodeableConcept",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_coding: typing.Optional[Coding] = pydantic.Field(
        alias="valueCoding",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_contact_point: typing.Optional[ContactPoint] = pydantic.Field(
        alias="valueContactPoint",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_count: typing.Optional[Count] = pydantic.Field(
        alias="valueCount",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_distance: typing.Optional[Distance] = pydantic.Field(
        alias="valueDistance",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_duration: typing.Optional[Duration] = pydantic.Field(
        alias="valueDuration",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_human_name: typing.Optional[HumanName] = pydantic.Field(
        alias="valueHumanName",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="valueIdentifier",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_money: typing.Optional[Money] = pydantic.Field(
        alias="valueMoney",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_period: typing.Optional[Period] = pydantic.Field(
        alias="valuePeriod",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="valueQuantity",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_range: typing.Optional[Range] = pydantic.Field(
        alias="valueRange",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_ratio: typing.Optional[Ratio] = pydantic.Field(
        alias="valueRatio",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_reference: typing.Optional[Reference] = pydantic.Field(
        alias="valueReference",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_sampled_data: typing.Optional[SampledData] = pydantic.Field(
        alias="valueSampledData",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_signature: typing.Optional[Signature] = pydantic.Field(
        alias="valueSignature",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_timing: typing.Optional[Timing] = pydantic.Field(
        alias="valueTiming",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_contact_detail: typing.Optional[ContactDetail] = pydantic.Field(
        alias="valueContactDetail",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_contributor: typing.Optional[Contributor] = pydantic.Field(
        alias="valueContributor",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_data_requirement: typing.Optional[DataRequirement] = pydantic.Field(
        alias="valueDataRequirement",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_expression: typing.Optional[Expression] = pydantic.Field(
        alias="valueExpression",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_parameter_definition: typing.Optional[ParameterDefinition] = pydantic.Field(
        alias="valueParameterDefinition",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_related_artifact: typing.Optional[RelatedArtifact] = pydantic.Field(
        alias="valueRelatedArtifact",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_trigger_definition: typing.Optional[TriggerDefinition] = pydantic.Field(
        alias="valueTriggerDefinition",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_usage_context: typing.Optional[UsageContext] = pydantic.Field(
        alias="valueUsageContext",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_dosage: typing.Optional[Dosage] = pydantic.Field(
        alias="valueDosage",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_meta: typing.Optional[Meta] = pydantic.Field(
        alias="valueMeta",
        description="Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
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


from .address import Address  # noqa: E402
from .age import Age  # noqa: E402
from .annotation import Annotation  # noqa: E402
from .attachment import Attachment  # noqa: E402
from .codeable_concept import CodeableConcept  # noqa: E402
from .coding import Coding  # noqa: E402
from .contact_detail import ContactDetail  # noqa: E402
from .contact_point import ContactPoint  # noqa: E402
from .contributor import Contributor  # noqa: E402
from .count import Count  # noqa: E402
from .data_requirement import DataRequirement  # noqa: E402
from .distance import Distance  # noqa: E402
from .dosage import Dosage  # noqa: E402
from .duration import Duration  # noqa: E402
from .expression import Expression  # noqa: E402
from .human_name import HumanName  # noqa: E402
from .identifier import Identifier  # noqa: E402
from .meta import Meta  # noqa: E402
from .money import Money  # noqa: E402
from .parameter_definition import ParameterDefinition  # noqa: E402
from .period import Period  # noqa: E402
from .quantity import Quantity  # noqa: E402
from .range import Range  # noqa: E402
from .ratio import Ratio  # noqa: E402
from .reference import Reference  # noqa: E402
from .related_artifact import RelatedArtifact  # noqa: E402
from .sampled_data import SampledData  # noqa: E402
from .signature import Signature  # noqa: E402
from .timing import Timing  # noqa: E402
from .trigger_definition import TriggerDefinition  # noqa: E402
from .usage_context import UsageContext  # noqa: E402

Extension.update_forward_refs()
