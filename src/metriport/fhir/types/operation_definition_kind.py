# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OperationDefinitionKind(str, enum.Enum):
    """
    Whether this is an operation or a named query.
    """

    OPERATION = "operation"
    QUERY = "query"

    def visit(self, operation: typing.Callable[[], T_Result], query: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperationDefinitionKind.OPERATION:
            return operation()
        if self is OperationDefinitionKind.QUERY:
            return query()
