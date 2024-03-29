# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObservationDefinitionQualifiedIntervalGender(str, enum.Enum):
    """
    Sex of the population the range applies to.
    """

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    UNKNOWN = "unknown"

    def visit(
        self,
        male: typing.Callable[[], T_Result],
        female: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObservationDefinitionQualifiedIntervalGender.MALE:
            return male()
        if self is ObservationDefinitionQualifiedIntervalGender.FEMALE:
            return female()
        if self is ObservationDefinitionQualifiedIntervalGender.OTHER:
            return other()
        if self is ObservationDefinitionQualifiedIntervalGender.UNKNOWN:
            return unknown()
