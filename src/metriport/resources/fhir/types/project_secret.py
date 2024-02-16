# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .decimal import Decimal

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProjectSecret(pydantic.BaseModel):
    """
    Secure environment variable that can be used to store secrets for bots.
    """

    name: str = pydantic.Field(description="The secret name.")
    value_string: typing.Optional[str] = pydantic.Field(alias="valueString", description="The secret value.")
    value_boolean: typing.Optional[bool] = pydantic.Field(alias="valueBoolean", description="The secret value.")
    value_decimal: typing.Optional[Decimal] = pydantic.Field(alias="valueDecimal", description="The secret value.")
    value_integer: typing.Optional[int] = pydantic.Field(alias="valueInteger", description="The secret value.")

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
