# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HumanNameUse(str, enum.Enum):
    """
    Identifies the purpose for this name.
    """

    USUAL = "usual"
    OFFICIAL = "official"
    TEMP = "temp"
    NICKNAME = "nickname"
    ANONYMOUS = "anonymous"
    OLD = "old"
    MAIDEN = "maiden"

    def visit(
        self,
        usual: typing.Callable[[], T_Result],
        official: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        nickname: typing.Callable[[], T_Result],
        anonymous: typing.Callable[[], T_Result],
        old: typing.Callable[[], T_Result],
        maiden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HumanNameUse.USUAL:
            return usual()
        if self is HumanNameUse.OFFICIAL:
            return official()
        if self is HumanNameUse.TEMP:
            return temp()
        if self is HumanNameUse.NICKNAME:
            return nickname()
        if self is HumanNameUse.ANONYMOUS:
            return anonymous()
        if self is HumanNameUse.OLD:
            return old()
        if self is HumanNameUse.MAIDEN:
            return maiden()
