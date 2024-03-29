# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .prod_characteristic import ProdCharacteristic
from .quantity import Quantity
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicinalProductManufactured(BaseResource):
    """
    The manufactured item as contained in the packaged medicinal product.
    """

    resource_type: typing.Literal["MedicinalProductManufactured"] = pydantic.Field(alias="resourceType")
    manufactured_dose_form: CodeableConcept = pydantic.Field(
        alias="manufacturedDoseForm",
        description="Dose form as manufactured and before any transformation into the pharmaceutical product.",
    )
    unit_of_presentation: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="unitOfPresentation",
        default=None,
        description="The “real world” units in which the quantity of the manufactured item is described.",
    )
    quantity: Quantity = pydantic.Field(description='The quantity or "count number" of the manufactured item.')
    manufacturer: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description='Manufacturer of the item (Note that this should be named "manufacturer" but it currently causes technical issues).',
    )
    ingredient: typing.Optional[typing.List[Reference]] = pydantic.Field(default=None, description="Ingredient.")
    physical_characteristics: typing.Optional[ProdCharacteristic] = pydantic.Field(
        alias="physicalCharacteristics", default=None, description="Dimensions, color etc."
    )
    other_characteristics: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="otherCharacteristics", default=None, description="Other codeable characteristics."
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
