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
from .uri import Uri
from .usage_context import UsageContext
from .value_set_compose import ValueSetCompose
from .value_set_expansion import ValueSetExpansion
from .value_set_status import ValueSetStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ValueSet(BaseResource):
    """
    A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
    """

    resource_type: typing_extensions.Literal["ValueSet"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        description="An absolute URI that is used to identify this value set when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this value set is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the value set is stored on different servers."
    )
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="A formal identifier that is used to identify this value set when it is represented in other formats, or referenced in a specification, model, design or an instance."
    )
    version: typing.Optional[str] = pydantic.Field(
        description="The identifier that is used to identify this version of the value set when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the value set author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the value set. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    title: typing.Optional[str] = pydantic.Field(
        description="A short, descriptive, user-friendly title for the value set."
    )
    status: typing.Optional[ValueSetStatus] = pydantic.Field(
        description="The status of this value set. Enables tracking the life-cycle of the content. The status of the value set applies to the value set definition (ValueSet.compose) and the associated ValueSet metadata. Expansions do not have a state."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        description="A Boolean value to indicate that this value set is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the value set was created or revised (e.g. the 'content logical definition')."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the value set."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the value set from a consumer's perspective. The textual description specifies the span of meanings for concepts to be included within the Value Set Expansion, and also may specify the intended use and limitations of the Value Set."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate value set instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the value set is intended to be used."
    )
    immutable: typing.Optional[bool] = pydantic.Field(
        description="If this is set to 'true', then no new versions of the content logical definition can be created. Note: Other metadata might still change."
    )
    purpose: typing.Optional[Markdown] = pydantic.Field(
        description="Explanation of why this value set is needed and why it has been designed as it has."
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        description="A copyright statement relating to the value set and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the value set."
    )
    compose: typing.Optional[ValueSetCompose] = pydantic.Field(
        description="A set of criteria that define the contents of the value set by including or excluding codes selected from the specified code system(s) that the value set draws from. This is also known as the Content Logical Definition (CLD)."
    )
    expansion: typing.Optional[ValueSetExpansion] = pydantic.Field(
        description='A value set can also be "expanded", where the value set is turned into a simple collection of enumerated codes. This element holds the expansion, if it has been performed.'
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
