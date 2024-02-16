# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AgentStatus(str, enum.Enum):
    """
    The status of the agent.
    """

    ACTIVE = "active"
    OFF = "off"
    ERROR = "error"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        off: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentStatus.ACTIVE:
            return active()
        if self is AgentStatus.OFF:
            return off()
        if self is AgentStatus.ERROR:
            return error()