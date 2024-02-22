# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .code import Code
from .id import Id
from .meta import Meta
from .project_membership_access import ProjectMembershipAccess
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProjectMembership(pydantic.BaseModel):
    """
    Medplum project membership. A project membership grants a user access to a project.
    """

    resource_type: typing.Literal["ProjectMembership"] = pydantic.Field(alias="resourceType")
    id: typing.Optional[Id] = pydantic.Field(
        default=None,
        description="The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.",
    )
    meta: typing.Optional[Meta] = pydantic.Field(
        default=None,
        description="The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.",
    )
    implicit_rules: typing.Optional[Uri] = pydantic.Field(
        alias="implicitRules",
        default=None,
        description="A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.",
    )
    language: typing.Optional[Code] = pydantic.Field(
        default=None, description="The base language in which the resource is written."
    )
    project: Reference = pydantic.Field(description="Project where the memberships are available.")
    invited_by: typing.Optional[Reference] = pydantic.Field(
        alias="invitedBy", default=None, description="The project administrator who invited the user to the project."
    )
    user: Reference = pydantic.Field(description="User that is granted access to the project.")
    profile: Reference = pydantic.Field(
        description="Reference to the resource that represents the user profile within the project."
    )
    external_id: typing.Optional[str] = pydantic.Field(
        alias="externalId",
        default=None,
        description='A String that is an identifier for the resource as defined by the provisioning client. The "externalId" may simplify identification of a resource between the provisioning client and the service provider by allowing the client to use a filter to locate the resource with an identifier from the provisioning domain, obviating the need to store a local mapping between the provisioning domain\'s identifier of the resource and the identifier used by the service provider. Each resource MAY include a non-empty "externalId" value. The value of the "externalId" attribute is always issued by the provisioning client and MUST NOT be specified by the service provider. The service provider MUST always interpret the externalId as scoped to the provisioning domain.',
    )
    access_policy: typing.Optional[Reference] = pydantic.Field(
        alias="accessPolicy", default=None, description="The access policy for the user within the project memebership."
    )
    access: typing.Optional[typing.List[ProjectMembershipAccess]] = pydantic.Field(
        default=None, description="Extended access configuration using parameterized access policies."
    )
    user_configuration: typing.Optional[Reference] = pydantic.Field(
        alias="userConfiguration",
        default=None,
        description="The user configuration for the user within the project memebership such as menu links, saved searches, and features.",
    )
    admin: typing.Optional[bool] = pydantic.Field(
        default=None, description="Whether this user is a project administrator."
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
