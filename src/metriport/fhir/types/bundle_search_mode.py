# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BundleSearchMode(str, enum.Enum):
    """
    Why this entry is in the result set - whether it's included as a match or because of an \_include requirement, or to convey information or warning information about the search process.
    """

    MATCH = "match"
    INCLUDE = "include"
    OUTCOME = "outcome"

    def visit(
        self,
        match: typing.Callable[[], T_Result],
        include: typing.Callable[[], T_Result],
        outcome: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BundleSearchMode.MATCH:
            return match()
        if self is BundleSearchMode.INCLUDE:
            return include()
        if self is BundleSearchMode.OUTCOME:
            return outcome()
