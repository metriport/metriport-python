# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CapabilityStatementInteractionCode(str, enum.Enum):
    """
    Coded identifier of the operation, supported by the system resource.
    """

    READ = "read"
    VREAD = "vread"
    UPDATE = "update"
    PATCH = "patch"
    DELETE = "delete"
    HISTORY_INSTANCE = "history-instance"
    HISTORY_TYPE = "history-type"
    CREATE = "create"
    SEARCH_TYPE = "search-type"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        vread: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        history_instance: typing.Callable[[], T_Result],
        history_type: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        search_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CapabilityStatementInteractionCode.READ:
            return read()
        if self is CapabilityStatementInteractionCode.VREAD:
            return vread()
        if self is CapabilityStatementInteractionCode.UPDATE:
            return update()
        if self is CapabilityStatementInteractionCode.PATCH:
            return patch()
        if self is CapabilityStatementInteractionCode.DELETE:
            return delete()
        if self is CapabilityStatementInteractionCode.HISTORY_INSTANCE:
            return history_instance()
        if self is CapabilityStatementInteractionCode.HISTORY_TYPE:
            return history_type()
        if self is CapabilityStatementInteractionCode.CREATE:
            return create()
        if self is CapabilityStatementInteractionCode.SEARCH_TYPE:
            return search_type()
