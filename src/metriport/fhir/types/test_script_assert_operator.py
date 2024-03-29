# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TestScriptAssertOperator(str, enum.Enum):
    """
    The operator type defines the conditional behavior of the assert. If not defined, the default is equals.
    """

    EQUALS = "equals"
    NOT_EQUALS = "notEquals"
    IN = "in"
    NOT_IN = "notIn"
    GREATER_THAN = "greaterThan"
    LESS_THAN = "lessThan"
    EMPTY = "empty"
    NOT_EMPTY = "notEmpty"
    CONTAINS = "contains"
    NOT_CONTAINS = "notContains"
    EVAL = "eval"

    def visit(
        self,
        equals: typing.Callable[[], T_Result],
        not_equals: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        not_in: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
        not_empty: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        not_contains: typing.Callable[[], T_Result],
        eval: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestScriptAssertOperator.EQUALS:
            return equals()
        if self is TestScriptAssertOperator.NOT_EQUALS:
            return not_equals()
        if self is TestScriptAssertOperator.IN:
            return in_()
        if self is TestScriptAssertOperator.NOT_IN:
            return not_in()
        if self is TestScriptAssertOperator.GREATER_THAN:
            return greater_than()
        if self is TestScriptAssertOperator.LESS_THAN:
            return less_than()
        if self is TestScriptAssertOperator.EMPTY:
            return empty()
        if self is TestScriptAssertOperator.NOT_EMPTY:
            return not_empty()
        if self is TestScriptAssertOperator.CONTAINS:
            return contains()
        if self is TestScriptAssertOperator.NOT_CONTAINS:
            return not_contains()
        if self is TestScriptAssertOperator.EVAL:
            return eval()
