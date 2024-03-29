# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceUseStatementStatus(str, enum.Enum):
    """
    A code representing the patient or other source's judgment about the state of the device used that this statement is about. Generally this will be active or completed.
    """

    ACTIVE = "active"
    COMPLETED = "completed"
    ENTERED_IN_ERROR = "entered-in-error"
    INTENDED = "intended"
    STOPPED = "stopped"
    ON_HOLD = "on-hold"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
        intended: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        on_hold: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeviceUseStatementStatus.ACTIVE:
            return active()
        if self is DeviceUseStatementStatus.COMPLETED:
            return completed()
        if self is DeviceUseStatementStatus.ENTERED_IN_ERROR:
            return entered_in_error()
        if self is DeviceUseStatementStatus.INTENDED:
            return intended()
        if self is DeviceUseStatementStatus.STOPPED:
            return stopped()
        if self is DeviceUseStatementStatus.ON_HOLD:
            return on_hold()
