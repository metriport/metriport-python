# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .marketing_status import MarketingStatus
from .medicinal_product_packaged_batch_identifier import MedicinalProductPackagedBatchIdentifier
from .medicinal_product_packaged_package_item import MedicinalProductPackagedPackageItem
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicinalProductPackaged(BaseResource):
    """
    A medicinal product in a container or package.
    """

    resource_type: typing.Literal["MedicinalProductPackaged"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(description="Unique identifier.")
    subject: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The product with this is a pack for."
    )
    description: typing.Optional[str] = pydantic.Field(description="Textual description.")
    legal_status_of_supply: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="legalStatusOfSupply",
        description="The legal status of supply of the medicinal product as classified by the regulator.",
    )
    marketing_status: typing.Optional[typing.List[MarketingStatus]] = pydantic.Field(
        alias="marketingStatus", description="Marketing information."
    )
    marketing_authorization: typing.Optional[Reference] = pydantic.Field(
        alias="marketingAuthorization", description="Manufacturer of this Package Item."
    )
    manufacturer: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Manufacturer of this Package Item."
    )
    batch_identifier: typing.Optional[typing.List[MedicinalProductPackagedBatchIdentifier]] = pydantic.Field(
        alias="batchIdentifier", description="Batch numbering."
    )
    package_item: typing.List[MedicinalProductPackagedPackageItem] = pydantic.Field(
        alias="packageItem",
        description="A packaging item, as a contained for medicine, possibly with other packaging items within.",
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
