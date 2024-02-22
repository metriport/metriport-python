# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .insurance_plan_contact import InsurancePlanContact
from .insurance_plan_coverage import InsurancePlanCoverage
from .insurance_plan_plan import InsurancePlanPlan
from .insurance_plan_status import InsurancePlanStatus
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InsurancePlan(BaseResource):
    """
    Details of a Health Insurance product/plan provided by an organization.
    """

    resource_type: typing.Literal["InsurancePlan"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Business identifiers assigned to this health insurance product which remain constant as the resource is updated and propagates from server to server."
    )
    status: typing.Optional[InsurancePlanStatus] = pydantic.Field(
        description="The current state of the health insurance product."
    )
    type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="The kind of health insurance product."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="Official name of the health insurance product as designated by the owner."
    )
    alias: typing.Optional[typing.List[str]] = pydantic.Field(
        description="A list of alternate names that the product is known as, or was known as in the past."
    )
    period: typing.Optional[Period] = pydantic.Field(
        description="The period of time that the health insurance product is available."
    )
    owned_by: typing.Optional[Reference] = pydantic.Field(
        alias="ownedBy",
        description="The entity that is providing the health insurance product and underwriting the risk. This is typically an insurance carriers, other third-party payers, or health plan sponsors comonly referred to as 'payers'.",
    )
    administered_by: typing.Optional[Reference] = pydantic.Field(
        alias="administeredBy",
        description="An organization which administer other services such as underwriting, customer service and/or claims processing on behalf of the health insurance product owner.",
    )
    coverage_area: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="coverageArea", description="The geographic region in which a health insurance product's benefits apply."
    )
    contact: typing.Optional[typing.List[InsurancePlanContact]] = pydantic.Field(
        description="The contact for the health insurance product for a certain purpose."
    )
    endpoint: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The technical endpoints providing access to services operated for the health insurance product."
    )
    network: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Reference to the network included in the health insurance product."
    )
    coverage: typing.Optional[typing.List[InsurancePlanCoverage]] = pydantic.Field(
        description="Details about the coverage offered by the insurance product."
    )
    plan: typing.Optional[typing.List[InsurancePlanPlan]] = pydantic.Field(
        description="Details about an insurance plan."
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
