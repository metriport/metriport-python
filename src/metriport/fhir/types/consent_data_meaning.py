# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConsentDataMeaning(str, enum.Enum):
    """
    How the resource reference is interpreted when testing consent restrictions.
    """

    INSTANCE = "instance"
    RELATED = "related"
    DEPENDENTS = "dependents"
    AUTHOREDBY = "authoredby"

    def visit(
        self,
        instance: typing.Callable[[], T_Result],
        related: typing.Callable[[], T_Result],
        dependents: typing.Callable[[], T_Result],
        authoredby: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsentDataMeaning.INSTANCE:
            return instance()
        if self is ConsentDataMeaning.RELATED:
            return related()
        if self is ConsentDataMeaning.DEPENDENTS:
            return dependents()
        if self is ConsentDataMeaning.AUTHOREDBY:
            return authoredby()
