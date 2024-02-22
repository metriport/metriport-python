# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .canonical import Canonical
from .id import Id
from .instant import Instant
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Meta(pydantic.BaseModel):
    """
    The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    version_id: typing.Optional[Id] = pydantic.Field(
        alias="versionId",
        default=None,
        description="The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.",
    )
    last_updated: typing.Optional[Instant] = pydantic.Field(
        alias="lastUpdated", default=None, description="When the resource last changed - e.g. when the version changed."
    )
    source: typing.Optional[Uri] = pydantic.Field(
        default=None,
        description="A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.",
    )
    profile: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        default=None,
        description="A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].",
    )
    security: typing.Optional[typing.List[Coding]] = pydantic.Field(
        default=None,
        description="Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.",
    )
    tag: typing.Optional[typing.List[Coding]] = pydantic.Field(
        default=None,
        description="Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.",
    )
    project: typing.Optional[Uri] = pydantic.Field(default=None, description="The project that contains this resource.")
    author: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The individual, device or organization who initiated the last change."
    )
    account: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Optional account reference that can be used for sub-project compartments."
    )
    compartment: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description="The list of compartments containing this resource. This is readonly and is set by the server.",
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


from .coding import Coding  # noqa: E402
from .extension import Extension  # noqa: E402
from .reference import Reference  # noqa: E402

Meta.update_forward_refs()
