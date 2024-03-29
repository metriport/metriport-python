# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubscriptionStatus(str, enum.Enum):
    """
    The status of the subscription, which marks the server state for managing the subscription.
    """

    REQUESTED = "requested"
    ACTIVE = "active"
    ERROR = "error"
    OFF = "off"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        off: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionStatus.REQUESTED:
            return requested()
        if self is SubscriptionStatus.ACTIVE:
            return active()
        if self is SubscriptionStatus.ERROR:
            return error()
        if self is SubscriptionStatus.OFF:
            return off()
