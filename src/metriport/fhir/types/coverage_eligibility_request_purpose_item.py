# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CoverageEligibilityRequestPurposeItem(str, enum.Enum):
    AUTH_REQUIREMENTS = "auth-requirements"
    BENEFITS = "benefits"
    DISCOVERY = "discovery"
    VALIDATION = "validation"

    def visit(
        self,
        auth_requirements: typing.Callable[[], T_Result],
        benefits: typing.Callable[[], T_Result],
        discovery: typing.Callable[[], T_Result],
        validation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CoverageEligibilityRequestPurposeItem.AUTH_REQUIREMENTS:
            return auth_requirements()
        if self is CoverageEligibilityRequestPurposeItem.BENEFITS:
            return benefits()
        if self is CoverageEligibilityRequestPurposeItem.DISCOVERY:
            return discovery()
        if self is CoverageEligibilityRequestPurposeItem.VALIDATION:
            return validation()
