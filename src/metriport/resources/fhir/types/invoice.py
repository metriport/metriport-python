# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .invoice_line_item import InvoiceLineItem
from .invoice_participant import InvoiceParticipant
from .invoice_price_component import InvoicePriceComponent
from .invoice_status import InvoiceStatus
from .markdown import Markdown
from .money import Money
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Invoice(BaseResource):
    """
    Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    """

    resource_type: typing_extensions.Literal["Invoice"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifier of this Invoice, often used for reference in correspondence about this invoice or for tracking of payments."
    )
    status: typing.Optional[InvoiceStatus] = pydantic.Field(description="The current state of the Invoice.")
    cancelled_reason: typing.Optional[str] = pydantic.Field(
        alias="cancelledReason",
        description="In case of Invoice cancellation a reason must be given (entered in error, superseded by corrected invoice etc.).",
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Type of Invoice depending on domain, realm an usage (e.g. internal/external, dental, preliminary)."
    )
    subject: typing.Optional[Reference] = pydantic.Field(
        description="The individual or set of individuals receiving the goods and services billed in this invoice."
    )
    recipient: typing.Optional[Reference] = pydantic.Field(
        description="The individual or Organization responsible for balancing of this invoice."
    )
    date: typing.Optional[DateTime] = pydantic.Field(description="Date/time(s) of when this Invoice was posted.")
    participant: typing.Optional[typing.List[InvoiceParticipant]] = pydantic.Field(
        description="Indicates who or what performed or participated in the charged service."
    )
    issuer: typing.Optional[Reference] = pydantic.Field(description="The organizationissuing the Invoice.")
    account: typing.Optional[Reference] = pydantic.Field(
        description="Account which is supposed to be balanced with this Invoice."
    )
    line_item: typing.Optional[typing.List[InvoiceLineItem]] = pydantic.Field(
        alias="lineItem",
        description="Each line item represents one charge for goods and services rendered. Details such as date, code and amount are found in the referenced ChargeItem resource.",
    )
    total_price_component: typing.Optional[typing.List[InvoicePriceComponent]] = pydantic.Field(
        alias="totalPriceComponent",
        description="The total amount for the Invoice may be calculated as the sum of the line items with surcharges/deductions that apply in certain conditions. The priceComponent element can be used to offer transparency to the recipient of the Invoice of how the total price was calculated.",
    )
    total_net: typing.Optional[Money] = pydantic.Field(alias="totalNet", description="Invoice total , taxes excluded.")
    total_gross: typing.Optional[Money] = pydantic.Field(alias="totalGross", description="Invoice total, tax included.")
    payment_terms: typing.Optional[Markdown] = pydantic.Field(
        alias="paymentTerms",
        description="Payment details such as banking details, period of payment, deductibles, methods of payment.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Comments made about the invoice by the issuer, subject, or other participants."
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
