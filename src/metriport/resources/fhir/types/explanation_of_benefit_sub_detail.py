# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .decimal import Decimal
from .explanation_of_benefit_adjudication import ExplanationOfBenefitAdjudication
from .extension import Extension
from .money import Money
from .positive_int import PositiveInt
from .quantity import Quantity
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ExplanationOfBenefitSubDetail(pydantic.BaseModel):
    """
    This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
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
    sequence: typing.Optional[PositiveInt] = pydantic.Field(
        description="A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple items."
    )
    revenue: typing.Optional[CodeableConcept] = pydantic.Field(
        description="The type of revenue or cost center providing the product and/or service."
    )
    category: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Code to identify the general type of benefits under which products and services are provided."
    )
    product_or_service: CodeableConcept = pydantic.Field(
        alias="productOrService",
        description="When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the item.",
    )
    modifier: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Item typification or modifiers codes to convey additional context for the product or service."
    )
    program_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="programCode", description="Identifies the program under which this may be recovered."
    )
    quantity: typing.Optional[Quantity] = pydantic.Field(
        description="The number of repetitions of a service or product."
    )
    unit_price: typing.Optional[Money] = pydantic.Field(
        alias="unitPrice",
        description="If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the group.",
    )
    factor: typing.Optional[Decimal] = pydantic.Field(
        description="A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amount."
    )
    net: typing.Optional[Money] = pydantic.Field(
        description="The quantity times the unit price for an additional service or product or charge."
    )
    udi: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Unique Device Identifiers associated with this line item."
    )
    note_number: typing.Optional[typing.List[PositiveInt]] = pydantic.Field(
        alias="noteNumber",
        description="The numbers associated with notes below which apply to the adjudication of this item.",
    )
    adjudication: typing.Optional[typing.List[ExplanationOfBenefitAdjudication]] = pydantic.Field(
        description="The adjudication results."
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
