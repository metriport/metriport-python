# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .decimal import Decimal
from .extension import Extension
from .period import Period
from .range import Range

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RiskAssessmentPrediction(pydantic.BaseModel):
    """
    An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
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
    outcome: typing.Optional[CodeableConcept] = pydantic.Field(
        description="One of the potential outcomes for the patient (e.g. remission, death, a particular condition)."
    )
    probability_decimal: typing.Optional[float] = pydantic.Field(
        alias="probabilityDecimal", description="Indicates how likely the outcome is (in the specified timeframe)."
    )
    probability_range: typing.Optional[Range] = pydantic.Field(
        alias="probabilityRange", description="Indicates how likely the outcome is (in the specified timeframe)."
    )
    qualitative_risk: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="qualitativeRisk",
        description="Indicates how likely the outcome is (in the specified timeframe), expressed as a qualitative value (e.g. low, medium, or high).",
    )
    relative_risk: typing.Optional[Decimal] = pydantic.Field(
        alias="relativeRisk",
        description="Indicates the risk for this particular subject (with their specific characteristics) divided by the risk of the population in general. (Numbers greater than 1 = higher risk than the population, numbers less than 1 = lower risk.).",
    )
    when_period: typing.Optional[Period] = pydantic.Field(
        alias="whenPeriod",
        description="Indicates the period of time or age range of the subject to which the specified probability applies.",
    )
    when_range: typing.Optional[Range] = pydantic.Field(
        alias="whenRange",
        description="Indicates the period of time or age range of the subject to which the specified probability applies.",
    )
    rationale: typing.Optional[str] = pydantic.Field(
        description="Additional information explaining the basis for the prediction."
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