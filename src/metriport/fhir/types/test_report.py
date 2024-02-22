# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .date_time import DateTime
from .decimal import Decimal
from .identifier import Identifier
from .reference import Reference
from .test_report_participant import TestReportParticipant
from .test_report_result import TestReportResult
from .test_report_setup import TestReportSetup
from .test_report_status import TestReportStatus
from .test_report_teardown import TestReportTeardown
from .test_report_test import TestReportTest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestReport(BaseResource):
    """
    A summary of information based on the results of executing a TestScript.
    """

    resource_type: typing.Literal["TestReport"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[Identifier] = pydantic.Field(
        description="Identifier for the TestScript assigned for external purposes outside the context of FHIR."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A free text natural language name identifying the executed TestScript."
    )
    status: typing.Optional[TestReportStatus] = pydantic.Field(description="The current state of this test report.")
    test_script: Reference = pydantic.Field(
        alias="testScript",
        description="Ideally this is an absolute URL that is used to identify the version-specific TestScript that was executed, matching the `TestScript.url`.",
    )
    result: typing.Optional[TestReportResult] = pydantic.Field(
        description="The overall result from the execution of the TestScript."
    )
    score: typing.Optional[Decimal] = pydantic.Field(
        description="The final score (percentage of tests passed) resulting from the execution of the TestScript."
    )
    tester: typing.Optional[str] = pydantic.Field(
        description="Name of the tester producing this report (Organization or individual)."
    )
    issued: typing.Optional[DateTime] = pydantic.Field(
        description="When the TestScript was executed and this TestReport was generated."
    )
    participant: typing.Optional[typing.List[TestReportParticipant]] = pydantic.Field(
        description="A participant in the test execution, either the execution engine, a client, or a server."
    )
    setup: typing.Optional[TestReportSetup] = pydantic.Field(
        description="The results of the series of required setup operations before the tests were executed."
    )
    test: typing.Optional[typing.List[TestReportTest]] = pydantic.Field(
        description="A test executed from the test script."
    )
    teardown: typing.Optional[TestReportTeardown] = pydantic.Field(
        description="The results of the series of operations required to clean up after all the tests were executed (successfully or otherwise)."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
