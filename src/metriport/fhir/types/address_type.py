# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AddressType(str, enum.Enum):
    """
    Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.
    """

    POSTAL = "postal"
    PHYSICAL = "physical"
    BOTH = "both"

    def visit(
        self,
        postal: typing.Callable[[], T_Result],
        physical: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressType.POSTAL:
            return postal()
        if self is AddressType.PHYSICAL:
            return physical()
        if self is AddressType.BOTH:
            return both()
