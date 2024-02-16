# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .medicinal_product_authorization_jurisdictional_authorization import (
    MedicinalProductAuthorizationJurisdictionalAuthorization,
)
from .medicinal_product_authorization_procedure import MedicinalProductAuthorizationProcedure
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicinalProductAuthorization(BaseResource):
    """
    The regulatory authorization of a medicinal product.
    """

    resource_type: typing_extensions.Literal["MedicinalProductAuthorization"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Business identifier for the marketing authorization, as assigned by a regulator."
    )
    subject: typing.Optional[Reference] = pydantic.Field(description="The medicinal product that is being authorized.")
    country: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="The country in which the marketing authorization has been granted."
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Jurisdiction within a country."
    )
    status: typing.Optional[CodeableConcept] = pydantic.Field(description="The status of the marketing authorization.")
    status_date: typing.Optional[DateTime] = pydantic.Field(
        alias="statusDate", description="The date at which the given status has become applicable."
    )
    restore_date: typing.Optional[DateTime] = pydantic.Field(
        alias="restoreDate",
        description="The date when a suspended the marketing or the marketing authorization of the product is anticipated to be restored.",
    )
    validity_period: typing.Optional[Period] = pydantic.Field(
        alias="validityPeriod",
        description="The beginning of the time period in which the marketing authorization is in the specific status shall be specified A complete date consisting of day, month and year shall be specified using the ISO 8601 date format.",
    )
    data_exclusivity_period: typing.Optional[Period] = pydantic.Field(
        alias="dataExclusivityPeriod",
        description="A period of time after authorization before generic product applicatiosn can be submitted.",
    )
    date_of_first_authorization: typing.Optional[DateTime] = pydantic.Field(
        alias="dateOfFirstAuthorization",
        description="The date when the first authorization was granted by a Medicines Regulatory Agency.",
    )
    international_birth_date: typing.Optional[DateTime] = pydantic.Field(
        alias="internationalBirthDate",
        description="Date of first marketing authorization for a company's new medicinal product in any country in the World.",
    )
    legal_basis: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="legalBasis", description="The legal framework against which this authorization is granted."
    )
    jurisdictional_authorization: typing.Optional[
        typing.List[MedicinalProductAuthorizationJurisdictionalAuthorization]
    ] = pydantic.Field(alias="jurisdictionalAuthorization", description="Authorization in areas within a country.")
    holder: typing.Optional[Reference] = pydantic.Field(description="Marketing Authorization Holder.")
    regulator: typing.Optional[Reference] = pydantic.Field(description="Medicines Regulatory Agency.")
    procedure: typing.Optional[MedicinalProductAuthorizationProcedure] = pydantic.Field(
        description="The regulatory procedure for granting or amending a marketing authorization."
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