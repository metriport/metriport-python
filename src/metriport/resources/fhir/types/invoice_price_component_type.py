# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoicePriceComponentType(str, enum.Enum):
    """
    This code identifies the type of the component.
    """

    BASE = "base"
    SURCHARGE = "surcharge"
    DEDUCTION = "deduction"
    DISCOUNT = "discount"
    TAX = "tax"
    INFORMATIONAL = "informational"

    def visit(
        self,
        base: typing.Callable[[], T_Result],
        surcharge: typing.Callable[[], T_Result],
        deduction: typing.Callable[[], T_Result],
        discount: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
        informational: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoicePriceComponentType.BASE:
            return base()
        if self is InvoicePriceComponentType.SURCHARGE:
            return surcharge()
        if self is InvoicePriceComponentType.DEDUCTION:
            return deduction()
        if self is InvoicePriceComponentType.DISCOUNT:
            return discount()
        if self is InvoicePriceComponentType.TAX:
            return tax()
        if self is InvoicePriceComponentType.INFORMATIONAL:
            return informational()
