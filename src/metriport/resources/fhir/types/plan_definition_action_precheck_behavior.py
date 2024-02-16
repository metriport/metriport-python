# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PlanDefinitionActionPrecheckBehavior(str, enum.Enum):
    """
    Defines whether the action should usually be preselected.
    """

    YES = "yes"
    NO = "no"

    def visit(self, yes: typing.Callable[[], T_Result], no: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlanDefinitionActionPrecheckBehavior.YES:
            return yes()
        if self is PlanDefinitionActionPrecheckBehavior.NO:
            return no()
