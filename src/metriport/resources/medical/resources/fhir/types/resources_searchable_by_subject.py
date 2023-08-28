# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResourcesSearchableBySubject(str, enum.Enum):
    ADVERSE_EVENT = "AdverseEvent"
    TASK = "Task"

    def visit(self, adverse_event: typing.Callable[[], T_Result], task: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResourcesSearchableBySubject.ADVERSE_EVENT:
            return adverse_event()
        if self is ResourcesSearchableBySubject.TASK:
            return task()
