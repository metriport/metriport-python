# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .group_characteristic import GroupCharacteristic
from .group_member import GroupMember
from .group_type import GroupType
from .identifier import Identifier
from .reference import Reference
from .unsigned_int import UnsignedInt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Group(BaseResource):
    """
    Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.
    """

    resource_type: typing.Literal["Group"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="A unique business identifier for this group."
    )
    active: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="Indicates whether the record for the group is available for use or is merely being retained for historical purposes.",
    )
    type: typing.Optional[GroupType] = pydantic.Field(
        default=None, description="Identifies the broad classification of the kind of resources the group includes."
    )
    actual: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="If true, indicates that the resource refers to a specific group of real individuals. If false, the group defines a set of intended individuals.",
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description='Provides a specific type of resource the group includes; e.g. "cow", "syringe", etc.'
    )
    name: typing.Optional[str] = pydantic.Field(
        default=None, description="A label assigned to the group for human identification and communication."
    )
    quantity: typing.Optional[UnsignedInt] = pydantic.Field(
        default=None, description="A count of the number of resource instances that are part of the group."
    )
    managing_entity: typing.Optional[Reference] = pydantic.Field(
        alias="managingEntity",
        default=None,
        description="Entity responsible for defining and maintaining Group characteristics and/or registered members.",
    )
    characteristic: typing.Optional[typing.List[GroupCharacteristic]] = pydantic.Field(
        default=None, description="Identifies traits whose presence r absence is shared by members of the group."
    )
    member: typing.Optional[typing.List[GroupMember]] = pydantic.Field(
        default=None, description="Identifies the resource instances that are members of the group."
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
