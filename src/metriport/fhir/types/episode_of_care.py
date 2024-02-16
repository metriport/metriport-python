# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .episode_of_care_diagnosis import EpisodeOfCareDiagnosis
from .episode_of_care_status import EpisodeOfCareStatus
from .episode_of_care_status_history import EpisodeOfCareStatusHistory
from .identifier import Identifier
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EpisodeOfCare(BaseResource):
    """
    An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.
    """

    resource_type: typing_extensions.Literal["EpisodeOfCare"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="The EpisodeOfCare may be known by different identifiers for different contexts of use, such as when an external agency is tracking the Episode for funding purposes."
    )
    status: typing.Optional[EpisodeOfCareStatus] = pydantic.Field(
        description=("planned \n" " waitlist \n" " active \n" " onhold \n" " finished \n" " cancelled.\n")
    )
    status_history: typing.Optional[typing.List[EpisodeOfCareStatusHistory]] = pydantic.Field(
        alias="statusHistory",
        description="The history of statuses that the EpisodeOfCare has been through (without requiring processing the history of the resource).",
    )
    type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A classification of the type of episode of care; e.g. specialist referral, disease management, type of funded care."
    )
    diagnosis: typing.Optional[typing.List[EpisodeOfCareDiagnosis]] = pydantic.Field(
        description="The list of diagnosis relevant to this episode of care."
    )
    patient: Reference = pydantic.Field(description="The patient who is the focus of this episode of care.")
    managing_organization: typing.Optional[Reference] = pydantic.Field(
        alias="managingOrganization",
        description="The organization that has assumed the specific responsibilities for the specified duration.",
    )
    period: typing.Optional[Period] = pydantic.Field(
        description="The interval during which the managing organization assumes the defined responsibility."
    )
    referral_request: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="referralRequest",
        description="Referral Request(s) that are fulfilled by this EpisodeOfCare, incoming referrals.",
    )
    care_manager: typing.Optional[Reference] = pydantic.Field(
        alias="careManager", description="The practitioner that is the care manager/care coordinator for this patient."
    )
    team: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The list of practitioners that may be facilitating this episode of care for specific purposes."
    )
    account: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The set of accounts that may be used for billing for this EpisodeOfCare."
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