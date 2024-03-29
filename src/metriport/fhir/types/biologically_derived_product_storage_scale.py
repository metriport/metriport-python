# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BiologicallyDerivedProductStorageScale(str, enum.Enum):
    """
    Temperature scale used.
    """

    FARENHEIT = "farenheit"
    CELSIUS = "celsius"
    KELVIN = "kelvin"

    def visit(
        self,
        farenheit: typing.Callable[[], T_Result],
        celsius: typing.Callable[[], T_Result],
        kelvin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BiologicallyDerivedProductStorageScale.FARENHEIT:
            return farenheit()
        if self is BiologicallyDerivedProductStorageScale.CELSIUS:
            return celsius()
        if self is BiologicallyDerivedProductStorageScale.KELVIN:
            return kelvin()
