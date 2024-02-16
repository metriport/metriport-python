# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.datetime_utils import serialize_datetime
from .payload_patient import PayloadPatient
from .webhook_metadata_payload import WebhookMetadataPayload

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class WebhookPatientConsolidatedDataPayload(pydantic.BaseModel):
    meta: WebhookMetadataPayload = pydantic.Field(description="The metadata of the webhook.")
    patients: typing.List[PayloadPatient] = pydantic.Field(description="An array of Payload Patient objects.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
