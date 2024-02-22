# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .code import Code
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProjectMembershipAccessParameter(pydantic.BaseModel):
    """
    User options that control the display of the application.
    """

    name: Code = pydantic.Field(description="The unique name of the parameter.")
    value_string: typing.Optional[str] = pydantic.Field(
        alias="valueString",
        default=None,
        description="Value of the parameter - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
    )
    value_reference: typing.Optional[Reference] = pydantic.Field(
        alias="valueReference",
        default=None,
        description="Value of the parameter - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).",
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
