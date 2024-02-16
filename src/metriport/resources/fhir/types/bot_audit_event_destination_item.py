# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BotAuditEventDestinationItem(str, enum.Enum):
    LOG = "log"
    RESOURCE = "resource"

    def visit(self, log: typing.Callable[[], T_Result], resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is BotAuditEventDestinationItem.LOG:
            return log()
        if self is BotAuditEventDestinationItem.RESOURCE:
            return resource()
