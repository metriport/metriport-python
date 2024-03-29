# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .coverage_eligibility_response_error import CoverageEligibilityResponseError
from .coverage_eligibility_response_insurance import CoverageEligibilityResponseInsurance
from .coverage_eligibility_response_outcome import CoverageEligibilityResponseOutcome
from .coverage_eligibility_response_purpose_item import CoverageEligibilityResponsePurposeItem
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CoverageEligibilityResponse(BaseResource):
    """
    This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
    """

    resource_type: typing.Literal["CoverageEligibilityResponse"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="A unique identifier assigned to this coverage eligiblity request."
    )
    status: typing.Optional[Code] = pydantic.Field(default=None, description="The status of the resource instance.")
    purpose: typing.Optional[typing.List[CoverageEligibilityResponsePurposeItem]] = pydantic.Field(
        default=None,
        description="Code to specify whether requesting: prior authorization requirements for some service categories or billing codes; benefits for coverages specified or discovered; discovery and return of coverages for the patient; and/or validation that the specified coverage is in-force at the date/period specified or 'now' if not specified.",
    )
    patient: Reference = pydantic.Field(
        description="The party who is the beneficiary of the supplied coverage and for whom eligibility is sought."
    )
    serviced_date: typing.Optional[str] = pydantic.Field(
        alias="servicedDate",
        default=None,
        description="The date or dates when the enclosed suite of services were performed or completed.",
    )
    serviced_period: typing.Optional[Period] = pydantic.Field(
        alias="servicedPeriod",
        default=None,
        description="The date or dates when the enclosed suite of services were performed or completed.",
    )
    created: typing.Optional[DateTime] = pydantic.Field(default=None, description="The date this resource was created.")
    requestor: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The provider which is responsible for the request."
    )
    request: Reference = pydantic.Field(description="Reference to the original request resource.")
    outcome: typing.Optional[CoverageEligibilityResponseOutcome] = pydantic.Field(
        default=None, description="The outcome of the request processing."
    )
    disposition: typing.Optional[str] = pydantic.Field(
        default=None, description="A human readable description of the status of the adjudication."
    )
    insurer: Reference = pydantic.Field(
        description="The Insurer who issued the coverage in question and is the author of the response."
    )
    insurance: typing.Optional[typing.List[CoverageEligibilityResponseInsurance]] = pydantic.Field(
        default=None, description="Financial instruments for reimbursement for the health care products and services."
    )
    pre_auth_ref: typing.Optional[str] = pydantic.Field(
        alias="preAuthRef",
        default=None,
        description="A reference from the Insurer to which these services pertain to be used on further communication and as proof that the request occurred.",
    )
    form: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="A code for the form to be used for printing the content."
    )
    error: typing.Optional[typing.List[CoverageEligibilityResponseError]] = pydantic.Field(
        default=None, description="Errors encountered during the processing of the request."
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
