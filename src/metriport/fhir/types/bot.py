# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .bot_audit_event_destination_item import BotAuditEventDestinationItem
from .bot_audit_event_trigger import BotAuditEventTrigger
from .bot_runtime_version import BotRuntimeVersion
from .code import Code
from .codeable_concept import CodeableConcept
from .id import Id
from .identifier import Identifier
from .meta import Meta
from .timing import Timing
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Bot(pydantic.BaseModel):
    """
    Bot account for automated actions.
    """

    resource_type: typing.Literal["Bot"] = pydantic.Field(alias="resourceType")
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
        default=None, description="An identifier for this bot."
    )
    name: typing.Optional[str] = pydantic.Field(default=None, description="A name associated with the Bot.")
    description: typing.Optional[str] = pydantic.Field(
        default=None, description="A summary, characterization or explanation of the Bot."
    )
    runtime_version: typing.Optional[BotRuntimeVersion] = pydantic.Field(
        alias="runtimeVersion",
        default=None,
        description="The identifier of the bot runtime environment (i.e., vmcontext, awslambda, etc).",
    )
    photo: typing.Optional[Attachment] = pydantic.Field(default=None, description="Image of the bot.")
    cron_timing: typing.Optional[Timing] = pydantic.Field(
        alias="cronTiming", default=None, description="A schedule for the bot to be executed."
    )
    cron_string: typing.Optional[str] = pydantic.Field(
        alias="cronString", default=None, description="A schedule for the bot to be executed."
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description='A code that classifies the service for searching, sorting and display purposes (e.g. "Surgical Procedure").',
    )
    run_as_user: typing.Optional[bool] = pydantic.Field(
        alias="runAsUser", default=None, description="Optional flag to indicate that the bot should be run as the user."
    )
    audit_event_trigger: typing.Optional[BotAuditEventTrigger] = pydantic.Field(
        alias="auditEventTrigger",
        default=None,
        description="Criteria for creating an AuditEvent as a result of the bot invocation. Possible values are 'always', 'never', 'on-error', or 'on-output'. Default value is 'always'.",
    )
    audit_event_destination: typing.Optional[typing.List[BotAuditEventDestinationItem]] = pydantic.Field(
        alias="auditEventDestination",
        default=None,
        description="The destination system in which the AuditEvent is to be sent. Possible values are 'log' or 'resource'. Default value is 'resource'.",
    )
    source_code: typing.Optional[Attachment] = pydantic.Field(
        alias="sourceCode", default=None, description="Bot logic in original source code form written by developers."
    )
    executable_code: typing.Optional[Attachment] = pydantic.Field(
        alias="executableCode",
        default=None,
        description="Bot logic in executable form as a result of compiling and bundling source code.",
    )
    code: typing.Optional[str] = pydantic.Field(
        default=None, description="DEPRECATED Bot logic script. Use Bot.sourceCode or Bot.executableCode instead."
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
