# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .contact_point import ContactPoint
from .instant import Instant
from .subscription_channel import SubscriptionChannel
from .subscription_status import SubscriptionStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Subscription(BaseResource):
    """
    The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.
    """

    resource_type: typing.Literal["Subscription"] = pydantic.Field(alias="resourceType")
    status: typing.Optional[SubscriptionStatus] = pydantic.Field(
        default=None,
        description="The status of the subscription, which marks the server state for managing the subscription.",
    )
    contact: typing.Optional[typing.List[ContactPoint]] = pydantic.Field(
        default=None,
        description="Contact details for a human to contact about the subscription. The primary use of this for system administrator troubleshooting.",
    )
    end: typing.Optional[Instant] = pydantic.Field(
        default=None, description="The time for the server to turn the subscription off."
    )
    reason: typing.Optional[str] = pydantic.Field(
        default=None, description="A description of why this subscription is defined."
    )
    criteria: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The rules that the server should use to determine when to generate notifications for this subscription.",
    )
    error: typing.Optional[str] = pydantic.Field(
        default=None, description="A record of the last error that occurred when the server processed a notification."
    )
    channel: SubscriptionChannel = pydantic.Field(
        description="Details where to send notifications when resources are received that meet the criteria."
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
