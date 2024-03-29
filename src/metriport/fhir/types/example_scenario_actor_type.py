# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExampleScenarioActorType(str, enum.Enum):
    """
    The type of actor - person or system.
    """

    PERSON = "person"
    ENTITY = "entity"

    def visit(self, person: typing.Callable[[], T_Result], entity: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExampleScenarioActorType.PERSON:
            return person()
        if self is ExampleScenarioActorType.ENTITY:
            return entity()
