# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .observation_reference_range import ObservationReferenceRange
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .sampled_data import SampledData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ObservationComponent(pydantic.BaseModel):
    """
    Measurements and simple assertions made about a patient, device or other subject.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    code: CodeableConcept = pydantic.Field(
        description='Describes what was observed. Sometimes this is called the observation "code".'
    )
    value_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="valueQuantity",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="valueCodeableConcept",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_string: typing.Optional[str] = pydantic.Field(
        alias="valueString",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_boolean: typing.Optional[bool] = pydantic.Field(
        alias="valueBoolean",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_integer: typing.Optional[float] = pydantic.Field(
        alias="valueInteger",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_range: typing.Optional[Range] = pydantic.Field(
        alias="valueRange",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_ratio: typing.Optional[Ratio] = pydantic.Field(
        alias="valueRatio",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_sampled_data: typing.Optional[SampledData] = pydantic.Field(
        alias="valueSampledData",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_time: typing.Optional[str] = pydantic.Field(
        alias="valueTime",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_date_time: typing.Optional[str] = pydantic.Field(
        alias="valueDateTime",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    value_period: typing.Optional[Period] = pydantic.Field(
        alias="valuePeriod",
        description="The information determined as a result of making the observation, if the information has a simple value.",
    )
    data_absent_reason: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="dataAbsentReason",
        description="Provides a reason why the expected value in the element Observation.component.value[x] is missing.",
    )
    interpretation: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A categorical assessment of an observation value. For example, high, low, normal."
    )
    reference_range: typing.Optional[typing.List[ObservationReferenceRange]] = pydantic.Field(
        alias="referenceRange",
        description="Guidance on how to interpret the value by comparison to a normal or recommended range.",
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