# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .catalog_entry_related_entry import CatalogEntryRelatedEntry
from .catalog_entry_status import CatalogEntryStatus
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CatalogEntry(BaseResource):
    """
    Catalog entries are wrappers that contextualize items included in a catalog.
    """

    resource_type: typing.Literal["CatalogEntry"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Used in supporting different identifiers for the same product, e.g. manufacturer code and retailer code.",
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="The type of item - medication, device, service, protocol or other."
    )
    orderable: typing.Optional[bool] = pydantic.Field(
        default=None, description="Whether the entry represents an orderable item."
    )
    referenced_item: Reference = pydantic.Field(
        alias="referencedItem", description="The item in a catalog or definition."
    )
    additional_identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        alias="additionalIdentifier",
        default=None,
        description="Used in supporting related concepts, e.g. NDC to RxNorm.",
    )
    classification: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="Classes of devices, or ATC for medication."
    )
    status: typing.Optional[CatalogEntryStatus] = pydantic.Field(
        default=None,
        description="Used to support catalog exchange even for unsupported products, e.g. getting list of medications even if not prescribable.",
    )
    validity_period: typing.Optional[Period] = pydantic.Field(
        alias="validityPeriod",
        default=None,
        description="The time period in which this catalog entry is expected to be active.",
    )
    valid_to: typing.Optional[DateTime] = pydantic.Field(
        alias="validTo", default=None, description="The date until which this catalog entry is expected to be active."
    )
    last_updated: typing.Optional[DateTime] = pydantic.Field(
        alias="lastUpdated",
        default=None,
        description="Typically date of issue is different from the beginning of the validity. This can be used to see when an item was last updated.",
    )
    additional_characteristic: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="additionalCharacteristic",
        default=None,
        description="Used for examplefor Out of Formulary, or any specifics.",
    )
    additional_classification: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="additionalClassification", default=None, description="User for example for ATC classification, or."
    )
    related_entry: typing.Optional[typing.List[CatalogEntryRelatedEntry]] = pydantic.Field(
        alias="relatedEntry",
        default=None,
        description="Used for example, to point to a substance, or to a device used to administer a medication.",
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
