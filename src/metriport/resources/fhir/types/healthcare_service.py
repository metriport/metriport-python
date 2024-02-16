# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_point import ContactPoint
from .healthcare_service_available_time import HealthcareServiceAvailableTime
from .healthcare_service_eligibility import HealthcareServiceEligibility
from .healthcare_service_not_available import HealthcareServiceNotAvailable
from .identifier import Identifier
from .markdown import Markdown
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HealthcareService(BaseResource):
    """
    The details of a healthcare service available at a location.
    """

    resource_type: typing_extensions.Literal["HealthcareService"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="External identifiers for this item."
    )
    active: typing.Optional[bool] = pydantic.Field(
        description="This flag is used to mark the record to not be used. This is not used when a center is closed for maintenance, or for holidays, the notAvailable period is to be used for this."
    )
    provided_by: typing.Optional[Reference] = pydantic.Field(
        alias="providedBy", description="The organization that provides this healthcare service."
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Identifies the broad category of service being performed or delivered."
    )
    type: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="The specific type of service that may be delivered or performed."
    )
    specialty: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Collection of specialties handled by the service site. This is more of a medical term."
    )
    location: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The location(s) where this healthcare service may be provided."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="Further description of the service as it would be presented to a consumer while searching."
    )
    comment: typing.Optional[str] = pydantic.Field(
        description="Any additional description of the service and/or any specific issues not covered by the other attributes, which can be displayed as further detail under the serviceName."
    )
    extra_details: typing.Optional[Markdown] = pydantic.Field(
        alias="extraDetails", description="Extra details about the service that can't be placed in the other fields."
    )
    photo: typing.Optional[Attachment] = pydantic.Field(
        description="If there is a photo/symbol associated with this HealthcareService, it may be included here to facilitate quick identification of the service in a list."
    )
    telecom: typing.Optional[typing.List[ContactPoint]] = pydantic.Field(
        description="List of contacts related to this specific healthcare service."
    )
    coverage_area: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="coverageArea",
        description="The location(s) that this service is available to (not where the service is provided).",
    )
    service_provision_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="serviceProvisionCode",
        description="The code(s) that detail the conditions under which the healthcare service is available/offered.",
    )
    eligibility: typing.Optional[typing.List[HealthcareServiceEligibility]] = pydantic.Field(
        description="Does this service have specific eligibility requirements that need to be met in order to use the service?"
    )
    program: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Programs that this service is applicable to."
    )
    characteristic: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Collection of characteristics (attributes)."
    )
    communication: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Some services are specifically made available in multiple languages, this property permits a directory to declare the languages this is offered in. Typically this is only provided where a service operates in communities with mixed languages used."
    )
    referral_method: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="referralMethod",
        description="Ways that the service accepts referrals, if this is not provided then it is implied that no referral is required.",
    )
    appointment_required: typing.Optional[bool] = pydantic.Field(
        alias="appointmentRequired",
        description="Indicates whether or not a prospective consumer will require an appointment for a particular service at a site to be provided by the Organization. Indicates if an appointment is required for access to this service.",
    )
    available_time: typing.Optional[typing.List[HealthcareServiceAvailableTime]] = pydantic.Field(
        alias="availableTime", description="A collection of times that the Service Site is available."
    )
    not_available: typing.Optional[typing.List[HealthcareServiceNotAvailable]] = pydantic.Field(
        alias="notAvailable",
        description="The HealthcareService is not available during this period of time due to the provided reason.",
    )
    availability_exceptions: typing.Optional[str] = pydantic.Field(
        alias="availabilityExceptions",
        description="A description of site availability exceptions, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as details in the available Times and not available Times.",
    )
    endpoint: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Technical endpoints providing access to services operated for the specific healthcare services defined at this resource."
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
