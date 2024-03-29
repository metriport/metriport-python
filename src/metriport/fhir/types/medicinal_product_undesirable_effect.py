# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .population import Population
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicinalProductUndesirableEffect(BaseResource):
    """
    Describe the undesirable effects of the medicinal product.
    """

    resource_type: typing.Literal["MedicinalProductUndesirableEffect"] = pydantic.Field(alias="resourceType")
    subject: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="The medication for which this is an indication."
    )
    symptom_condition_effect: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="symptomConditionEffect", default=None, description="The symptom, condition or undesirable effect."
    )
    classification: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="Classification of the effect."
    )
    frequency_of_occurrence: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="frequencyOfOccurrence", default=None, description="The frequency of occurrence of the effect."
    )
    population: typing.Optional[typing.List[Population]] = pydantic.Field(
        default=None, description="The population group to which this applies."
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
