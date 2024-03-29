# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .biologically_derived_product_collection import BiologicallyDerivedProductCollection
from .biologically_derived_product_manipulation import BiologicallyDerivedProductManipulation
from .biologically_derived_product_processing import BiologicallyDerivedProductProcessing
from .biologically_derived_product_product_category import BiologicallyDerivedProductProductCategory
from .biologically_derived_product_status import BiologicallyDerivedProductStatus
from .biologically_derived_product_storage import BiologicallyDerivedProductStorage
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BiologicallyDerivedProduct(BaseResource):
    """
    A material substance originating from a biological entity intended to be transplanted or infused into another (possibly the same) biological entity.
    """

    resource_type: typing.Literal["BiologicallyDerivedProduct"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="This records identifiers associated with this biologically derived product instance that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation).",
    )
    product_category: typing.Optional[BiologicallyDerivedProductProductCategory] = pydantic.Field(
        alias="productCategory", default=None, description="Broad category of this product."
    )
    product_code: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="productCode",
        default=None,
        description="A code that identifies the kind of this biologically derived product (SNOMED Ctcode).",
    )
    status: typing.Optional[BiologicallyDerivedProductStatus] = pydantic.Field(
        default=None, description="Whether the product is currently available."
    )
    request: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="Procedure request to obtain this biologically derived product."
    )
    quantity: typing.Optional[int] = pydantic.Field(
        default=None, description="Number of discrete units within this product."
    )
    parent: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="Parent product (if any)."
    )
    collection: typing.Optional[BiologicallyDerivedProductCollection] = pydantic.Field(
        default=None, description="How this product was collected."
    )
    processing: typing.Optional[typing.List[BiologicallyDerivedProductProcessing]] = pydantic.Field(
        default=None,
        description="Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cells.",
    )
    manipulation: typing.Optional[BiologicallyDerivedProductManipulation] = pydantic.Field(
        default=None,
        description="Any manipulation of product post-collection that is intended to alter the product. For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusion.",
    )
    storage: typing.Optional[typing.List[BiologicallyDerivedProductStorage]] = pydantic.Field(
        default=None, description="Product storage."
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
