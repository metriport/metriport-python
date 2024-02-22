# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .code import Code
from .id import Id
from .meta import Meta
from .project_features_item import ProjectFeaturesItem
from .project_secret import ProjectSecret
from .project_site import ProjectSite
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Project(pydantic.BaseModel):
    """
    Encapsulation of resources for a specific project or organization.
    """

    resource_type: typing.Literal["Project"] = pydantic.Field(alias="resourceType")
    id: typing.Optional[Id] = pydantic.Field(
        description="The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."
    )
    meta: typing.Optional[Meta] = pydantic.Field(
        description="The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."
    )
    implicit_rules: typing.Optional[Uri] = pydantic.Field(
        alias="implicitRules",
        description="A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc.",
    )
    language: typing.Optional[Code] = pydantic.Field(description="The base language in which the resource is written.")
    name: typing.Optional[str] = pydantic.Field(description="A name associated with the Project.")
    description: typing.Optional[str] = pydantic.Field(
        description="A summary, characterization or explanation of the Project."
    )
    super_admin: typing.Optional[bool] = pydantic.Field(
        alias="superAdmin",
        description="Whether this project is the super administrator project. A super administrator is a user who has complete access to all resources in all projects.",
    )
    strict_mode: typing.Optional[bool] = pydantic.Field(
        alias="strictMode", description="Whether this project uses strict FHIR validation."
    )
    check_references_on_write: typing.Optional[bool] = pydantic.Field(
        alias="checkReferencesOnWrite",
        description="Whether this project uses referential integrity on write operations such as 'create' and 'update'.",
    )
    owner: typing.Optional[Reference] = pydantic.Field(description="The user who owns the project.")
    features: typing.Optional[typing.List[ProjectFeaturesItem]] = pydantic.Field(
        description="A list of optional features that are enabled for the project."
    )
    default_patient_access_policy: typing.Optional[Reference] = pydantic.Field(
        alias="defaultPatientAccessPolicy",
        description="The default access policy for patients using open registration.",
    )
    secret: typing.Optional[typing.List[ProjectSecret]] = pydantic.Field(
        description="Secure environment variable that can be used to store secrets for bots."
    )
    site: typing.Optional[typing.List[ProjectSite]] = pydantic.Field(
        description="Web application or web site that is associated with the project."
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
