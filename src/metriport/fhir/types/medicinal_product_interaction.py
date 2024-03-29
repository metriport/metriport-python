# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .medicinal_product_interaction_interactant import MedicinalProductInteractionInteractant
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicinalProductInteraction(BaseResource):
    """
    The interactions of the medicinal product with other medicinal products, or other forms of interactions.
    """

    resource_type: typing.Literal["MedicinalProductInteraction"] = pydantic.Field(alias="resourceType")
    subject: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="The medication for which this is a described interaction."
    )
    description: typing.Optional[str] = pydantic.Field(default=None, description="The interaction described.")
    interactant: typing.Optional[typing.List[MedicinalProductInteractionInteractant]] = pydantic.Field(
        default=None, description="The specific medication, food or laboratory test that interacts."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="The type of the interaction e.g. drug-drug interaction, drug-food interaction, drug-lab test interaction.",
    )
    effect: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description='The effect of the interaction, for example "reduced gastric absorption of primary medication".',
    )
    incidence: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="The incidence of the interaction, e.g. theoretical, observed."
    )
    management: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="Actions for managing the interaction."
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
