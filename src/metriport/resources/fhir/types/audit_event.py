# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .audit_event_action import AuditEventAction
from .audit_event_agent import AuditEventAgent
from .audit_event_entity import AuditEventEntity
from .audit_event_outcome import AuditEventOutcome
from .audit_event_source import AuditEventSource
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .coding import Coding
from .instant import Instant
from .period import Period

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AuditEvent(BaseResource):
    """
    A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
    """

    resource_type: typing_extensions.Literal["AuditEvent"] = pydantic.Field(alias="resourceType")
    type: Coding = pydantic.Field(
        description="Identifier for a family of the event. For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function."
    )
    subtype: typing.Optional[typing.List[Coding]] = pydantic.Field(description="Identifier for the category of event.")
    action: typing.Optional[AuditEventAction] = pydantic.Field(
        description="Indicator for type of action performed during the event that generated the audit."
    )
    period: typing.Optional[Period] = pydantic.Field(description="The period during which the activity occurred.")
    recorded: typing.Optional[Instant] = pydantic.Field(description="The time when the event was recorded.")
    outcome: typing.Optional[AuditEventOutcome] = pydantic.Field(
        description="Indicates whether the event succeeded or failed."
    )
    outcome_desc: typing.Optional[str] = pydantic.Field(
        alias="outcomeDesc", description="A free text description of the outcome of the event."
    )
    purpose_of_event: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="purposeOfEvent", description="The purposeOfUse (reason) that was used during the event being recorded."
    )
    agent: typing.List[AuditEventAgent] = pydantic.Field(
        description="An actor taking an active role in the event or activity that is logged."
    )
    source: AuditEventSource = pydantic.Field(description="The system that is reporting the event.")
    entity: typing.Optional[typing.List[AuditEventEntity]] = pydantic.Field(
        description="Specific instances of data or objects that have been accessed."
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
