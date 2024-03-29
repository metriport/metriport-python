# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TerminologyCapabilitiesCodeSearch(str, enum.Enum):
    """
    The degree to which the server supports the code search parameter on ValueSet, if it is supported.
    """

    EXPLICIT = "explicit"
    ALL = "all"

    def visit(self, explicit: typing.Callable[[], T_Result], all: typing.Callable[[], T_Result]) -> T_Result:
        if self is TerminologyCapabilitiesCodeSearch.EXPLICIT:
            return explicit()
        if self is TerminologyCapabilitiesCodeSearch.ALL:
            return all()
