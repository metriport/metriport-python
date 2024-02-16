# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .money import Money
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PaymentNotice(BaseResource):
    """
    This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
    """

    resource_type: typing_extensions.Literal["PaymentNotice"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="A unique identifier assigned to this payment notice."
    )
    status: typing.Optional[Code] = pydantic.Field(description="The status of the resource instance.")
    request: typing.Optional[Reference] = pydantic.Field(
        description="Reference of resource for which payment is being made."
    )
    response: typing.Optional[Reference] = pydantic.Field(
        description="Reference of response to resource for which payment is being made."
    )
    created: typing.Optional[DateTime] = pydantic.Field(description="The date when this resource was created.")
    provider: typing.Optional[Reference] = pydantic.Field(
        description="The practitioner who is responsible for the services rendered to the patient."
    )
    payment: Reference = pydantic.Field(description="A reference to the payment which is the subject of this notice.")
    payment_date: typing.Optional[dt.date] = pydantic.Field(
        alias="paymentDate", description="The date when the above payment action occurred."
    )
    payee: typing.Optional[Reference] = pydantic.Field(
        description="The party who will receive or has received payment that is the subject of this notification."
    )
    recipient: Reference = pydantic.Field(description="The party who is notified of the payment status.")
    amount: Money = pydantic.Field(description="The amount sent to the payee.")
    payment_status: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="paymentStatus", description="A code indicating whether payment has been sent or cleared."
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