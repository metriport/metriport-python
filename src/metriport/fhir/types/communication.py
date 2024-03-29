# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .communication_payload import CommunicationPayload
from .date_time import DateTime
from .identifier import Identifier
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Communication(BaseResource):
    """
    An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.
    """

    resource_type: typing.Literal["Communication"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Business identifiers assigned to this communication by the performer or other systems which remain constant as the resource is updated and propagates from server to server.",
    )
    instantiates_canonical: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="instantiatesCanonical",
        default=None,
        description="The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this Communication.",
    )
    instantiates_uri: typing.Optional[typing.List[Uri]] = pydantic.Field(
        alias="instantiatesUri",
        default=None,
        description="The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this Communication.",
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn",
        default=None,
        description="An order, proposal or plan fulfilled in whole or in part by this Communication.",
    )
    part_of: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="partOf", default=None, description="Part of this action."
    )
    in_response_to: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="inResponseTo", default=None, description="Prior communication that this communication is in response to."
    )
    status: typing.Optional[Code] = pydantic.Field(default=None, description="The status of the transmission.")
    status_reason: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="statusReason",
        default=None,
        description="Captures the reason for the current state of the Communication.",
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="The type of message conveyed such as alert, notification, reminder, instruction, etc.",
    )
    priority: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="Characterizes how quickly the planned or in progress communication must be addressed. Includes concepts such as stat, urgent, routine.",
    )
    medium: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None, description="A channel that was used for this communication (e.g. email, fax)."
    )
    subject: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The patient or group that was the focus of this communication."
    )
    topic: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="Description of the purpose/content, similar to a subject line in an email."
    )
    about: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description="Other resources that pertain to this communication and to which this communication should be associated.",
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The Encounter during which this Communication was created or to which the creation of this record is tightly associated.",
    )
    sent: typing.Optional[DateTime] = pydantic.Field(
        default=None, description="The time when this communication was sent."
    )
    received: typing.Optional[DateTime] = pydantic.Field(
        default=None, description="The time when this communication arrived at the destination."
    )
    recipient: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description="The entity (e.g. person, organization, clinical information system, care team or device) which was the target of the communication. If receipts need to be tracked by an individual, a separate resource instance will need to be created for each recipient. Multiple recipient communications are intended where either receipts are not tracked (e.g. a mass mail-out) or a receipt is captured in aggregate (all emails confirmed received by a particular time).",
    )
    sender: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The entity (e.g. person, organization, clinical information system, or device) which was the source of the communication.",
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode", default=None, description="The reason or justification for the communication."
    )
    reason_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="reasonReference",
        default=None,
        description="Indicates another resource whose existence justifies this communication.",
    )
    payload: typing.Optional[typing.List[CommunicationPayload]] = pydantic.Field(
        default=None, description="Text, attachment(s), or resource(s) that was communicated to the recipient."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None,
        description="Additional notes or commentary about the communication by the sender, receiver or other interested parties.",
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
