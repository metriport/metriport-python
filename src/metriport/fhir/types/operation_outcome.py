# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .operation_outcome_issue import OperationOutcomeIssue

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OperationOutcome(BaseResource):
    """
    A collection of error, warning, or information messages that result from a system action.
    """

    resource_type: typing_extensions.Literal["OperationOutcome"] = pydantic.Field(alias="resourceType")
    issue: typing.List[OperationOutcomeIssue] = pydantic.Field(
        description="An error, warning, or information message that results from a system action."
    )
    status: typing.Optional[int] = pydantic.Field(description="Optional HTTP status code returned by the operation.")
    resource: typing.Any = pydantic.Field(description="Optional Resource created or modified by this operation.")

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