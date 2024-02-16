# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StructureDefinitionStatus(str, enum.Enum):
    """
    The status of this structure definition. Enables tracking the life-cycle of the content.
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
        if self is StructureDefinitionStatus.DRAFT:
            return draft()
        if self is StructureDefinitionStatus.ACTIVE:
            return active()
        if self is StructureDefinitionStatus.RETIRED:
            return retired()
        if self is StructureDefinitionStatus.UNKNOWN:
            return unknown()
