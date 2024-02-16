# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .identifier import Identifier
from .markdown import Markdown
from .reference import Reference
from .test_script_destination import TestScriptDestination
from .test_script_fixture import TestScriptFixture
from .test_script_metadata import TestScriptMetadata
from .test_script_origin import TestScriptOrigin
from .test_script_setup import TestScriptSetup
from .test_script_status import TestScriptStatus
from .test_script_teardown import TestScriptTeardown
from .test_script_test import TestScriptTest
from .test_script_variable import TestScriptVariable
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestScript(BaseResource):
    """
    A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    """

    resource_type: typing_extensions.Literal["TestScript"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        description="An absolute URI that is used to identify this test script when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this test script is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the test script is stored on different servers."
    )
    identifier: typing.Optional[Identifier] = pydantic.Field(
        description="A formal identifier that is used to identify this test script when it is represented in other formats, or referenced in a specification, model, design or an instance."
    )
    version: typing.Optional[str] = pydantic.Field(
        description="The identifier that is used to identify this version of the test script when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the test script author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the test script. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    title: typing.Optional[str] = pydantic.Field(
        description="A short, descriptive, user-friendly title for the test script."
    )
    status: typing.Optional[TestScriptStatus] = pydantic.Field(
        description="The status of this test script. Enables tracking the life-cycle of the content."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        description="A Boolean value to indicate that this test script is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the test script was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the test script changes."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the test script."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the test script from a consumer's perspective."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate test script instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the test script is intended to be used."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        description="Explanation of why this test script is needed and why it has been designed as it has."
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        description="A copyright statement relating to the test script and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the test script."
    )
    origin: typing.Optional[typing.List[TestScriptOrigin]] = pydantic.Field(
        description="An abstract server used in operations within this test script in the origin element."
    )
    destination: typing.Optional[typing.List[TestScriptDestination]] = pydantic.Field(
        description="An abstract server used in operations within this test script in the destination element."
    )
    metadata: typing.Optional[TestScriptMetadata] = pydantic.Field(
        description="The required capability must exist and are assumed to function correctly on the FHIR server being tested."
    )
    fixture: typing.Optional[typing.List[TestScriptFixture]] = pydantic.Field(
        description="Fixture in the test script - by reference (uri). All fixtures are required for the test script to execute."
    )
    profile: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Reference to the profile to be used for validation."
    )
    variable: typing.Optional[typing.List[TestScriptVariable]] = pydantic.Field(
        description="Variable is set based either on element value in response body or on header field value in the response headers."
    )
    setup: typing.Optional[TestScriptSetup] = pydantic.Field(
        description="A series of required setup operations before tests are executed."
    )
    test: typing.Optional[typing.List[TestScriptTest]] = pydantic.Field(description="A test in this script.")
    teardown: typing.Optional[TestScriptTeardown] = pydantic.Field(
        description="A series of operations required to clean up after all the tests are executed (successfully or otherwise)."
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
