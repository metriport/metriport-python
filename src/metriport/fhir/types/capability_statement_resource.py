# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .canonical import Canonical
from .capability_statement_interaction import CapabilityStatementInteraction
from .capability_statement_operation import CapabilityStatementOperation
from .capability_statement_resource_conditional_delete import CapabilityStatementResourceConditionalDelete
from .capability_statement_resource_conditional_read import CapabilityStatementResourceConditionalRead
from .capability_statement_resource_reference_policy_item import CapabilityStatementResourceReferencePolicyItem
from .capability_statement_resource_versioning import CapabilityStatementResourceVersioning
from .capability_statement_search_param import CapabilityStatementSearchParam
from .code import Code
from .extension import Extension
from .markdown import Markdown

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CapabilityStatementResource(pydantic.BaseModel):
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    type: typing.Optional[Code] = pydantic.Field(
        default=None, description="A type of resource exposed via the restful interface."
    )
    profile: typing.Optional[Canonical] = pydantic.Field(
        default=None,
        description="A specification of the profile that describes the solution's overall support for the resource, including any constraints on cardinality, bindings, lengths or other limitations. See further discussion in [Using Profiles](profiling.html#profile-uses).",
    )
    supported_profile: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="supportedProfile",
        default=None,
        description='A list of profiles that represent different use cases supported by the system. For a server, "supported by the system" means the system hosts/produces a set of resources that are conformant to a particular profile, and allows clients that use its services to search using this profile and to find appropriate data. For a client, it means the system will search by this profile and process data according to the guidance implicit in the profile. See further discussion in [Using Profiles](profiling.html#profile-uses).',
    )
    documentation: typing.Optional[Markdown] = pydantic.Field(
        default=None, description="Additional information about the resource type used by the system."
    )
    interaction: typing.Optional[typing.List[CapabilityStatementInteraction]] = pydantic.Field(
        default=None, description="Identifies a restful operation supported by the solution."
    )
    versioning: typing.Optional[CapabilityStatementResourceVersioning] = pydantic.Field(
        default=None,
        description="This field is set to no-version to specify that the system does not support (server) or use (client) versioning for this resource type. If this has some other value, the server must at least correctly track and populate the versionId meta-property on resources. If the value is 'versioned-update', then the server supports all the versioning features, including using e-tags for version integrity in the API.",
    )
    read_history: typing.Optional[bool] = pydantic.Field(
        alias="readHistory",
        default=None,
        description="A flag for whether the server is able to return past versions as part of the vRead operation.",
    )
    update_create: typing.Optional[bool] = pydantic.Field(
        alias="updateCreate",
        default=None,
        description="A flag to indicate that the server allows or needs to allow the client to create new identities on the server (that is, the client PUTs to a location where there is no existing resource). Allowing this operation means that the server allows the client to create new identities on the server.",
    )
    conditional_create: typing.Optional[bool] = pydantic.Field(
        alias="conditionalCreate",
        default=None,
        description="A flag that indicates that the server supports conditional create.",
    )
    conditional_read: typing.Optional[CapabilityStatementResourceConditionalRead] = pydantic.Field(
        alias="conditionalRead",
        default=None,
        description="A code that indicates how the server supports conditional read.",
    )
    conditional_update: typing.Optional[bool] = pydantic.Field(
        alias="conditionalUpdate",
        default=None,
        description="A flag that indicates that the server supports conditional update.",
    )
    conditional_delete: typing.Optional[CapabilityStatementResourceConditionalDelete] = pydantic.Field(
        alias="conditionalDelete",
        default=None,
        description="A code that indicates how the server supports conditional delete.",
    )
    reference_policy: typing.Optional[typing.List[CapabilityStatementResourceReferencePolicyItem]] = pydantic.Field(
        alias="referencePolicy", default=None, description="A set of flags that defines how references are supported."
    )
    search_include: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="searchInclude", default=None, description="A list of \_include values supported by the server."
    )
    search_rev_include: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="searchRevInclude",
        default=None,
        description="A list of \_revinclude (reverse include) values supported by the server.",
    )
    search_param: typing.Optional[typing.List[CapabilityStatementSearchParam]] = pydantic.Field(
        alias="searchParam",
        default=None,
        description="Search parameters for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.",
    )
    operation: typing.Optional[typing.List[CapabilityStatementOperation]] = pydantic.Field(
        default=None,
        description="Definition of an operation or a named query together with its parameters and their meaning and type. Consult the definition of the operation for details about how to invoke the operation, and the parameters.",
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
