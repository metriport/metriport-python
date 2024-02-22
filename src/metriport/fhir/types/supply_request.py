# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .reference import Reference
from .supply_request_parameter import SupplyRequestParameter
from .supply_request_status import SupplyRequestStatus
from .timing import Timing

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SupplyRequest(BaseResource):
    """
    A record of a request for a medication, substance or device used in the healthcare setting.
    """

    resource_type: typing.Literal["SupplyRequest"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Business identifiers assigned to this SupplyRequest by the author and/or other systems. These identifiers remain constant as the resource is updated and propagates from server to server.",
    )
    status: typing.Optional[SupplyRequestStatus] = pydantic.Field(
        default=None, description="Status of the supply request."
    )
    category: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="Category of supply, e.g. central, non-stock, etc. This is used to support work flows associated with the supply process.",
    )
    priority: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="Indicates how quickly this SupplyRequest should be addressed with respect to other requests.",
    )
    item_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="itemCodeableConcept",
        default=None,
        description="The item that is requested to be supplied. This is either a link to a resource representing the details of the item or a code that identifies the item from a known list.",
    )
    item_reference: typing.Optional[Reference] = pydantic.Field(
        alias="itemReference",
        default=None,
        description="The item that is requested to be supplied. This is either a link to a resource representing the details of the item or a code that identifies the item from a known list.",
    )
    quantity: Quantity = pydantic.Field(description="The amount that is being ordered of the indicated item.")
    parameter: typing.Optional[typing.List[SupplyRequestParameter]] = pydantic.Field(
        default=None,
        description="Specific parameters for the ordered item. For example, the size of the indicated item.",
    )
    occurrence_date_time: typing.Optional[str] = pydantic.Field(
        alias="occurrenceDateTime", default=None, description="When the request should be fulfilled."
    )
    occurrence_period: typing.Optional[Period] = pydantic.Field(
        alias="occurrencePeriod", default=None, description="When the request should be fulfilled."
    )
    occurrence_timing: typing.Optional[Timing] = pydantic.Field(
        alias="occurrenceTiming", default=None, description="When the request should be fulfilled."
    )
    authored_on: typing.Optional[DateTime] = pydantic.Field(
        alias="authoredOn", default=None, description="When the request was made."
    )
    requester: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The device, practitioner, etc. who initiated the request."
    )
    supplier: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="Who is intended to fulfill the request."
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode", default=None, description="The reason why the supply item was requested."
    )
    reason_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="reasonReference", default=None, description="The reason why the supply item was requested."
    )
    deliver_from: typing.Optional[Reference] = pydantic.Field(
        alias="deliverFrom", default=None, description="Where the supply is expected to come from."
    )
    deliver_to: typing.Optional[Reference] = pydantic.Field(
        alias="deliverTo", default=None, description="Where the supply is destined to go."
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
