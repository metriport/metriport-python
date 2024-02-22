# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .base_resource import BaseResource
from .claim_response_add_item import ClaimResponseAddItem
from .claim_response_adjudication import ClaimResponseAdjudication
from .claim_response_error import ClaimResponseError
from .claim_response_insurance import ClaimResponseInsurance
from .claim_response_item import ClaimResponseItem
from .claim_response_payment import ClaimResponsePayment
from .claim_response_process_note import ClaimResponseProcessNote
from .claim_response_total import ClaimResponseTotal
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClaimResponse(BaseResource):
    """
    This resource provides the adjudication details from the processing of a Claim resource.
    """

    resource_type: typing.Literal["ClaimResponse"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="A unique identifier assigned to this claim response."
    )
    status: typing.Optional[Code] = pydantic.Field(description="The status of the resource instance.")
    type: CodeableConcept = pydantic.Field(
        description="A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty service."
    )
    sub_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="subType",
        description="A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty service.",
    )
    use: typing.Optional[Code] = pydantic.Field(
        description="A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the future."
    )
    patient: Reference = pydantic.Field(
        description="The party to whom the professional services and/or products have been supplied or are being considered and for whom actual for facast reimbursement is sought."
    )
    created: typing.Optional[DateTime] = pydantic.Field(description="The date this resource was created.")
    insurer: Reference = pydantic.Field(
        description="The party responsible for authorization, adjudication and reimbursement."
    )
    requestor: typing.Optional[Reference] = pydantic.Field(
        description="The provider which is responsible for the claim, predetermination or preauthorization."
    )
    request: typing.Optional[Reference] = pydantic.Field(description="Original request resource reference.")
    outcome: typing.Optional[Code] = pydantic.Field(
        description="The outcome of the claim, predetermination, or preauthorization processing."
    )
    disposition: typing.Optional[str] = pydantic.Field(
        description="A human readable description of the status of the adjudication."
    )
    pre_auth_ref: typing.Optional[str] = pydantic.Field(
        alias="preAuthRef",
        description="Reference from the Insurer which is used in later communications which refers to this adjudication.",
    )
    pre_auth_period: typing.Optional[Period] = pydantic.Field(
        alias="preAuthPeriod", description="The time frame during which this authorization is effective."
    )
    payee_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="payeeType", description="Type of Party to be reimbursed: subscriber, provider, other."
    )
    item: typing.Optional[typing.List[ClaimResponseItem]] = pydantic.Field(
        description="A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details."
    )
    add_item: typing.Optional[typing.List[ClaimResponseAddItem]] = pydantic.Field(
        alias="addItem", description="The first-tier service adjudications for payor added product or service lines."
    )
    adjudication: typing.Optional[typing.List[ClaimResponseAdjudication]] = pydantic.Field(
        description="The adjudication results which are presented at the header level rather than at the line-item or add-item levels."
    )
    total: typing.Optional[typing.List[ClaimResponseTotal]] = pydantic.Field(
        description="Categorized monetary totals for the adjudication."
    )
    payment: typing.Optional[ClaimResponsePayment] = pydantic.Field(
        description="Payment details for the adjudication of the claim."
    )
    funds_reserve: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="fundsReserve",
        description="A code, used only on a response to a preauthorization, to indicate whether the benefits payable have been reserved and for whom.",
    )
    form_code: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="formCode", description="A code for the form to be used for printing the content."
    )
    form: typing.Optional[Attachment] = pydantic.Field(
        description="The actual form, by reference or inclusion, for printing the content or an EOB."
    )
    process_note: typing.Optional[typing.List[ClaimResponseProcessNote]] = pydantic.Field(
        alias="processNote",
        description="A note that describes or explains adjudication results in a human readable form.",
    )
    communication_request: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="communicationRequest", description="Request for additional supporting or authorizing information."
    )
    insurance: typing.Optional[typing.List[ClaimResponseInsurance]] = pydantic.Field(
        description="Financial instruments for reimbursement for the health care products and services specified on the claim."
    )
    error: typing.Optional[typing.List[ClaimResponseError]] = pydantic.Field(
        description="Errors encountered during the processing of the adjudication."
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
