# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .identifier import Identifier
from .prod_characteristic import ProdCharacteristic
from .product_shelf_life import ProductShelfLife
from .quantity import Quantity
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicinalProductPackagedPackageItem(pydantic.BaseModel):
    """
    A medicinal product in a container or package.
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
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Including possibly Data Carrier Identifier."
    )
    type: CodeableConcept = pydantic.Field(description="The physical type of the container of the medicine.")
    quantity: Quantity = pydantic.Field(
        description="The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1."
    )
    material: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Material type of the package item."
    )
    alternate_material: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="alternateMaterial", description="A possible alternate material for the packaging."
    )
    device: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="A device accompanying a medicinal product."
    )
    manufactured_item: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="manufacturedItem", description="The manufactured item as contained in the packaged medicinal product."
    )
    package_item: typing.Optional[typing.List[MedicinalProductPackagedPackageItem]] = pydantic.Field(
        alias="packageItem", description="Allows containers within containers."
    )
    physical_characteristics: typing.Optional[ProdCharacteristic] = pydantic.Field(
        alias="physicalCharacteristics", description="Dimensions, color etc."
    )
    other_characteristics: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="otherCharacteristics", description="Other codeable characteristics."
    )
    shelf_life_storage: typing.Optional[typing.List[ProductShelfLife]] = pydantic.Field(
        alias="shelfLifeStorage", description="Shelf Life and storage information."
    )
    manufacturer: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Manufacturer of this Package Item."
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


MedicinalProductPackagedPackageItem.update_forward_refs()
