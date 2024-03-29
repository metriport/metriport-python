# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CapabilityStatementRestMode(str, enum.Enum):
    """
    Identifies whether this portion of the statement is describing the ability to initiate or receive restful operations.
    """

    CLIENT = "client"
    SERVER = "server"

    def visit(self, client: typing.Callable[[], T_Result], server: typing.Callable[[], T_Result]) -> T_Result:
        if self is CapabilityStatementRestMode.CLIENT:
            return client()
        if self is CapabilityStatementRestMode.SERVER:
            return server()
