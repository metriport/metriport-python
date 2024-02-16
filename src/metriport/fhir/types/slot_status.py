# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SlotStatus(str, enum.Enum):
    """
    busy | free | busy-unavailable | busy-tentative | entered-in-error.
    """

    BUSY = "busy"
    FREE = "free"
    BUSY_UNAVAILABLE = "busy-unavailable"
    BUSY_TENTATIVE = "busy-tentative"
    ENTERED_IN_ERROR = "entered-in-error"

    def visit(
        self,
        busy: typing.Callable[[], T_Result],
        free: typing.Callable[[], T_Result],
        busy_unavailable: typing.Callable[[], T_Result],
        busy_tentative: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SlotStatus.BUSY:
            return busy()
        if self is SlotStatus.FREE:
            return free()
        if self is SlotStatus.BUSY_UNAVAILABLE:
            return busy_unavailable()
        if self is SlotStatus.BUSY_TENTATIVE:
            return busy_tentative()
        if self is SlotStatus.ENTERED_IN_ERROR:
            return entered_in_error()