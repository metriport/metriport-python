# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .expression import Expression
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AccessPolicyResource(pydantic.BaseModel):
    """
    Access details for a resource type.
    """

    compartment: typing.Optional[Reference] = pydantic.Field(
        default=None, description="DEPRECATED Optional compartment restriction for the resource type."
    )
    criteria: typing.Optional[str] = pydantic.Field(
        default=None, description="The rules that the server should use to determine which resources to allow."
    )
    readonly: typing.Optional[bool] = pydantic.Field(
        default=None, description="Optional flag to indicate that the resource type is read-only."
    )
    hidden_fields: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="hiddenFields",
        default=None,
        description="Optional list of hidden fields. Hidden fields are not readable or writeable.",
    )
    readonly_fields: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="readonlyFields",
        default=None,
        description="Optional list of read-only fields. Read-only fields are readable but not writeable.",
    )
    write_constraint: typing.Optional[typing.List[Expression]] = pydantic.Field(
        alias="writeConstraint",
        default=None,
        description="Invariants that must be satisfied for the resource to be written. Can include %before and %after placeholders to refer to the resource before and after the updates are applied.",
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
