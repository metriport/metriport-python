# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TestReportResult(str, enum.Enum):
    """
    The overall result from the execution of the TestScript.
    """

    PASS = "pass"
    FAIL = "fail"
    PENDING = "pending"

    def visit(
        self,
        pass_: typing.Callable[[], T_Result],
        fail: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestReportResult.PASS:
            return pass_()
        if self is TestReportResult.FAIL:
            return fail()
        if self is TestReportResult.PENDING:
            return pending()