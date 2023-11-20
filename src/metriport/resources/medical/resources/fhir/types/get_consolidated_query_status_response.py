# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .patient_consolidated_data_status import PatientConsolidatedDataStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GetConsolidatedQueryStatusResponse(pydantic.BaseModel):
    """
    from metriport.resources.medical import (
        GetConsolidatedQueryStatusResponse,
        PatientConsolidatedDataStatus,
    )

    GetConsolidatedQueryStatusResponse(
        status=PatientConsolidatedDataStatus.COMPLETED,
        message="Trigger a new query by POST /patient/:id/consolidated/query; data will be sent through Webhook",
    )
    """

    status: PatientConsolidatedDataStatus
    message: typing.Optional[str]

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
