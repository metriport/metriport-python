# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .medication_knowledge_dosage import MedicationKnowledgeDosage
from .medication_knowledge_patient_characteristics import MedicationKnowledgePatientCharacteristics
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicationKnowledgeAdministrationGuidelines(pydantic.BaseModel):
    """
    Information about a medication that is used to support knowledge.
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
    dosage: typing.Optional[typing.List[MedicationKnowledgeDosage]] = pydantic.Field(
        description="Dosage for the medication for the specific guidelines."
    )
    indication_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="indicationCodeableConcept",
        description="Indication for use that apply to the specific administration guidelines.",
    )
    indication_reference: typing.Optional[Reference] = pydantic.Field(
        alias="indicationReference",
        description="Indication for use that apply to the specific administration guidelines.",
    )
    patient_characteristics: typing.Optional[typing.List[MedicationKnowledgePatientCharacteristics]] = pydantic.Field(
        alias="patientCharacteristics",
        description="Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).",
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
