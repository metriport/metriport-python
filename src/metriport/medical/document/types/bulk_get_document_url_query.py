# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .document_query_status import DocumentQueryStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BulkGetDocumentUrlQuery(pydantic.BaseModel):
    """
    from metriport.medical import BulkGetDocumentUrlQuery, DocumentQueryStatus

    BulkGetDocumentUrlQuery(
        status=DocumentQueryStatus.PROCESSING,
        request_id="018c1e9d-dfce-70cb-8c0e-edfbbd2a7f5f",
    )
    """

    status: DocumentQueryStatus = pydantic.Field(description="The status of the URL generation process.")
    request_id: typing.Optional[str] = pydantic.Field(
        alias="requestId", default=None, description="The ID of the request."
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