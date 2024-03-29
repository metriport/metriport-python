# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CoverageEligibilityResponseOutcome(str, enum.Enum):
    """
    The outcome of the request processing.
    """

    QUEUED = "queued"
    COMPLETE = "complete"
    ERROR = "error"
    PARTIAL = "partial"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CoverageEligibilityResponseOutcome.QUEUED:
            return queued()
        if self is CoverageEligibilityResponseOutcome.COMPLETE:
            return complete()
        if self is CoverageEligibilityResponseOutcome.ERROR:
            return error()
        if self is CoverageEligibilityResponseOutcome.PARTIAL:
            return partial()
