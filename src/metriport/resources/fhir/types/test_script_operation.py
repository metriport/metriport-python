# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .code import Code
from .coding import Coding
from .extension import Extension
from .id import Id
from .test_script_operation_method import TestScriptOperationMethod
from .test_script_request_header import TestScriptRequestHeader

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestScriptOperation(pydantic.BaseModel):
    """
    A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    type: typing.Optional[Coding] = pydantic.Field(description="Server interaction or operation type.")
    resource: typing.Optional[Code] = pydantic.Field(
        description="The type of the resource. See http://build.fhir.org/resourcelist.html."
    )
    label: typing.Optional[str] = pydantic.Field(
        description="The label would be used for tracking/logging purposes by test engines."
    )
    description: typing.Optional[str] = pydantic.Field(
        description="The description would be used by test engines for tracking and reporting purposes."
    )
    accept: typing.Optional[Code] = pydantic.Field(
        description="The mime-type to use for RESTful operation in the 'Accept' header."
    )
    content_type: typing.Optional[Code] = pydantic.Field(
        alias="contentType", description="The mime-type to use for RESTful operation in the 'Content-Type' header."
    )
    destination: typing.Optional[int] = pydantic.Field(
        description="The server where the request message is destined for. Must be one of the server numbers listed in TestScript.destination section."
    )
    encode_request_url: typing.Optional[bool] = pydantic.Field(
        alias="encodeRequestUrl",
        description="Whether or not to implicitly send the request url in encoded format. The default is true to match the standard RESTful client behavior. Set to false when communicating with a server that does not support encoded url paths.",
    )
    method: typing.Optional[TestScriptOperationMethod] = pydantic.Field(
        description="The HTTP method the test engine MUST use for this operation regardless of any other operation details."
    )
    origin: typing.Optional[int] = pydantic.Field(
        description="The server where the request message originates from. Must be one of the server numbers listed in TestScript.origin section."
    )
    params: typing.Optional[str] = pydantic.Field(
        description="Path plus parameters after [type]. Used to set parts of the request URL explicitly."
    )
    request_header: typing.Optional[typing.List[TestScriptRequestHeader]] = pydantic.Field(
        alias="requestHeader", description="Header elements would be used to set HTTP headers."
    )
    request_id: typing.Optional[Id] = pydantic.Field(
        alias="requestId", description="The fixture id (maybe new) to map to the request."
    )
    response_id: typing.Optional[Id] = pydantic.Field(
        alias="responseId", description="The fixture id (maybe new) to map to the response."
    )
    source_id: typing.Optional[Id] = pydantic.Field(
        alias="sourceId", description="The id of the fixture used as the body of a PUT or POST request."
    )
    target_id: typing.Optional[Id] = pydantic.Field(
        alias="targetId", description="Id of fixture used for extracting the [id], [type], and [vid] for GET requests."
    )
    url: typing.Optional[str] = pydantic.Field(description="Complete request URL.")

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
