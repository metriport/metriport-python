# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .graph_definition_link import GraphDefinitionLink
from .graph_definition_status import GraphDefinitionStatus
from .markdown import Markdown
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GraphDefinition(BaseResource):
    """
    A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.
    """

    resource_type: typing.Literal["GraphDefinition"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        default=None,
        description="An absolute URI that is used to identify this graph definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this graph definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the graph definition is stored on different servers.",
    )
    version: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The identifier that is used to identify this version of the graph definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the graph definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.",
    )
    name: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A natural language name identifying the graph definition. This name should be usable as an identifier for the module by machine processing applications such as code generation.",
    )
    status: typing.Optional[GraphDefinitionStatus] = pydantic.Field(
        default=None, description="The status of this graph definition. Enables tracking the life-cycle of the content."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="A Boolean value to indicate that this graph definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.",
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        default=None,
        description="The date (and optionally time) when the graph definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the graph definition changes.",
    )
    publisher: typing.Optional[str] = pydantic.Field(
        default=None, description="The name of the organization or individual that published the graph definition."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        default=None, description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="A free text natural language description of the graph definition from a consumer's perspective.",
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        default=None,
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate graph definition instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="A legal or geographic region in which the graph definition is intended to be used."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="Explanation of why this graph definition is needed and why it has been designed as it has.",
    )
    start: typing.Optional[Code] = pydantic.Field(
        default=None, description="The type of FHIR resource at which instances of this graph start."
    )
    profile: typing.Optional[Canonical] = pydantic.Field(
        default=None, description="The profile that describes the use of the base resource."
    )
    link: typing.Optional[typing.List[GraphDefinitionLink]] = pydantic.Field(
        default=None, description="Links this graph makes rules about."
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
