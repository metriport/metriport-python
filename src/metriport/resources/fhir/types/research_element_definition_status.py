# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResearchElementDefinitionStatus(str, enum.Enum):
    """
    The status of this research element definition. Enables tracking the life-cycle of the content.
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
        if self is ResearchElementDefinitionStatus.DRAFT:
            return draft()
        if self is ResearchElementDefinitionStatus.ACTIVE:
            return active()
        if self is ResearchElementDefinitionStatus.RETIRED:
            return retired()
        if self is ResearchElementDefinitionStatus.UNKNOWN:
            return unknown()
