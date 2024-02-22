# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .agent_channel import AgentChannel
from .agent_setting import AgentSetting
from .agent_status import AgentStatus
from .code import Code
from .id import Id
from .identifier import Identifier
from .meta import Meta
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Agent(pydantic.BaseModel):
    """
    Configuration details for an instance of the Medplum agent application.
    """

    resource_type: typing.Literal["Agent"] = pydantic.Field(alias="resourceType")
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
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="An identifier for this agent."
    )
    name: str = pydantic.Field(description="The human readable friendly name of the agent.")
    status: AgentStatus = pydantic.Field(description="The status of the agent.")
    device: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Optional device resource representing the device running the agent."
    )
    setting: typing.Optional[typing.List[AgentSetting]] = pydantic.Field(
        default=None, description="The settings for the agent."
    )
    channel: typing.List[AgentChannel] = pydantic.Field(
        description="Details where to send notifications when resources are received that meet the criteria."
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
