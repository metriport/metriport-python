# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .nutrition_order_administration import NutritionOrderAdministration
from .quantity import Quantity

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NutritionOrderEnteralFormula(pydantic.BaseModel):
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
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
    base_formula_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="baseFormulaType",
        default=None,
        description="The type of enteral or infant formula such as an adult standard formula with fiber or a soy-based infant formula.",
    )
    base_formula_product_name: typing.Optional[str] = pydantic.Field(
        alias="baseFormulaProductName",
        default=None,
        description='The product or brand name of the enteral or infant formula product such as "ACME Adult Standard Formula".',
    )
    additive_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="additiveType",
        default=None,
        description="Indicates the type of modular component such as protein, carbohydrate, fat or fiber to be provided in addition to or mixed with the base formula.",
    )
    additive_product_name: typing.Optional[str] = pydantic.Field(
        alias="additiveProductName",
        default=None,
        description="The product or brand name of the type of modular component to be added to the formula.",
    )
    caloric_density: typing.Optional[Quantity] = pydantic.Field(
        alias="caloricDensity",
        default=None,
        description="The amount of energy (calories) that the formula should provide per specified volume, typically per mL or fluid oz. For example, an infant may require a formula that provides 24 calories per fluid ounce or an adult may require an enteral formula that provides 1.5 calorie/mL.",
    )
    routeof_administration: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="routeofAdministration",
        default=None,
        description="The route or physiological path of administration into the patient's gastrointestinal tract for purposes of providing the formula feeding, e.g. nasogastric tube.",
    )
    administration: typing.Optional[typing.List[NutritionOrderAdministration]] = pydantic.Field(
        default=None,
        description="Formula administration instructions as structured data. This repeating structure allows for changing the administration rate or volume over time for both bolus and continuous feeding. An example of this would be an instruction to increase the rate of continuous feeding every 2 hours.",
    )
    max_volume_to_deliver: typing.Optional[Quantity] = pydantic.Field(
        alias="maxVolumeToDeliver",
        default=None,
        description="The maximum total quantity of formula that may be administered to a subject over the period of time, e.g. 1440 mL over 24 hours.",
    )
    administration_instruction: typing.Optional[str] = pydantic.Field(
        alias="administrationInstruction",
        default=None,
        description="Free text formula administration, feeding instructions or additional instructions or information.",
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
