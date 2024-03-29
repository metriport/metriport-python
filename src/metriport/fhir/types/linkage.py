# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .linkage_item import LinkageItem
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Linkage(BaseResource):
    """
    Identifies two or more records (resource instances) that refer to the same real-world "occurrence".
    """

    resource_type: typing.Literal["Linkage"] = pydantic.Field(alias="resourceType")
    active: typing.Optional[bool] = pydantic.Field(
        default=None, description='Indicates whether the asserted set of linkages are considered to be "in effect".'
    )
    author: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="Identifies the user or organization responsible for asserting the linkages as well as the user or organization who establishes the context in which the nature of each linkage is evaluated.",
    )
    item: typing.List[LinkageItem] = pydantic.Field(
        description="Identifies which record considered as the reference to the same real-world occurrence as well as how the items should be evaluated within the collection of linked items."
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
