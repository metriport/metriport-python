# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .coverage_class import CoverageClass
from .coverage_cost_to_beneficiary import CoverageCostToBeneficiary
from .identifier import Identifier
from .period import Period
from .positive_int import PositiveInt
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Coverage(BaseResource):
    """
    Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    """

    resource_type: typing_extensions.Literal["Coverage"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="A unique identifier assigned to this coverage."
    )
    status: typing.Optional[Code] = pydantic.Field(description="The status of the resource instance.")
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        description="The type of coverage: social program, medical plan, accident coverage (workers compensation, auto), group health or payment by an individual or organization."
    )
    policy_holder: typing.Optional[Reference] = pydantic.Field(
        alias="policyHolder", description="The party who 'owns' the insurance policy."
    )
    subscriber: typing.Optional[Reference] = pydantic.Field(
        description="The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due."
    )
    subscriber_id: typing.Optional[str] = pydantic.Field(
        alias="subscriberId", description="The insurer assigned ID for the Subscriber."
    )
    beneficiary: Reference = pydantic.Field(
        description="The party who benefits from the insurance coverage; the patient when products and/or services are provided."
    )
    dependent: typing.Optional[str] = pydantic.Field(
        description="A unique identifier for a dependent under the coverage."
    )
    relationship: typing.Optional[CodeableConcept] = pydantic.Field(
        description="The relationship of beneficiary (patient) to the subscriber."
    )
    period: typing.Optional[Period] = pydantic.Field(
        description="Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force."
    )
    payor: typing.List[Reference] = pydantic.Field(
        description="The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements."
    )
    class_: typing.Optional[typing.List[CoverageClass]] = pydantic.Field(
        alias="class", description="A suite of underwriter specific classifiers."
    )
    order: typing.Optional[PositiveInt] = pydantic.Field(
        description="The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care."
    )
    network: typing.Optional[str] = pydantic.Field(
        description="The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply."
    )
    cost_to_beneficiary: typing.Optional[typing.List[CoverageCostToBeneficiary]] = pydantic.Field(
        alias="costToBeneficiary",
        description="A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been included on the health card.",
    )
    subrogation: typing.Optional[bool] = pydantic.Field(
        description="When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs."
    )
    contract: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The policy(s) which constitute this insurance coverage."
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