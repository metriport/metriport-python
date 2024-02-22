# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .explanation_of_benefit_accident import ExplanationOfBenefitAccident
from .explanation_of_benefit_add_item import ExplanationOfBenefitAddItem
from .explanation_of_benefit_adjudication import ExplanationOfBenefitAdjudication
from .explanation_of_benefit_benefit_balance import ExplanationOfBenefitBenefitBalance
from .explanation_of_benefit_care_team import ExplanationOfBenefitCareTeam
from .explanation_of_benefit_diagnosis import ExplanationOfBenefitDiagnosis
from .explanation_of_benefit_insurance import ExplanationOfBenefitInsurance
from .explanation_of_benefit_item import ExplanationOfBenefitItem
from .explanation_of_benefit_payee import ExplanationOfBenefitPayee
from .explanation_of_benefit_payment import ExplanationOfBenefitPayment
from .explanation_of_benefit_procedure import ExplanationOfBenefitProcedure
from .explanation_of_benefit_process_note import ExplanationOfBenefitProcessNote
from .explanation_of_benefit_related import ExplanationOfBenefitRelated
from .explanation_of_benefit_status import ExplanationOfBenefitStatus
from .explanation_of_benefit_supporting_info import ExplanationOfBenefitSupportingInfo
from .explanation_of_benefit_total import ExplanationOfBenefitTotal
from .identifier import Identifier
from .period import Period
from .positive_int import PositiveInt
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ExplanationOfBenefit(BaseResource):
    """
    This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    """

    resource_type: typing.Literal["ExplanationOfBenefit"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None, description="A unique identifier assigned to this explanation of benefit."
    )
    status: typing.Optional[ExplanationOfBenefitStatus] = pydantic.Field(
        default=None, description="The status of the resource instance."
    )
    type: CodeableConcept = pydantic.Field(
        description="The category of claim, e.g. oral, pharmacy, vision, institutional, professional."
    )
    sub_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="subType",
        default=None,
        description="A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty service.",
    )
    use: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the future.",
    )
    patient: Reference = pydantic.Field(
        description="The party to whom the professional services and/or products have been supplied or are being considered and for whom actual for forecast reimbursement is sought."
    )
    billable_period: typing.Optional[Period] = pydantic.Field(
        alias="billablePeriod", default=None, description="The period for which charges are being submitted."
    )
    created: typing.Optional[DateTime] = pydantic.Field(default=None, description="The date this resource was created.")
    enterer: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Individual who created the claim, predetermination or preauthorization."
    )
    insurer: Reference = pydantic.Field(
        description="The party responsible for authorization, adjudication and reimbursement."
    )
    provider: Reference = pydantic.Field(
        description="The provider which is responsible for the claim, predetermination or preauthorization."
    )
    priority: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="The provider-required urgency of processing the request. Typical values include: stat, routine deferred.",
    )
    funds_reserve_requested: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="fundsReserveRequested",
        default=None,
        description="A code to indicate whether and for whom funds are to be reserved for future claims.",
    )
    funds_reserve: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="fundsReserve",
        default=None,
        description="A code, used only on a response to a preauthorization, to indicate whether the benefits payable have been reserved and for whom.",
    )
    related: typing.Optional[typing.List[ExplanationOfBenefitRelated]] = pydantic.Field(
        default=None,
        description="Other claims which are related to this claim such as prior submissions or claims for related services or for the same event.",
    )
    prescription: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Prescription to support the dispensing of pharmacy, device or vision products."
    )
    original_prescription: typing.Optional[Reference] = pydantic.Field(
        alias="originalPrescription",
        default=None,
        description="Original prescription which has been superseded by this prescription to support the dispensing of pharmacy services, medications or products.",
    )
    payee: typing.Optional[ExplanationOfBenefitPayee] = pydantic.Field(
        default=None,
        description="The party to be reimbursed for cost of the products and services according to the terms of the policy.",
    )
    referral: typing.Optional[Reference] = pydantic.Field(
        default=None, description="A reference to a referral resource."
    )
    facility: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Facility where the services were provided."
    )
    claim: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="The business identifier for the instance of the adjudication request: claim predetermination or preauthorization.",
    )
    claim_response: typing.Optional[Reference] = pydantic.Field(
        alias="claimResponse",
        default=None,
        description="The business identifier for the instance of the adjudication response: claim, predetermination or preauthorization response.",
    )
    outcome: typing.Optional[Code] = pydantic.Field(
        default=None, description="The outcome of the claim, predetermination, or preauthorization processing."
    )
    disposition: typing.Optional[str] = pydantic.Field(
        default=None, description="A human readable description of the status of the adjudication."
    )
    pre_auth_ref: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="preAuthRef",
        default=None,
        description="Reference from the Insurer which is used in later communications which refers to this adjudication.",
    )
    pre_auth_ref_period: typing.Optional[typing.List[Period]] = pydantic.Field(
        alias="preAuthRefPeriod",
        default=None,
        description="The timeframe during which the supplied preauthorization reference may be quoted on claims to obtain the adjudication as provided.",
    )
    care_team: typing.Optional[typing.List[ExplanationOfBenefitCareTeam]] = pydantic.Field(
        alias="careTeam", default=None, description="The members of the team who provided the products and services."
    )
    supporting_info: typing.Optional[typing.List[ExplanationOfBenefitSupportingInfo]] = pydantic.Field(
        alias="supportingInfo",
        default=None,
        description="Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.",
    )
    diagnosis: typing.Optional[typing.List[ExplanationOfBenefitDiagnosis]] = pydantic.Field(
        default=None, description="Information about diagnoses relevant to the claim items."
    )
    procedure: typing.Optional[typing.List[ExplanationOfBenefitProcedure]] = pydantic.Field(
        default=None, description="Procedures performed on the patient relevant to the billing items with the claim."
    )
    precedence: typing.Optional[PositiveInt] = pydantic.Field(
        default=None,
        description="This indicates the relative order of a series of EOBs related to different coverages for the same suite of services.",
    )
    insurance: typing.List[ExplanationOfBenefitInsurance] = pydantic.Field(
        description="Financial instruments for reimbursement for the health care products and services specified on the claim."
    )
    accident: typing.Optional[ExplanationOfBenefitAccident] = pydantic.Field(
        default=None,
        description="Details of a accident which resulted in injuries which required the products and services listed in the claim.",
    )
    item: typing.Optional[typing.List[ExplanationOfBenefitItem]] = pydantic.Field(
        default=None,
        description="A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-details.",
    )
    add_item: typing.Optional[typing.List[ExplanationOfBenefitAddItem]] = pydantic.Field(
        alias="addItem",
        default=None,
        description="The first-tier service adjudications for payor added product or service lines.",
    )
    adjudication: typing.Optional[typing.List[ExplanationOfBenefitAdjudication]] = pydantic.Field(
        default=None,
        description="The adjudication results which are presented at the header level rather than at the line-item or add-item levels.",
    )
    total: typing.Optional[typing.List[ExplanationOfBenefitTotal]] = pydantic.Field(
        default=None, description="Categorized monetary totals for the adjudication."
    )
    payment: typing.Optional[ExplanationOfBenefitPayment] = pydantic.Field(
        default=None, description="Payment details for the adjudication of the claim."
    )
    form_code: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="formCode", default=None, description="A code for the form to be used for printing the content."
    )
    form: typing.Optional[Attachment] = pydantic.Field(
        default=None, description="The actual form, by reference or inclusion, for printing the content or an EOB."
    )
    process_note: typing.Optional[typing.List[ExplanationOfBenefitProcessNote]] = pydantic.Field(
        alias="processNote",
        default=None,
        description="A note that describes or explains adjudication results in a human readable form.",
    )
    benefit_period: typing.Optional[Period] = pydantic.Field(
        alias="benefitPeriod", default=None, description="The term of the benefits documented in this response."
    )
    benefit_balance: typing.Optional[typing.List[ExplanationOfBenefitBenefitBalance]] = pydantic.Field(
        alias="benefitBalance", default=None, description="Balance by Benefit Category."
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
