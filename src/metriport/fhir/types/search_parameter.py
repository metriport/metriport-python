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
from .markdown import Markdown
from .search_parameter_comparator_item import SearchParameterComparatorItem
from .search_parameter_component import SearchParameterComponent
from .search_parameter_modifier_item import SearchParameterModifierItem
from .search_parameter_status import SearchParameterStatus
from .search_parameter_type import SearchParameterType
from .search_parameter_xpath_usage import SearchParameterXpathUsage
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SearchParameter(BaseResource):
    """
    A search parameter that defines a named search item that can be used to search/filter on a resource.
    """

    resource_type: typing.Literal["SearchParameter"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        default=None,
        description="An absolute URI that is used to identify this search parameter when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this search parameter is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the search parameter is stored on different servers.",
    )
    version: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The identifier that is used to identify this version of the search parameter when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the search parameter author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.",
    )
    name: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A natural language name identifying the search parameter. This name should be usable as an identifier for the module by machine processing applications such as code generation.",
    )
    derived_from: typing.Optional[Canonical] = pydantic.Field(
        alias="derivedFrom",
        default=None,
        description="Where this search parameter is originally defined. If a derivedFrom is provided, then the details in the search parameter must be consistent with the definition from which it is defined. i.e. the parameter should have the same meaning, and (usually) the functionality should be a proper subset of the underlying search parameter.",
    )
    status: typing.Optional[SearchParameterStatus] = pydantic.Field(
        default=None, description="The status of this search parameter. Enables tracking the life-cycle of the content."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="A Boolean value to indicate that this search parameter is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.",
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        default=None,
        description="The date (and optionally time) when the search parameter was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the search parameter changes.",
    )
    publisher: typing.Optional[str] = pydantic.Field(
        default=None, description="The name of the organization or individual that published the search parameter."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        default=None, description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(default=None, description="And how it used.")
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        default=None,
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate search parameter instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="A legal or geographic region in which the search parameter is intended to be used."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="Explanation of why this search parameter is needed and why it has been designed as it has.",
    )
    code: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="The code used in the URL or the parameter name in a parameters resource for this search parameter.",
    )
    base: typing.Optional[typing.List[Code]] = pydantic.Field(
        default=None, description="The base resource type(s) that this search parameter can be used against."
    )
    type: typing.Optional[SearchParameterType] = pydantic.Field(
        default=None,
        description="The type of value that a search parameter may contain, and how the content is interpreted.",
    )
    expression: typing.Optional[str] = pydantic.Field(
        default=None, description="A FHIRPath expression that returns a set of elements for the search parameter."
    )
    xpath: typing.Optional[str] = pydantic.Field(
        default=None, description="An XPath expression that returns a set of elements for the search parameter."
    )
    xpath_usage: typing.Optional[SearchParameterXpathUsage] = pydantic.Field(
        alias="xpathUsage",
        default=None,
        description="How the search parameter relates to the set of elements returned by evaluating the xpath query.",
    )
    target: typing.Optional[typing.List[Code]] = pydantic.Field(
        default=None, description="Types of resource (if a resource is referenced)."
    )
    multiple_or: typing.Optional[bool] = pydantic.Field(
        alias="multipleOr",
        default=None,
        description="Whether multiple values are allowed for each time the parameter exists. Values are separated by commas, and the parameter matches if any of the values match.",
    )
    multiple_and: typing.Optional[bool] = pydantic.Field(
        alias="multipleAnd",
        default=None,
        description="Whether multiple parameters are allowed - e.g. more than one parameter with the same name. The search matches if all the parameters match.",
    )
    comparator: typing.Optional[typing.List[SearchParameterComparatorItem]] = pydantic.Field(
        default=None, description="Comparators supported for the search parameter."
    )
    modifier: typing.Optional[typing.List[SearchParameterModifierItem]] = pydantic.Field(
        default=None, description="A modifier supported for the search parameter."
    )
    chain: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None,
        description="Contains the names of any search parameters which may be chained to the containing search parameter. Chained parameters may be added to search parameters of type reference and specify that resources will only be returned if they contain a reference to a resource which matches the chained parameter value. Values for this field should be drawn from SearchParameter.code for a parameter on the target resource type.",
    )
    component: typing.Optional[typing.List[SearchParameterComponent]] = pydantic.Field(
        default=None, description="Used to define the parts of a composite search parameter."
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
