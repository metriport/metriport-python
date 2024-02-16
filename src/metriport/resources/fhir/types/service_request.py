# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .canonical import Canonical
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .reference import Reference
from .timing import Timing
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ServiceRequest(BaseResource):
    """
    A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    """

    resource_type: typing_extensions.Literal["ServiceRequest"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifiers assigned to this order instance by the orderer and/or the receiver and/or order fulfiller."
    )
    instantiates_canonical: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="instantiatesCanonical",
        description="The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this ServiceRequest.",
    )
    instantiates_uri: typing.Optional[typing.List[Uri]] = pydantic.Field(
        alias="instantiatesUri",
        description="The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this ServiceRequest.",
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn", description="Plan/proposal/order fulfilled by this request."
    )
    replaces: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The request takes the place of the referenced completed or terminated request(s)."
    )
    requisition: typing.Optional[Identifier] = pydantic.Field(
        description="A shared identifier common to all service requests that were authorized more or less simultaneously by a single author, representing the composite or group identifier."
    )
    status: typing.Optional[Code] = pydantic.Field(description="The status of the order.")
    intent: typing.Optional[Code] = pydantic.Field(
        description="Whether the request is a proposal, plan, an original order or a reflex order."
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description='A code that classifies the service for searching, sorting and display purposes (e.g. "Surgical Procedure").'
    )
    priority: typing.Optional[Code] = pydantic.Field(
        description="Indicates how quickly the ServiceRequest should be addressed with respect to other requests."
    )
    do_not_perform: typing.Optional[bool] = pydantic.Field(
        alias="doNotPerform",
        description="Set this to true if the record is saying that the service/procedure should NOT be performed.",
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A code that identifies a particular service (i.e., procedure, diagnostic investigation, or panel of investigations) that have been requested."
    )
    order_detail: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="orderDetail",
        description="Additional details and instructions about the how the services are to be delivered. For example, and order for a urinary catheter may have an order detail for an external or indwelling catheter, or an order for a bandage may require additional instructions specifying how the bandage should be applied.",
    )
    quantity_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="quantityQuantity",
        description="An amount of service being requested which can be a quantity ( for example $1,500 home modification), a ratio ( for example, 20 half day visits per month), or a range (2.0 to 1.8 Gy per fraction).",
    )
    quantity_ratio: typing.Optional[Ratio] = pydantic.Field(
        alias="quantityRatio",
        description="An amount of service being requested which can be a quantity ( for example $1,500 home modification), a ratio ( for example, 20 half day visits per month), or a range (2.0 to 1.8 Gy per fraction).",
    )
    quantity_range: typing.Optional[Range] = pydantic.Field(
        alias="quantityRange",
        description="An amount of service being requested which can be a quantity ( for example $1,500 home modification), a ratio ( for example, 20 half day visits per month), or a range (2.0 to 1.8 Gy per fraction).",
    )
    subject: Reference = pydantic.Field(
        description="On whom or what the service is to be performed. This is usually a human patient, but can also be requested on animals, groups of humans or animals, devices such as dialysis machines, or even locations (typically for environmental scans)."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        description="An encounter that provides additional information about the healthcare context in which this request is made."
    )
    occurrence_date_time: typing.Optional[str] = pydantic.Field(
        alias="occurrenceDateTime", description="The date/time at which the requested service should occur."
    )
    occurrence_period: typing.Optional[Period] = pydantic.Field(
        alias="occurrencePeriod", description="The date/time at which the requested service should occur."
    )
    occurrence_timing: typing.Optional[Timing] = pydantic.Field(
        alias="occurrenceTiming", description="The date/time at which the requested service should occur."
    )
    as_needed_boolean: typing.Optional[bool] = pydantic.Field(
        alias="asNeededBoolean",
        description='If a CodeableConcept is present, it indicates the pre-condition for performing the service. For example "pain", "on flare-up", etc.',
    )
    as_needed_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="asNeededCodeableConcept",
        description='If a CodeableConcept is present, it indicates the pre-condition for performing the service. For example "pain", "on flare-up", etc.',
    )
    authored_on: typing.Optional[DateTime] = pydantic.Field(
        alias="authoredOn", description="When the request transitioned to being actionable."
    )
    requester: typing.Optional[Reference] = pydantic.Field(
        description="The individual who initiated the request and has responsibility for its activation."
    )
    performer_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="performerType", description="Desired type of performer for doing the requested service."
    )
    performer: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The desired performer for doing the requested service. For example, the surgeon, dermatopathologist, endoscopist, etc."
    )
    location_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="locationCode",
        description="The preferred location(s) where the procedure should actually happen in coded or free text form. E.g. at home or nursing day care center.",
    )
    location_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="locationReference",
        description="A reference to the the preferred location(s) where the procedure should actually happen. E.g. at home or nursing day care center.",
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode",
        description="An explanation or justification for why this service is being requested in coded or textual form. This is often for billing purposes. May relate to the resources referred to in `supportingInfo`.",
    )
    reason_reference: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="reasonReference",
        description="Indicates another resource that provides a justification for why this service is being requested. May relate to the resources referred to in `supportingInfo`.",
    )
    insurance: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be needed for delivering the requested service."
    )
    supporting_info: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="supportingInfo",
        description='Additional clinical information about the patient or specimen that may influence the services or their interpretations. This information includes diagnosis, clinical findings and other observations. In laboratory ordering these are typically referred to as "ask at order entry questions (AOEs)". This includes observations explicitly requested by the producer (filler) to provide context or supporting information needed to complete the order. For example, reporting the amount of inspired oxygen for blood gas measurements.',
    )
    specimen: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="One or more specimens that the laboratory procedure will use."
    )
    body_site: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="bodySite",
        description="Anatomic location where the procedure should be performed. This is the target site.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Any other notes and comments made about the service request. For example, internal billing notes."
    )
    patient_instruction: typing.Optional[str] = pydantic.Field(
        alias="patientInstruction", description="Instructions in terms that are understood by the patient or consumer."
    )
    relevant_history: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="relevantHistory", description="Key events in the history of the request."
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
