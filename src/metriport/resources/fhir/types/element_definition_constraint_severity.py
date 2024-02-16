# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ElementDefinitionConstraintSeverity(str, enum.Enum):
    """
    Identifies the impact constraint violation has on the conformance of the instance.
    """

    ERROR = "error"
    WARNING = "warning"

    def visit(self, error: typing.Callable[[], T_Result], warning: typing.Callable[[], T_Result]) -> T_Result:
        if self is ElementDefinitionConstraintSeverity.ERROR:
            return error()
        if self is ElementDefinitionConstraintSeverity.WARNING:
            return warning()
