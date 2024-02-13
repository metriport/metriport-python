# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .filter import Filter

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ConsolidatedCountResponse(pydantic.BaseModel):
    total: int = pydantic.Field(description="The sum of all resource type count.")
    resources: typing.Dict[str, int] = pydantic.Field(
        description=(
            "Object containing resource types as properties and the amount of entries for\n"
            "the resource as the value (integer). Only resource types with amount\n"
            "of entries higher than one are included.\n"
        )
    )
    filter: Filter = pydantic.Field(description="The filters used to perform this operation.")

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
