# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .account_coverage import AccountCoverage
from .account_guarantor import AccountGuarantor
from .account_status import AccountStatus
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Account(BaseResource):
    """
    A financial tool for tracking value accrued for a particular purpose. In the healthcare field, used to track charges for a patient, cost centers, etc.
    """

    resource_type: typing.Literal["Account"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Unique identifier used to reference the account. Might or might not be intended for human use (e.g. credit card number)."
    )
    status: typing.Optional[AccountStatus] = pydantic.Field(
        description="Indicates whether the account is presently used/usable or not."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Categorizes the account for reporting and searching purposes."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="Name used for the account when displaying it to humans in reports, etc."
    )
    subject: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Identifies the entity which incurs the expenses. While the immediate recipients of services or goods might be entities related to the subject, the expenses were ultimately incurred by the subject of the Account."
    )
    service_period: typing.Optional[Period] = pydantic.Field(
        alias="servicePeriod", description="The date range of services associated with this account."
    )
    coverage: typing.Optional[typing.List[AccountCoverage]] = pydantic.Field(
        description="The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account."
    )
    owner: typing.Optional[Reference] = pydantic.Field(
        description="Indicates the service area, hospital, department, etc. with responsibility for managing the Account."
    )
    description: typing.Optional[str] = pydantic.Field(
        description="Provides additional information about what the account tracks and how it is used."
    )
    guarantor: typing.Optional[typing.List[AccountGuarantor]] = pydantic.Field(
        description="The parties responsible for balancing the account if other payment options fall short."
    )
    part_of: typing.Optional[Reference] = pydantic.Field(alias="partOf", description="Reference to a parent Account.")

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
