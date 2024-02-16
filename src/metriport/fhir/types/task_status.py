# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskStatus(str, enum.Enum):
    """
    The current status of the task.
    """

    DRAFT = "draft"
    REQUESTED = "requested"
    RECEIVED = "received"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    READY = "ready"
    CANCELLED = "cancelled"
    IN_PROGRESS = "in-progress"
    ON_HOLD = "on-hold"
    FAILED = "failed"
    COMPLETED = "completed"
    ENTERED_IN_ERROR = "entered-in-error"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        requested: typing.Callable[[], T_Result],
        received: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        on_hold: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskStatus.DRAFT:
            return draft()
        if self is TaskStatus.REQUESTED:
            return requested()
        if self is TaskStatus.RECEIVED:
            return received()
        if self is TaskStatus.ACCEPTED:
            return accepted()
        if self is TaskStatus.REJECTED:
            return rejected()
        if self is TaskStatus.READY:
            return ready()
        if self is TaskStatus.CANCELLED:
            return cancelled()
        if self is TaskStatus.IN_PROGRESS:
            return in_progress()
        if self is TaskStatus.ON_HOLD:
            return on_hold()
        if self is TaskStatus.FAILED:
            return failed()
        if self is TaskStatus.COMPLETED:
            return completed()
        if self is TaskStatus.ENTERED_IN_ERROR:
            return entered_in_error()