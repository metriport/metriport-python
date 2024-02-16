# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .quantity import Quantity
from .ratio import Ratio

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicationAdministrationDosage(pydantic.BaseModel):
    """
    Describes the event of a patient consuming or otherwise being administered a medication. This may be as simple as swallowing a tablet or it may be a long running infusion. Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.
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
    text: typing.Optional[str] = pydantic.Field(
        description=(
            "Free text dosage can be used for cases where the dosage administered is too complex to code. When coded dosage is present, the free text dosage may still be present for display to humans.\n"
            "\n"
            "The dosage instructions should reflect the dosage of the medication that was administered.\n"
        )
    )
    site: typing.Optional[CodeableConcept] = pydantic.Field(
        description='A coded specification of the anatomic site where the medication first entered the body. For example, "left arm".'
    )
    route: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A code specifying the route or physiological path of administration of a therapeutic agent into or onto the patient. For example, topical, intravenous, etc."
    )
    method: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A coded value indicating the method by which the medication is intended to be or was introduced into or on the body. This attribute will most often NOT be populated. It is most commonly used for injections. For example, Slow Push, Deep IV."
    )
    dose: typing.Optional[Quantity] = pydantic.Field(
        description="The amount of the medication given at one administration event. Use this value when the administration is essentially an instantaneous event such as a swallowing a tablet or giving an injection."
    )
    rate_ratio: typing.Optional[Ratio] = pydantic.Field(
        alias="rateRatio",
        description="Identifies the speed with which the medication was or will be introduced into the patient. Typically, the rate for an infusion e.g. 100 ml per 1 hour or 100 ml/hr. May also be expressed as a rate per unit of time, e.g. 500 ml per 2 hours. Other examples: 200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.",
    )
    rate_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="rateQuantity",
        description="Identifies the speed with which the medication was or will be introduced into the patient. Typically, the rate for an infusion e.g. 100 ml per 1 hour or 100 ml/hr. May also be expressed as a rate per unit of time, e.g. 500 ml per 2 hours. Other examples: 200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.",
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
