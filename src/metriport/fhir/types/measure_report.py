# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .canonical import Canonical
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .measure_report_group import MeasureReportGroup
from .measure_report_status import MeasureReportStatus
from .measure_report_type import MeasureReportType
from .period import Period
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MeasureReport(BaseResource):
    """
    The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.
    """

    resource_type: typing.Literal["MeasureReport"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="A formal identifier that is used to identify this MeasureReport when it is represented in other formats or referenced in a specification, model, design or an instance.",
    )
    status: typing.Optional[MeasureReportStatus] = pydantic.Field(
        default=None,
        description="The MeasureReport status. No data will be available until the MeasureReport status is complete.",
    )
    type: typing.Optional[MeasureReportType] = pydantic.Field(
        default=None,
        description="The type of measure report. This may be an individual report, which provides the score for the measure for an individual member of the population; a subject-listing, which returns the list of members that meet the various criteria in the measure; a summary report, which returns a population count for each of the criteria in the measure; or a data-collection, which enables the MeasureReport to be used to exchange the data-of-interest for a quality measure.",
    )
    measure: Canonical = pydantic.Field(
        description="A reference to the Measure that was calculated to produce this report."
    )
    subject: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Optional subject identifying the individual or individuals the report is for."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        default=None, description="The date this measure report was generated."
    )
    reporter: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The individual, location, or organization that is reporting the data."
    )
    period: Period = pydantic.Field(description="The reporting period for which the report was calculated.")
    improvement_notation: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="improvementNotation",
        default=None,
        description="Whether improvement in the measure is noted by an increase or decrease in the measure score.",
    )
    group: typing.Optional[typing.List[MeasureReportGroup]] = pydantic.Field(
        default=None, description="The results of the calculation, one for each population group in the measure."
    )
    evaluated_resource: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="evaluatedResource",
        default=None,
        description="A reference to a Bundle containing the Resources that were used in the calculation of this measure.",
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
