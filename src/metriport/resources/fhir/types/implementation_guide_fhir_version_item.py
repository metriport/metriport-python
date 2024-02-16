# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ImplementationGuideFhirVersionItem(str, enum.Enum):
    ZERO_01 = "0.01"
    ZERO_05 = "0.05"
    ZERO_06 = "0.06"
    ZERO_11 = "0.11"
    ZERO_080 = "0.0.80"
    ZERO_081 = "0.0.81"
    ZERO_082 = "0.0.82"
    ZERO_40 = "0.4.0"
    ZERO_50 = "0.5.0"
    ONE_00 = "1.0.0"
    ONE_01 = "1.0.1"
    ONE_02 = "1.0.2"
    ONE_10 = "1.1.0"
    ONE_40 = "1.4.0"
    ONE_60 = "1.6.0"
    ONE_80 = "1.8.0"
    THREE_00 = "3.0.0"
    THREE_01 = "3.0.1"
    THREE_30 = "3.3.0"
    THREE_50 = "3.5.0"
    FOUR_00 = "4.0.0"
    FOUR_01 = "4.0.1"

    def visit(
        self,
        zero_01: typing.Callable[[], T_Result],
        zero_05: typing.Callable[[], T_Result],
        zero_06: typing.Callable[[], T_Result],
        zero_11: typing.Callable[[], T_Result],
        zero_080: typing.Callable[[], T_Result],
        zero_081: typing.Callable[[], T_Result],
        zero_082: typing.Callable[[], T_Result],
        zero_40: typing.Callable[[], T_Result],
        zero_50: typing.Callable[[], T_Result],
        one_00: typing.Callable[[], T_Result],
        one_01: typing.Callable[[], T_Result],
        one_02: typing.Callable[[], T_Result],
        one_10: typing.Callable[[], T_Result],
        one_40: typing.Callable[[], T_Result],
        one_60: typing.Callable[[], T_Result],
        one_80: typing.Callable[[], T_Result],
        three_00: typing.Callable[[], T_Result],
        three_01: typing.Callable[[], T_Result],
        three_30: typing.Callable[[], T_Result],
        three_50: typing.Callable[[], T_Result],
        four_00: typing.Callable[[], T_Result],
        four_01: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImplementationGuideFhirVersionItem.ZERO_01:
            return zero_01()
        if self is ImplementationGuideFhirVersionItem.ZERO_05:
            return zero_05()
        if self is ImplementationGuideFhirVersionItem.ZERO_06:
            return zero_06()
        if self is ImplementationGuideFhirVersionItem.ZERO_11:
            return zero_11()
        if self is ImplementationGuideFhirVersionItem.ZERO_080:
            return zero_080()
        if self is ImplementationGuideFhirVersionItem.ZERO_081:
            return zero_081()
        if self is ImplementationGuideFhirVersionItem.ZERO_082:
            return zero_082()
        if self is ImplementationGuideFhirVersionItem.ZERO_40:
            return zero_40()
        if self is ImplementationGuideFhirVersionItem.ZERO_50:
            return zero_50()
        if self is ImplementationGuideFhirVersionItem.ONE_00:
            return one_00()
        if self is ImplementationGuideFhirVersionItem.ONE_01:
            return one_01()
        if self is ImplementationGuideFhirVersionItem.ONE_02:
            return one_02()
        if self is ImplementationGuideFhirVersionItem.ONE_10:
            return one_10()
        if self is ImplementationGuideFhirVersionItem.ONE_40:
            return one_40()
        if self is ImplementationGuideFhirVersionItem.ONE_60:
            return one_60()
        if self is ImplementationGuideFhirVersionItem.ONE_80:
            return one_80()
        if self is ImplementationGuideFhirVersionItem.THREE_00:
            return three_00()
        if self is ImplementationGuideFhirVersionItem.THREE_01:
            return three_01()
        if self is ImplementationGuideFhirVersionItem.THREE_30:
            return three_30()
        if self is ImplementationGuideFhirVersionItem.THREE_50:
            return three_50()
        if self is ImplementationGuideFhirVersionItem.FOUR_00:
            return four_00()
        if self is ImplementationGuideFhirVersionItem.FOUR_01:
            return four_01()
