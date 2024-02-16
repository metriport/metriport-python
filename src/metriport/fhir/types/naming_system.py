# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .markdown import Markdown
from .naming_system_kind import NamingSystemKind
from .naming_system_status import NamingSystemStatus
from .naming_system_unique_id import NamingSystemUniqueId
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NamingSystem(BaseResource):
    """
    A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc. Represents a "System" used within the Identifier and Coding data types.
    """

    resource_type: typing_extensions.Literal["NamingSystem"] = pydantic.Field(alias="resourceType")
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the naming system. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    status: typing.Optional[NamingSystemStatus] = pydantic.Field(
        description="The status of this naming system. Enables tracking the life-cycle of the content."
    )
    kind: typing.Optional[NamingSystemKind] = pydantic.Field(
        description="Indicates the purpose for the naming system - what kinds of things does it make unique?"
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the naming system was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the naming system changes."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the naming system."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    responsible: typing.Optional[str] = pydantic.Field(
        description="The name of the organization that is responsible for issuing identifiers or codes for this namespace and ensuring their non-collision."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Categorizes a naming system for easier search by grouping related naming systems."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the naming system from a consumer's perspective. Details about what the namespace identifies including scope, granularity, version labeling, etc."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate naming system instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the naming system is intended to be used."
    )
    usage: typing.Optional[str] = pydantic.Field(
        description="Provides guidance on the use of the namespace, including the handling of formatting characters, use of upper vs. lower case, etc."
    )
    unique_id: typing.List[NamingSystemUniqueId] = pydantic.Field(
        alias="uniqueId",
        description="Indicates how the system may be identified when referenced in electronic exchange.",
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