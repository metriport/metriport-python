# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .immunization_recommendation_date_criterion import ImmunizationRecommendationDateCriterion
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ImmunizationRecommendationRecommendation(pydantic.BaseModel):
    """
    A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    vaccine_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="vaccineCode", default=None, description="Vaccine(s) or vaccine group that pertain to the recommendation."
    )
    target_disease: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="targetDisease", default=None, description="The targeted disease for the recommendation."
    )
    contraindicated_vaccine_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="contraindicatedVaccineCode",
        default=None,
        description="Vaccine(s) which should not be used to fulfill the recommendation.",
    )
    forecast_status: CodeableConcept = pydantic.Field(
        alias="forecastStatus",
        description="Indicates the patient status with respect to the path to immunity for the target disease.",
    )
    forecast_reason: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="forecastReason", default=None, description="The reason for the assigned forecast status."
    )
    date_criterion: typing.Optional[typing.List[ImmunizationRecommendationDateCriterion]] = pydantic.Field(
        alias="dateCriterion",
        default=None,
        description="Vaccine date recommendations. For example, earliest date to administer, latest date to administer, etc.",
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Contains the description about the protocol under which the vaccine was administered.",
    )
    series: typing.Optional[str] = pydantic.Field(
        default=None,
        description="One possible path to achieve presumed immunity against a disease - within the context of an authority.",
    )
    dose_number_positive_int: typing.Optional[float] = pydantic.Field(
        alias="doseNumberPositiveInt",
        default=None,
        description="Nominal position of the recommended dose in a series (e.g. dose 2 is the next recommended dose).",
    )
    dose_number_string: typing.Optional[str] = pydantic.Field(
        alias="doseNumberString",
        default=None,
        description="Nominal position of the recommended dose in a series (e.g. dose 2 is the next recommended dose).",
    )
    series_doses_positive_int: typing.Optional[float] = pydantic.Field(
        alias="seriesDosesPositiveInt", default=None, description="The recommended number of doses to achieve immunity."
    )
    series_doses_string: typing.Optional[str] = pydantic.Field(
        alias="seriesDosesString", default=None, description="The recommended number of doses to achieve immunity."
    )
    supporting_immunization: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="supportingImmunization",
        default=None,
        description="Immunization event history and/or evaluation that supports the status and recommendation.",
    )
    supporting_patient_information: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="supportingPatientInformation",
        default=None,
        description="Patient Information that supports the status and recommendation. This includes patient observations, adverse reactions and allergy/intolerance information.",
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
