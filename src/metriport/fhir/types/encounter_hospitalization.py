# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .identifier import Identifier
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EncounterHospitalization(pydantic.BaseModel):
    """
    An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
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
    pre_admission_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="preAdmissionIdentifier", default=None, description="Pre-admission identifier."
    )
    origin: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The location/organization from which the patient came before admission."
    )
    admit_source: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="admitSource", default=None, description="From where patient was admitted (physician referral, transfer)."
    )
    re_admission: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="reAdmission", default=None, description="Whether this hospitalization is a readmission and why if known."
    )
    diet_preference: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="dietPreference", default=None, description="Diet preferences reported by the patient."
    )
    special_courtesy: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="specialCourtesy", default=None, description="Special courtesies (VIP, board member)."
    )
    special_arrangement: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="specialArrangement",
        default=None,
        description="Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other things.",
    )
    destination: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Location/organization to which the patient is discharged."
    )
    discharge_disposition: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="dischargeDisposition", default=None, description="Category or kind of location after discharge."
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
