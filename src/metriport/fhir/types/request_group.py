# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .reference import Reference
from .request_group_action import RequestGroupAction
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RequestGroup(BaseResource):
    """
    A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
    """

    resource_type: typing_extensions.Literal["RequestGroup"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Allows a service to provide a unique, business identifier for the request."
    )
    instantiates_canonical: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="instantiatesCanonical",
        description="A canonical URL referencing a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this request.",
    )
    instantiates_uri: typing.Optional[typing.List[Uri]] = pydantic.Field(
        alias="instantiatesUri",
        description="A URL referencing an externally defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this request.",
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn", description="A plan, proposal or order that is fulfilled in whole or in part by this request."
    )
    replaces: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Completed or terminated request(s) whose function is taken by this new request."
    )
    group_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="groupIdentifier",
        description="A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar form.",
    )
    status: typing.Optional[Code] = pydantic.Field(
        description="The current state of the request. For request groups, the status reflects the status of all the requests in the group."
    )
    intent: typing.Optional[Code] = pydantic.Field(
        description="Indicates the level of authority/intentionality associated with the request and where the request fits into the workflow chain."
    )
    priority: typing.Optional[Code] = pydantic.Field(
        description="Indicates how quickly the request should be addressed with respect to other requests."
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A code that identifies what the overall request group is."
    )
    subject: typing.Optional[Reference] = pydantic.Field(
        description="The subject for which the request group was created."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        description="Describes the context of the request group, if any."
    )
    authored_on: typing.Optional[DateTime] = pydantic.Field(
        alias="authoredOn", description="Indicates when the request group was created."
    )
    author: typing.Optional[Reference] = pydantic.Field(
        description="Provides a reference to the author of the request group."
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode", description="Describes the reason for the request group in coded or textual form."
    )
    reason_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="reasonReference", description="Indicates another resource whose existence justifies this request group."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Provides a mechanism to communicate additional information about the response."
    )
    action: typing.Optional[typing.List[RequestGroupAction]] = pydantic.Field(
        description="The actions, if any, produced by the evaluation of the artifact."
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