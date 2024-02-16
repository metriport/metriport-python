# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.datetime_utils import serialize_datetime
from .....commons.types.address import Address
from .org_type import OrgType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OrganizationCreate(pydantic.BaseModel):
    name: str = pydantic.Field(
        description=(
            "The name of your organization.\n"
            "This is usually your legal corporate entity name -\n"
            "for example `Metriport Inc.`.\n"
        )
    )
    type: OrgType = pydantic.Field(description="The type of your organization.")
    location: Address

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
