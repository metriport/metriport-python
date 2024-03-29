# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .markdown import Markdown
from .medication_knowledge_administration_guidelines import MedicationKnowledgeAdministrationGuidelines
from .medication_knowledge_cost import MedicationKnowledgeCost
from .medication_knowledge_drug_characteristic import MedicationKnowledgeDrugCharacteristic
from .medication_knowledge_ingredient import MedicationKnowledgeIngredient
from .medication_knowledge_kinetics import MedicationKnowledgeKinetics
from .medication_knowledge_medicine_classification import MedicationKnowledgeMedicineClassification
from .medication_knowledge_monitoring_program import MedicationKnowledgeMonitoringProgram
from .medication_knowledge_monograph import MedicationKnowledgeMonograph
from .medication_knowledge_packaging import MedicationKnowledgePackaging
from .medication_knowledge_regulatory import MedicationKnowledgeRegulatory
from .medication_knowledge_related_medication_knowledge import MedicationKnowledgeRelatedMedicationKnowledge
from .quantity import Quantity
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicationKnowledge(BaseResource):
    """
    Information about a medication that is used to support knowledge.
    """

    resource_type: typing.Literal["MedicationKnowledge"] = pydantic.Field(alias="resourceType")
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="A code that specifies this medication, or a textual description if no code is available. Usage note: This could be a standard medication code such as a code from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local formulary code, optionally with translations to other code systems.",
    )
    status: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="A code to indicate if the medication is in active use. The status refers to the validity about the information of the medication and not to its medicinal properties.",
    )
    manufacturer: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="Describes the details of the manufacturer of the medication product. This is not intended to represent the distributor of a medication product.",
    )
    dose_form: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="doseForm", default=None, description="Describes the form of the item. Powder; tablets; capsule."
    )
    amount: typing.Optional[Quantity] = pydantic.Field(
        default=None,
        description="Specific amount of the drug in the packaged product. For example, when specifying a product that has the same strength (For example, Insulin glargine 100 unit per mL solution for injection), this attribute provides additional clarification of the package amount (For example, 3 mL, 10mL, etc.).",
    )
    synonym: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None,
        description="Additional names for a medication, for example, the name(s) given to a medication in different countries. For example, acetaminophen and paracetamol or salbutamol and albuterol.",
    )
    related_medication_knowledge: typing.Optional[
        typing.List[MedicationKnowledgeRelatedMedicationKnowledge]
    ] = pydantic.Field(
        alias="relatedMedicationKnowledge",
        default=None,
        description="Associated or related knowledge about a medication.",
    )
    associated_medication: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="associatedMedication",
        default=None,
        description="Associated or related medications. For example, if the medication is a branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g. Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this would link to a branded product (e.g. Crestor).",
    )
    product_type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="productType",
        default=None,
        description="Category of the medication or product (e.g. branded product, therapeutic moeity, generic product, innovator product, etc.).",
    )
    monograph: typing.Optional[typing.List[MedicationKnowledgeMonograph]] = pydantic.Field(
        default=None, description="Associated documentation about the medication."
    )
    ingredient: typing.Optional[typing.List[MedicationKnowledgeIngredient]] = pydantic.Field(
        default=None, description="Identifies a particular constituent of interest in the product."
    )
    preparation_instruction: typing.Optional[Markdown] = pydantic.Field(
        alias="preparationInstruction", default=None, description="The instructions for preparing the medication."
    )
    intended_route: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="intendedRoute", default=None, description="The intended or approved route of administration."
    )
    cost: typing.Optional[typing.List[MedicationKnowledgeCost]] = pydantic.Field(
        default=None, description="The price of the medication."
    )
    monitoring_program: typing.Optional[typing.List[MedicationKnowledgeMonitoringProgram]] = pydantic.Field(
        alias="monitoringProgram", default=None, description="The program under which the medication is reviewed."
    )
    administration_guidelines: typing.Optional[
        typing.List[MedicationKnowledgeAdministrationGuidelines]
    ] = pydantic.Field(
        alias="administrationGuidelines",
        default=None,
        description="Guidelines for the administration of the medication.",
    )
    medicine_classification: typing.Optional[typing.List[MedicationKnowledgeMedicineClassification]] = pydantic.Field(
        alias="medicineClassification",
        default=None,
        description="Categorization of the medication within a formulary or classification system.",
    )
    packaging: typing.Optional[MedicationKnowledgePackaging] = pydantic.Field(
        default=None, description="Information that only applies to packages (not products)."
    )
    drug_characteristic: typing.Optional[typing.List[MedicationKnowledgeDrugCharacteristic]] = pydantic.Field(
        alias="drugCharacteristic",
        default=None,
        description="Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.",
    )
    contraindication: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description="Potential clinical issue with or between medication(s) (for example, drug-drug interaction, drug-disease contraindication, drug-allergy interaction, etc.).",
    )
    regulatory: typing.Optional[typing.List[MedicationKnowledgeRegulatory]] = pydantic.Field(
        default=None, description="Regulatory information about a medication."
    )
    kinetics: typing.Optional[typing.List[MedicationKnowledgeKinetics]] = pydantic.Field(
        default=None,
        description="The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.",
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
