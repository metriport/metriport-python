# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .diagnostic_report_media import DiagnosticReportMedia
from .diagnostic_report_status import DiagnosticReportStatus
from .identifier import Identifier
from .instant import Instant
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DiagnosticReport(BaseResource):
    """
    The findings and interpretation of diagnostic tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.
    """

    resource_type: typing_extensions.Literal["DiagnosticReport"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifiers assigned to this report by the performer or other systems."
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn", description="Details concerning a service requested."
    )
    status: typing.Optional[DiagnosticReportStatus] = pydantic.Field(description="The status of the diagnostic report.")
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A code that classifies the clinical discipline, department or diagnostic service that created the report (e.g. cardiology, biochemistry, hematology, MRI). This is used for searching, sorting and display purposes."
    )
    code: CodeableConcept = pydantic.Field(description="A code or name that describes this diagnostic report.")
    subject: typing.Optional[Reference] = pydantic.Field(
        description="The subject of the report. Usually, but not always, this is a patient. However, diagnostic services also perform analyses on specimens collected from a variety of other sources."
    )
    encounter: typing.Optional[Reference] = pydantic.Field(
        description="The healthcare event (e.g. a patient and healthcare provider interaction) which this DiagnosticReport is about."
    )
    effective_date_time: typing.Optional[str] = pydantic.Field(
        alias="effectiveDateTime",
        description="The time or time-period the observed values are related to. When the subject of the report is a patient, this is usually either the time of the procedure or of specimen collection(s), but very often the source of the date/time is not known, only the date/time itself.",
    )
    effective_period: typing.Optional[Period] = pydantic.Field(
        alias="effectivePeriod",
        description="The time or time-period the observed values are related to. When the subject of the report is a patient, this is usually either the time of the procedure or of specimen collection(s), but very often the source of the date/time is not known, only the date/time itself.",
    )
    issued: typing.Optional[Instant] = pydantic.Field(
        description="The date and time that this version of the report was made available to providers, typically after the report was reviewed and verified."
    )
    performer: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="The diagnostic service that is responsible for issuing the report."
    )
    results_interpreter: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="resultsInterpreter",
        description="The practitioner or organization that is responsible for the report's conclusions and interpretations.",
    )
    specimen: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Details about the specimens on which this diagnostic report is based."
    )
    result: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="[Observations](observation.html) that are part of this diagnostic report."
    )
    imaging_study: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="imagingStudy",
        description="One or more links to full details of any imaging performed during the diagnostic investigation. Typically, this is imaging performed by DICOM enabled modalities, but this is not required. A fully enabled PACS viewer can use this information to provide views of the source images.",
    )
    media: typing.Optional[typing.List[DiagnosticReportMedia]] = pydantic.Field(
        description="A list of key images associated with this report. The images are generally created during the diagnostic process, and may be directly of the patient, or of treated specimens (i.e. slides of interest)."
    )
    conclusion: typing.Optional[str] = pydantic.Field(
        description="Concise and clinically contextualized summary conclusion (interpretation/impression) of the diagnostic report."
    )
    conclusion_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="conclusionCode",
        description="One or more codes that represent the summary conclusion (interpretation/impression) of the diagnostic report.",
    )
    presented_form: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        alias="presentedForm",
        description="Rich text representation of the entire result as issued by the diagnostic service. Multiple formats are allowed but they SHALL be semantically equivalent.",
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
