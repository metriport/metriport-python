# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .async_job_status import AsyncJobStatus
from .code import Code
from .id import Id
from .instant import Instant
from .meta import Meta
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AsyncJob(pydantic.BaseModel):
    """
    Contains details of long running asynchronous/background jobs.
    """

    resource_type: typing.Literal["AsyncJob"] = pydantic.Field(alias="resourceType")
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
    status: AsyncJobStatus = pydantic.Field(description="The status of the request.")
    request_time: Instant = pydantic.Field(
        alias="requestTime", description="Indicates the server's time when the query is requested."
    )
    transaction_time: typing.Optional[Instant] = pydantic.Field(
        alias="transactionTime",
        description="Indicates the server's time when the query is run. The response SHOULD NOT include any resources modified after this instant, and SHALL include any matching resources modified up to and including this instant.",
    )
    request: Uri = pydantic.Field(
        description="The full URL of the original kick-off request. In the case of a POST request, this URL will not include the request parameters."
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
