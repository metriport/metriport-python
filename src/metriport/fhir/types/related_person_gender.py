# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RelatedPersonGender(str, enum.Enum):
    """
    Administrative Gender - the gender that the person is considered to have for administration and record keeping purposes.
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
        if self is RelatedPersonGender.MALE:
            return male()
        if self is RelatedPersonGender.FEMALE:
            return female()
        if self is RelatedPersonGender.OTHER:
            return other()
        if self is RelatedPersonGender.UNKNOWN:
            return unknown()