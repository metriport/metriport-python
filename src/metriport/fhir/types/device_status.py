# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceStatus(str, enum.Enum):
    """
    Status of the Device availability.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    ENTERED_IN_ERROR = "entered-in-error"
    UNKNOWN = "unknown"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeviceStatus.ACTIVE:
            return active()
        if self is DeviceStatus.INACTIVE:
            return inactive()
        if self is DeviceStatus.ENTERED_IN_ERROR:
            return entered_in_error()
        if self is DeviceStatus.UNKNOWN:
            return unknown()
