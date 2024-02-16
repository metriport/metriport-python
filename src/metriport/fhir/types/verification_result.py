# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .reference import Reference
from .timing import Timing
from .verification_result_attestation import VerificationResultAttestation
from .verification_result_primary_source import VerificationResultPrimarySource
from .verification_result_validator import VerificationResultValidator

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class VerificationResult(BaseResource):
    """
    Describes validation requirements, source(s), status and dates for one or more elements.
    """

    resource_type: typing_extensions.Literal["VerificationResult"] = pydantic.Field(alias="resourceType")
    target: typing.Optional[typing.List[Reference]] = pydantic.Field(description="A resource that was validated.")
    target_location: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="targetLocation", description="The fhirpath location(s) within the resource that was validated."
    )
    need: typing.Optional[CodeableConcept] = pydantic.Field(
        description="The frequency with which the target must be validated (none; initial; periodic)."
    )
    status: typing.Optional[Code] = pydantic.Field(
        description="The validation status of the target (attested; validated; in process; requires revalidation; validation failed; revalidation failed)."
    )
    status_date: typing.Optional[DateTime] = pydantic.Field(
        alias="statusDate", description="When the validation status was updated."
    )
    validation_type: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="validationType",
        description="What the target is validated against (nothing; primary source; multiple sources).",
    )
    validation_process: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="validationProcess",
        description="The primary process by which the target is validated (edit check; value set; primary source; multiple sources; standalone; in context).",
    )
    frequency: typing.Optional[Timing] = pydantic.Field(description="Frequency of revalidation.")
    last_performed: typing.Optional[DateTime] = pydantic.Field(
        alias="lastPerformed", description="The date/time validation was last completed (including failed validations)."
    )
    next_scheduled: typing.Optional[dt.date] = pydantic.Field(
        alias="nextScheduled", description="The date when target is next validated, if appropriate."
    )
    failure_action: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="failureAction", description="The result if validation fails (fatal; warning; record only; none)."
    )
    primary_source: typing.Optional[typing.List[VerificationResultPrimarySource]] = pydantic.Field(
        alias="primarySource", description="Information about the primary source(s) involved in validation."
    )
    attestation: typing.Optional[VerificationResultAttestation] = pydantic.Field(
        description="Information about the entity attesting to information."
    )
    validator: typing.Optional[typing.List[VerificationResultValidator]] = pydantic.Field(
        description="Information about the entity validating information."
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