# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AdverseEventActuality(str, enum.Enum):
    """
    Whether the event actually happened, or just had the potential to. Note that this is independent of whether anyone was affected or harmed or how severely.
    """

    ACTUAL = "actual"
    POTENTIAL = "potential"

    def visit(self, actual: typing.Callable[[], T_Result], potential: typing.Callable[[], T_Result]) -> T_Result:
        if self is AdverseEventActuality.ACTUAL:
            return actual()
        if self is AdverseEventActuality.POTENTIAL:
            return potential()
