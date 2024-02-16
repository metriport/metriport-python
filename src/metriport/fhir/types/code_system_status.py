# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CodeSystemStatus(str, enum.Enum):
    """
    The date (and optionally time) when the code system resource was created or revised.
    """

    DRAFT = "draft"
    ACTIVE = "active"
    RETIRED = "retired"
    UNKNOWN = "unknown"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CodeSystemStatus.DRAFT:
            return draft()
        if self is CodeSystemStatus.ACTIVE:
            return active()
        if self is CodeSystemStatus.RETIRED:
            return retired()
        if self is CodeSystemStatus.UNKNOWN:
            return unknown()