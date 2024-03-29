# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CodeSystemPropertyType(str, enum.Enum):
    """
    The type of the property value. Properties of type "code" contain a code defined by the code system (e.g. a reference to another defined concept).
    """

    CODE = "code"
    CODING = "Coding"
    STRING = "string"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    DATE_TIME = "dateTime"
    DECIMAL = "decimal"

    def visit(
        self,
        code: typing.Callable[[], T_Result],
        coding: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        date_time: typing.Callable[[], T_Result],
        decimal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CodeSystemPropertyType.CODE:
            return code()
        if self is CodeSystemPropertyType.CODING:
            return coding()
        if self is CodeSystemPropertyType.STRING:
            return string()
        if self is CodeSystemPropertyType.INTEGER:
            return integer()
        if self is CodeSystemPropertyType.BOOLEAN:
            return boolean()
        if self is CodeSystemPropertyType.DATE_TIME:
            return date_time()
        if self is CodeSystemPropertyType.DECIMAL:
            return decimal()
