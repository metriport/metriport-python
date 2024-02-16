# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StructureDefinitionContextType(str, enum.Enum):
    """
    Defines how to interpret the expression that defines what the context of the extension is.
    """

    FHIRPATH = "fhirpath"
    ELEMENT = "element"
    EXTENSION = "extension"

    def visit(
        self,
        fhirpath: typing.Callable[[], T_Result],
        element: typing.Callable[[], T_Result],
        extension: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StructureDefinitionContextType.FHIRPATH:
            return fhirpath()
        if self is StructureDefinitionContextType.ELEMENT:
            return element()
        if self is StructureDefinitionContextType.EXTENSION:
            return extension()