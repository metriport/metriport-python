# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CodeSystemHierarchyMeaning(str, enum.Enum):
    """
    The meaning of the hierarchy of concepts as represented in this resource.
    """

    GROUPED_BY = "grouped-by"
    IS_A = "is-a"
    PART_OF = "part-of"
    CLASSIFIED_WITH = "classified-with"

    def visit(
        self,
        grouped_by: typing.Callable[[], T_Result],
        is_a: typing.Callable[[], T_Result],
        part_of: typing.Callable[[], T_Result],
        classified_with: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CodeSystemHierarchyMeaning.GROUPED_BY:
            return grouped_by()
        if self is CodeSystemHierarchyMeaning.IS_A:
            return is_a()
        if self is CodeSystemHierarchyMeaning.PART_OF:
            return part_of()
        if self is CodeSystemHierarchyMeaning.CLASSIFIED_WITH:
            return classified_with()