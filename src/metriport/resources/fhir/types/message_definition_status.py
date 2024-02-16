# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MessageDefinitionStatus(str, enum.Enum):
    """
    The status of this message definition. Enables tracking the life-cycle of the content.
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
        if self is MessageDefinitionStatus.DRAFT:
            return draft()
        if self is MessageDefinitionStatus.ACTIVE:
            return active()
        if self is MessageDefinitionStatus.RETIRED:
            return retired()
        if self is MessageDefinitionStatus.UNKNOWN:
            return unknown()
