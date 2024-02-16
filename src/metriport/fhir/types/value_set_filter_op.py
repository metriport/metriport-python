# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ValueSetFilterOp(str, enum.Enum):
    """
    The kind of operation to perform as a part of the filter criteria.
    """

    EQUALS = "="
    IS_A = "is-a"
    DESCENDENT_OF = "descendent-of"
    IS_NOT_A = "is-not-a"
    REGEX = "regex"
    IN = "in"
    NOT_IN = "not-in"
    GENERALIZES = "generalizes"
    EXISTS = "exists"

    def visit(
        self,
        equals: typing.Callable[[], T_Result],
        is_a: typing.Callable[[], T_Result],
        descendent_of: typing.Callable[[], T_Result],
        is_not_a: typing.Callable[[], T_Result],
        regex: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        not_in: typing.Callable[[], T_Result],
        generalizes: typing.Callable[[], T_Result],
        exists: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueSetFilterOp.EQUALS:
            return equals()
        if self is ValueSetFilterOp.IS_A:
            return is_a()
        if self is ValueSetFilterOp.DESCENDENT_OF:
            return descendent_of()
        if self is ValueSetFilterOp.IS_NOT_A:
            return is_not_a()
        if self is ValueSetFilterOp.REGEX:
            return regex()
        if self is ValueSetFilterOp.IN:
            return in_()
        if self is ValueSetFilterOp.NOT_IN:
            return not_in()
        if self is ValueSetFilterOp.GENERALIZES:
            return generalizes()
        if self is ValueSetFilterOp.EXISTS:
            return exists()