# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .markdown import Markdown
from .operation_definition_kind import OperationDefinitionKind
from .operation_definition_overload import OperationDefinitionOverload
from .operation_definition_parameter import OperationDefinitionParameter
from .operation_definition_status import OperationDefinitionStatus
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OperationDefinition(BaseResource):
    """
    A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
    """

    resource_type: typing_extensions.Literal["OperationDefinition"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        description="An absolute URI that is used to identify this operation definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this operation definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the operation definition is stored on different servers."
    )
    version: typing.Optional[str] = pydantic.Field(
        description="The identifier that is used to identify this version of the operation definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the operation definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the operation definition. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    title: typing.Optional[str] = pydantic.Field(
        description="A short, descriptive, user-friendly title for the operation definition."
    )
    status: typing.Optional[OperationDefinitionStatus] = pydantic.Field(
        description="The status of this operation definition. Enables tracking the life-cycle of the content."
    )
    kind: typing.Optional[OperationDefinitionKind] = pydantic.Field(
        description="Whether this is an operation or a named query."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        description="A Boolean value to indicate that this operation definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the operation definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the operation definition changes."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the operation definition."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the operation definition from a consumer's perspective."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate operation definition instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the operation definition is intended to be used."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        description="Explanation of why this operation definition is needed and why it has been designed as it has."
    )
    affects_state: typing.Optional[bool] = pydantic.Field(
        alias="affectsState",
        description="Whether the operation affects state. Side effects such as producing audit trail entries do not count as 'affecting state'.",
    )
    code: typing.Optional[Code] = pydantic.Field(description="The name used to invoke the operation.")
    comment: typing.Optional[Markdown] = pydantic.Field(
        description="Additional information about how to use this operation or named query."
    )
    base: typing.Optional[Canonical] = pydantic.Field(
        description="Indicates that this operation definition is a constraining profile on the base."
    )
    resource: typing.Optional[typing.List[Code]] = pydantic.Field(
        description="The types on which this operation can be executed."
    )
    system: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether this operation or named query can be invoked at the system level (e.g. without needing to choose a resource type for the context)."
    )
    type: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether this operation or named query can be invoked at the resource type level for any given resource type level (e.g. without needing to choose a specific resource id for the context)."
    )
    instance: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether this operation can be invoked on a particular instance of one of the given types."
    )
    input_profile: typing.Optional[Canonical] = pydantic.Field(
        alias="inputProfile",
        description="Additional validation information for the in parameters - a single profile that covers all the parameters. The profile is a constraint on the parameters resource as a whole.",
    )
    output_profile: typing.Optional[Canonical] = pydantic.Field(
        alias="outputProfile",
        description="Additional validation information for the out parameters - a single profile that covers all the parameters. The profile is a constraint on the parameters resource.",
    )
    parameter: typing.Optional[typing.List[OperationDefinitionParameter]] = pydantic.Field(
        description="The parameters for the operation/query."
    )
    overload: typing.Optional[typing.List[OperationDefinitionOverload]] = pydantic.Field(
        description="Defines an appropriate combination of parameters to use when invoking this operation, to help code generators when generating overloaded parameter sets for this operation."
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