# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .nutrition_order_enteral_formula import NutritionOrderEnteralFormula
from .nutrition_order_oral_diet import NutritionOrderOralDiet
from .nutrition_order_supplement import NutritionOrderSupplement
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NutritionOrder(BaseResource):
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    """

    resource_type: typing.Literal["NutritionOrder"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifiers assigned to this order by the order sender or by the order receiver."
    )
    instantiates_canonical: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="instantiatesCanonical",
        description="The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this NutritionOrder.",
    )
    instantiates_uri: typing.Optional[typing.List[Uri]] = pydantic.Field(
        alias="instantiatesUri",
        description="The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this NutritionOrder.",
    )
    instantiates: typing.Optional[typing.List[Uri]] = pydantic.Field(
        description="The URL pointing to a protocol, guideline, orderset or other definition that is adhered to in whole or in part by this NutritionOrder."
    )
    status: typing.Optional[Code] = pydantic.Field(description="The workflow status of the nutrition order/request.")
    intent: typing.Optional[Code] = pydantic.Field(
        description="Indicates the level of authority/intentionality associated with the NutrionOrder and where the request fits into the workflow chain."
    )
    patient: Reference = pydantic.Field(
        description="The person (patient) who needs the nutrition order for an oral diet, nutritional supplement and/or enteral or formula feeding."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        description="An encounter that provides additional information about the healthcare context in which this request is made."
    )
    date_time: typing.Optional[DateTime] = pydantic.Field(
        alias="dateTime", description="The date and time that this nutrition order was requested."
    )
    orderer: typing.Optional[Reference] = pydantic.Field(
        description="The practitioner that holds legal responsibility for ordering the diet, nutritional supplement, or formula feedings."
    )
    allergy_intolerance: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="allergyIntolerance",
        description="A link to a record of allergies or intolerances which should be included in the nutrition order.",
    )
    food_preference_modifier: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="foodPreferenceModifier",
        description="This modifier is used to convey order-specific modifiers about the type of food that should be given. These can be derived from patient allergies, intolerances, or preferences such as Halal, Vegan or Kosher. This modifier applies to the entire nutrition order inclusive of the oral diet, nutritional supplements and enteral formula feedings.",
    )
    exclude_food_modifier: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="excludeFoodModifier",
        description="This modifier is used to convey Order-specific modifier about the type of oral food or oral fluids that should not be given. These can be derived from patient allergies, intolerances, or preferences such as No Red Meat, No Soy or No Wheat or Gluten-Free. While it should not be necessary to repeat allergy or intolerance information captured in the referenced AllergyIntolerance resource in the excludeFoodModifier, this element may be used to convey additional specificity related to foods that should be eliminated from the patient’s diet for any reason. This modifier applies to the entire nutrition order inclusive of the oral diet, nutritional supplements and enteral formula feedings.",
    )
    oral_diet: typing.Optional[NutritionOrderOralDiet] = pydantic.Field(
        alias="oralDiet", description="Diet given orally in contrast to enteral (tube) feeding."
    )
    supplement: typing.Optional[typing.List[NutritionOrderSupplement]] = pydantic.Field(
        description="Oral nutritional products given in order to add further nutritional value to the patient's diet."
    )
    enteral_formula: typing.Optional[NutritionOrderEnteralFormula] = pydantic.Field(
        alias="enteralFormula",
        description="Feeding provided through the gastrointestinal tract via a tube, catheter, or stoma that delivers nutrition distal to the oral cavity.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Comments made about the {{title}} by the requester, performer, subject or other participants."
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
