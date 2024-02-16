# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CapabilityStatementDocumentMode(str, enum.Enum):
    """
    Mode of this document declaration - whether an application is a producer or consumer.
    """

    PRODUCER = "producer"
    CONSUMER = "consumer"

    def visit(self, producer: typing.Callable[[], T_Result], consumer: typing.Callable[[], T_Result]) -> T_Result:
        if self is CapabilityStatementDocumentMode.PRODUCER:
            return producer()
        if self is CapabilityStatementDocumentMode.CONSUMER:
            return consumer()