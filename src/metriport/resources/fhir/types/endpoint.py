# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .coding import Coding
from .contact_point import ContactPoint
from .endpoint_status import EndpointStatus
from .identifier import Identifier
from .period import Period
from .reference import Reference
from .url import Url

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Endpoint(BaseResource):
    """
    The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
    """

    resource_type: typing_extensions.Literal["Endpoint"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifier for the organization that is used to identify the endpoint across multiple disparate systems."
    )
    status: typing.Optional[EndpointStatus] = pydantic.Field(
        description=("active \n" " suspended \n" " error \n" " off \n" " test.\n")
    )
    connection_type: Coding = pydantic.Field(
        alias="connectionType",
        description="A coded value that represents the technical details of the usage of this endpoint, such as what WSDLs should be used in what way. (e.g. XDS.b/DICOM/cds-hook).",
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A friendly name that this endpoint can be referred to with."
    )
    managing_organization: typing.Optional[Reference] = pydantic.Field(
        alias="managingOrganization",
        description="The organization that manages this endpoint (even if technically another organization is hosting this in the cloud, it is the organization associated with the data).",
    )
    contact: typing.Optional[typing.List[ContactPoint]] = pydantic.Field(
        description="Contact details for a human to contact about the subscription. The primary use of this for system administrator troubleshooting."
    )
    period: typing.Optional[Period] = pydantic.Field(
        description="The interval during which the endpoint is expected to be operational."
    )
    payload_type: typing.List[CodeableConcept] = pydantic.Field(
        alias="payloadType",
        description="The payload type describes the acceptable content that can be communicated on the endpoint.",
    )
    payload_mime_type: typing.Optional[typing.List[Code]] = pydantic.Field(
        alias="payloadMimeType",
        description="The mime type to send the payload in - e.g. application/fhir+xml, application/fhir+json. If the mime type is not specified, then the sender could send any content (including no content depending on the connectionType).",
    )
    address: typing.Optional[Url] = pydantic.Field(
        description="The uri that describes the actual end-point to connect to."
    )
    header: typing.Optional[typing.List[str]] = pydantic.Field(
        description="Additional headers / information to send as part of the notification."
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
