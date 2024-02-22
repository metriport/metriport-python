# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .canonical import Canonical
from .code_system_concept import CodeSystemConcept
from .code_system_content import CodeSystemContent
from .code_system_filter import CodeSystemFilter
from .code_system_hierarchy_meaning import CodeSystemHierarchyMeaning
from .code_system_property import CodeSystemProperty
from .code_system_status import CodeSystemStatus
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .identifier import Identifier
from .markdown import Markdown
from .unsigned_int import UnsignedInt
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CodeSystem(BaseResource):
    """
    The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.
    """

    resource_type: typing.Literal["CodeSystem"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        default=None,
        description="An absolute URI that is used to identify this code system when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this code system is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the code system is stored on different servers. This is used in [Coding](datatypes.html#Coding).system.",
    )
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="A formal identifier that is used to identify this code system when it is represented in other formats, or referenced in a specification, model, design or an instance.",
    )
    version: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The identifier that is used to identify this version of the code system when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the code system author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. This is used in [Coding](datatypes.html#Coding).version.",
    )
    name: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A natural language name identifying the code system. This name should be usable as an identifier for the module by machine processing applications such as code generation.",
    )
    title: typing.Optional[str] = pydantic.Field(
        default=None, description="A short, descriptive, user-friendly title for the code system."
    )
    status: typing.Optional[CodeSystemStatus] = pydantic.Field(
        default=None, description="The date (and optionally time) when the code system resource was created or revised."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="A Boolean value to indicate that this code system is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.",
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        default=None,
        description="The date (and optionally time) when the code system was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the code system changes.",
    )
    publisher: typing.Optional[str] = pydantic.Field(
        default=None, description="The name of the organization or individual that published the code system."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        default=None, description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="A free text natural language description of the code system from a consumer's perspective.",
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        default=None,
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate code system instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="A legal or geographic region in which the code system is intended to be used."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="Explanation of why this code system is needed and why it has been designed as it has.",
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="A copyright statement relating to the code system and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the code system.",
    )
    case_sensitive: typing.Optional[bool] = pydantic.Field(
        alias="caseSensitive",
        default=None,
        description="If code comparison is case sensitive when codes within this system are compared to each other.",
    )
    value_set: typing.Optional[Canonical] = pydantic.Field(
        alias="valueSet",
        default=None,
        description="Canonical reference to the value set that contains the entire code system.",
    )
    hierarchy_meaning: typing.Optional[CodeSystemHierarchyMeaning] = pydantic.Field(
        alias="hierarchyMeaning",
        default=None,
        description="The meaning of the hierarchy of concepts as represented in this resource.",
    )
    compositional: typing.Optional[bool] = pydantic.Field(
        default=None, description="The code system defines a compositional (post-coordination) grammar."
    )
    version_needed: typing.Optional[bool] = pydantic.Field(
        alias="versionNeeded",
        default=None,
        description="This flag is used to signify that the code system does not commit to concept permanence across versions. If true, a version must be specified when referencing this code system.",
    )
    content: typing.Optional[CodeSystemContent] = pydantic.Field(
        default=None,
        description="The extent of the content of the code system (the concepts and codes it defines) are represented in this resource instance.",
    )
    supplements: typing.Optional[Canonical] = pydantic.Field(
        default=None,
        description="The canonical URL of the code system that this code system supplement is adding designations and properties to.",
    )
    count: typing.Optional[UnsignedInt] = pydantic.Field(
        default=None,
        description="The total number of concepts defined by the code system. Where the code system has a compositional grammar, the basis of this count is defined by the system steward.",
    )
    filter: typing.Optional[typing.List[CodeSystemFilter]] = pydantic.Field(
        default=None,
        description="A filter that can be used in a value set compose statement when selecting concepts using a filter.",
    )
    property: typing.Optional[typing.List[CodeSystemProperty]] = pydantic.Field(
        default=None,
        description="A property defines an additional slot through which additional information can be provided about a concept.",
    )
    concept: typing.Optional[typing.List[CodeSystemConcept]] = pydantic.Field(
        default=None,
        description="Concepts that are in the code system. The concept definitions are inherently hierarchical, but the definitions must be consulted to determine what the meanings of the hierarchical relationships are.",
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
