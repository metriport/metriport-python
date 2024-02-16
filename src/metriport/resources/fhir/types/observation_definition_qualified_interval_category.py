# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObservationDefinitionQualifiedIntervalCategory(str, enum.Enum):
    """
    The category of interval of values for continuous or ordinal observations conforming to this ObservationDefinition.
    """

    REFERENCE = "reference"
    CRITICAL = "critical"
    ABSOLUTE = "absolute"

    def visit(
        self,
        reference: typing.Callable[[], T_Result],
        critical: typing.Callable[[], T_Result],
        absolute: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObservationDefinitionQualifiedIntervalCategory.REFERENCE:
            return reference()
        if self is ObservationDefinitionQualifiedIntervalCategory.CRITICAL:
            return critical()
        if self is ObservationDefinitionQualifiedIntervalCategory.ABSOLUTE:
            return absolute()
