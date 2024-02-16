# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NamingSystemUniqueIdType(str, enum.Enum):
    """
    Identifies the unique identifier scheme used for this particular identifier.
    """

    OID = "oid"
    UUID = "uuid"
    URI = "uri"
    OTHER = "other"

    def visit(
        self,
        oid: typing.Callable[[], T_Result],
        uuid: typing.Callable[[], T_Result],
        uri: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NamingSystemUniqueIdType.OID:
            return oid()
        if self is NamingSystemUniqueIdType.UUID:
            return uuid()
        if self is NamingSystemUniqueIdType.URI:
            return uri()
        if self is NamingSystemUniqueIdType.OTHER:
            return other()