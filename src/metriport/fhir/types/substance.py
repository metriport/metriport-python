# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .substance_ingredient import SubstanceIngredient
from .substance_instance import SubstanceInstance
from .substance_status import SubstanceStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Substance(BaseResource):
    """
    A homogeneous material with a definite composition.
    """

    resource_type: typing.Literal["Substance"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Unique identifier for the substance."
    )
    status: typing.Optional[SubstanceStatus] = pydantic.Field(
        description="A code to indicate if the substance is actively used."
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A code that classifies the general type of substance. This is used for searching, sorting and display purposes."
    )
    code: CodeableConcept = pydantic.Field(description="A code (or set of codes) that identify this substance.")
    description: typing.Optional[str] = pydantic.Field(
        description="A description of the substance - its appearance, handling requirements, and other usage notes."
    )
    instance: typing.Optional[typing.List[SubstanceInstance]] = pydantic.Field(
        description="Substance may be used to describe a kind of substance, or a specific package/container of the substance: an instance."
    )
    ingredient: typing.Optional[typing.List[SubstanceIngredient]] = pydantic.Field(
        description="A substance can be composed of other substances."
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
