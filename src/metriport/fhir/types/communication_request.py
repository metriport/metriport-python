# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .communication_request_payload import CommunicationRequestPayload
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CommunicationRequest(BaseResource):
    """
    A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
    """

    resource_type: typing.Literal["CommunicationRequest"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Business identifiers assigned to this communication request by the performer or other systems which remain constant as the resource is updated and propagates from server to server."
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn", description="A plan or proposal that is fulfilled in whole or in part by this request."
    )
    replaces: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Completed or terminated request(s) whose function is taken by this new request."
    )
    group_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="groupIdentifier",
        description="A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar form.",
    )
    status: typing.Optional[Code] = pydantic.Field(description="The status of the proposal or order.")
    status_reason: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="statusReason", description="Captures the reason for the current state of the CommunicationRequest."
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="The type of message to be sent such as alert, notification, reminder, instruction, etc."
    )
    priority: typing.Optional[Code] = pydantic.Field(
        description="Characterizes how quickly the proposed act must be initiated. Includes concepts such as stat, urgent, routine."
    )
    do_not_perform: typing.Optional[bool] = pydantic.Field(
        alias="doNotPerform",
        description="If true indicates that the CommunicationRequest is asking for the specified action to _not_ occur.",
    )
    medium: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A channel that was used for this communication (e.g. email, fax)."
    )
    subject: typing.Optional[Reference] = pydantic.Field(
        description="The patient or group that is the focus of this communication request."
    )
    about: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Other resources that pertain to this communication request and to which this communication request should be associated."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        description="The Encounter during which this CommunicationRequest was created or to which the creation of this record is tightly associated."
    )
    payload: typing.Optional[typing.List[CommunicationRequestPayload]] = pydantic.Field(
        description="Text, attachment(s), or resource(s) to be communicated to the recipient."
    )
    occurrence_date_time: typing.Optional[str] = pydantic.Field(
        alias="occurrenceDateTime", description="The time when this communication is to occur."
    )
    occurrence_period: typing.Optional[Period] = pydantic.Field(
        alias="occurrencePeriod", description="The time when this communication is to occur."
    )
    authored_on: typing.Optional[DateTime] = pydantic.Field(
        alias="authoredOn",
        description="For draft requests, indicates the date of initial creation. For requests with other statuses, indicates the date of activation.",
    )
    requester: typing.Optional[Reference] = pydantic.Field(
        description="The device, individual, or organization who initiated the request and has responsibility for its activation."
    )
    recipient: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The entity (e.g. person, organization, clinical information system, device, group, or care team) which is the intended target of the communication."
    )
    sender: typing.Optional[Reference] = pydantic.Field(
        description="The entity (e.g. person, organization, clinical information system, or device) which is to be the source of the communication."
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode", description="Describes why the request is being made in coded or textual form."
    )
    reason_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="reasonReference", description="Indicates another resource whose existence justifies this request."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Comments made about the request by the requester, sender, recipient, subject or other participants."
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
