# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .dosage import Dosage
from .identifier import Identifier
from .medication_request_dispense_request import MedicationRequestDispenseRequest
from .medication_request_substitution import MedicationRequestSubstitution
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicationRequest(BaseResource):
    """
    An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
    """

    resource_type: typing.Literal["MedicationRequest"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Identifiers associated with this medication request that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to server.",
    )
    status: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="A code specifying the current state of the order. Generally, this will be active or completed state.",
    )
    status_reason: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="statusReason",
        default=None,
        description="Captures the reason for the current state of the MedicationRequest.",
    )
    intent: typing.Optional[Code] = pydantic.Field(
        default=None, description="Whether the request is a proposal, plan, or an original order."
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="Indicates the type of medication request (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient)).",
    )
    priority: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="Indicates how quickly the Medication Request should be addressed with respect to other requests.",
    )
    do_not_perform: typing.Optional[bool] = pydantic.Field(
        alias="doNotPerform",
        default=None,
        description="If true indicates that the provider is asking for the medication request not to occur.",
    )
    reported_boolean: typing.Optional[bool] = pydantic.Field(
        alias="reportedBoolean",
        default=None,
        description="Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record. It may also indicate the source of the report.",
    )
    reported_reference: typing.Optional[Reference] = pydantic.Field(
        alias="reportedReference",
        default=None,
        description="Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record. It may also indicate the source of the report.",
    )
    medication_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="medicationCodeableConcept",
        default=None,
        description="Identifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medications.",
    )
    medication_reference: typing.Optional[Reference] = pydantic.Field(
        alias="medicationReference",
        default=None,
        description="Identifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medications.",
    )
    subject: Reference = pydantic.Field(
        description="A link to a resource representing the person or set of individuals to whom the medication will be given."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The Encounter during which this [x] was created or to which the creation of this record is tightly associated.",
    )
    supporting_information: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="supportingInformation",
        default=None,
        description="Include additional information (for example, patient height and weight) that supports the ordering of the medication.",
    )
    authored_on: typing.Optional[DateTime] = pydantic.Field(
        alias="authoredOn",
        default=None,
        description="The date (and perhaps time) when the prescription was initially written or authored on.",
    )
    requester: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The individual, organization, or device that initiated the request and has responsibility for its activation.",
    )
    performer: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The specified desired performer of the medication treatment (e.g. the performer of the medication administration).",
    )
    performer_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="performerType",
        default=None,
        description="Indicates the type of performer of the administration of the medication.",
    )
    recorder: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The person who entered the order on behalf of another individual for example in the case of a verbal or a telephone order.",
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode",
        default=None,
        description="The reason or the indication for ordering or not ordering the medication.",
    )
    reason_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="reasonReference",
        default=None,
        description="Condition or observation that supports why the medication was ordered.",
    )
    instantiates_canonical: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="instantiatesCanonical",
        default=None,
        description="The URL pointing to a protocol, guideline, orderset, or other definition that is adhered to in whole or in part by this MedicationRequest.",
    )
    instantiates_uri: typing.Optional[typing.List[Uri]] = pydantic.Field(
        alias="instantiatesUri",
        default=None,
        description="The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this MedicationRequest.",
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn",
        default=None,
        description="A plan or request that is fulfilled in whole or in part by this medication request.",
    )
    group_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="groupIdentifier",
        default=None,
        description="A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition or prescription.",
    )
    course_of_therapy_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="courseOfTherapyType",
        default=None,
        description="The description of the overall patte3rn of the administration of the medication to the patient.",
    )
    insurance: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description="Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested service.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None,
        description="Extra information about the prescription that could not be conveyed by the other attributes.",
    )
    dosage_instruction: typing.Optional[typing.List[Dosage]] = pydantic.Field(
        alias="dosageInstruction",
        default=None,
        description="Indicates how the medication is to be used by the patient.",
    )
    dispense_request: typing.Optional[MedicationRequestDispenseRequest] = pydantic.Field(
        alias="dispenseRequest",
        default=None,
        description="Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order). Note that this information is not always sent with the order. There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy department.",
    )
    substitution: typing.Optional[MedicationRequestSubstitution] = pydantic.Field(
        default=None,
        description="Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be done.",
    )
    prior_prescription: typing.Optional[Reference] = pydantic.Field(
        alias="priorPrescription",
        default=None,
        description="A link to a resource representing an earlier order related order or prescription.",
    )
    detected_issue: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="detectedIssue",
        default=None,
        description="Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, duplicate therapy, dosage alert etc.",
    )
    event_history: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="eventHistory",
        default=None,
        description="Links to Provenance records for past versions of this resource or fulfilling request or event resources that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the resource.",
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
