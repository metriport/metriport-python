# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .canonical import Canonical
from .capability_statement_document import CapabilityStatementDocument
from .capability_statement_fhir_version import CapabilityStatementFhirVersion
from .capability_statement_implementation import CapabilityStatementImplementation
from .capability_statement_kind import CapabilityStatementKind
from .capability_statement_messaging import CapabilityStatementMessaging
from .capability_statement_rest import CapabilityStatementRest
from .capability_statement_software import CapabilityStatementSoftware
from .capability_statement_status import CapabilityStatementStatus
from .code import Code
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .markdown import Markdown
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CapabilityStatement(BaseResource):
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    resource_type: typing_extensions.Literal["CapabilityStatement"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        description="An absolute URI that is used to identify this capability statement when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this capability statement is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the capability statement is stored on different servers."
    )
    version: typing.Optional[str] = pydantic.Field(
        description="The identifier that is used to identify this version of the capability statement when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the capability statement author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the capability statement. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    title: typing.Optional[str] = pydantic.Field(
        description="A short, descriptive, user-friendly title for the capability statement."
    )
    status: typing.Optional[CapabilityStatementStatus] = pydantic.Field(
        description="The status of this capability statement. Enables tracking the life-cycle of the content."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        description="A Boolean value to indicate that this capability statement is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the capability statement was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the capability statement changes."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the capability statement."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the capability statement from a consumer's perspective. Typically, this is used when the capability statement describes a desired rather than an actual solution, for example as a formal expression of requirements as part of an RFP."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate capability statement instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the capability statement is intended to be used."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        description="Explanation of why this capability statement is needed and why it has been designed as it has."
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        description="A copyright statement relating to the capability statement and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the capability statement."
    )
    kind: typing.Optional[CapabilityStatementKind] = pydantic.Field(
        description="The way that this statement is intended to be used, to describe an actual running instance of software, a particular product (kind, not instance of software) or a class of implementation (e.g. a desired purchase)."
    )
    instantiates: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        description="Reference to a canonical URL of another CapabilityStatement that this software implements. This capability statement is a published API description that corresponds to a business service. The server may actually implement a subset of the capability statement it claims to implement, so the capability statement must specify the full capability details."
    )
    imports: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        description="Reference to a canonical URL of another CapabilityStatement that this software adds to. The capability statement automatically includes everything in the other statement, and it is not duplicated, though the server may repeat the same resources, interactions and operations to add additional details to them."
    )
    software: typing.Optional[CapabilityStatementSoftware] = pydantic.Field(
        description="Software that is covered by this capability statement. It is used when the capability statement describes the capabilities of a particular software version, independent of an installation."
    )
    implementation: typing.Optional[CapabilityStatementImplementation] = pydantic.Field(
        description="Identifies a specific implementation instance that is described by the capability statement - i.e. a particular installation, rather than the capabilities of a software program."
    )
    fhir_version: typing.Optional[CapabilityStatementFhirVersion] = pydantic.Field(
        alias="fhirVersion",
        description="The version of the FHIR specification that this CapabilityStatement describes (which SHALL be the same as the FHIR version of the CapabilityStatement itself). There is no default value.",
    )
    format: typing.Optional[typing.List[Code]] = pydantic.Field(
        description="A list of the formats supported by this implementation using their content types."
    )
    patch_format: typing.Optional[typing.List[Code]] = pydantic.Field(
        alias="patchFormat",
        description="A list of the patch formats supported by this implementation using their content types.",
    )
    implementation_guide: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="implementationGuide",
        description="A list of implementation guides that the server does (or should) support in their entirety.",
    )
    rest: typing.Optional[typing.List[CapabilityStatementRest]] = pydantic.Field(
        description="A definition of the restful capabilities of the solution, if any."
    )
    messaging: typing.Optional[typing.List[CapabilityStatementMessaging]] = pydantic.Field(
        description="A description of the messaging capabilities of the solution."
    )
    document: typing.Optional[typing.List[CapabilityStatementDocument]] = pydantic.Field(
        description="A document definition."
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