# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .canonical import Canonical
from .code import Code
from .positive_int import PositiveInt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DataRequirement(pydantic.BaseModel):
    """
    Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    type: typing.Optional[Code] = pydantic.Field(
        description="The type of the required data, specified as the type name of a resource. For profiles, this value is set to the type of the base resource of the profile."
    )
    profile: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        description="The profile of the required data, specified as the uri of the profile definition."
    )
    subject_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="subjectCodeableConcept",
        description="The intended subjects of the data requirement. If this element is not provided, a Patient subject is assumed.",
    )
    subject_reference: typing.Optional[Reference] = pydantic.Field(
        alias="subjectReference",
        description="The intended subjects of the data requirement. If this element is not provided, a Patient subject is assumed.",
    )
    must_support: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="mustSupport",
        description="Indicates that specific elements of the type are referenced by the knowledge module and must be supported by the consumer in order to obtain an effective evaluation. This does not mean that a value is required for this element, only that the consuming system must understand the element and be able to provide values for it if they are available. The value of mustSupport SHALL be a FHIRPath resolveable on the type of the DataRequirement. The path SHALL consist only of identifiers, constant indexers, and .resolve() (see the [Simple FHIRPath Profile](fhirpath.html#simple) for full details).",
    )
    code_filter: typing.Optional[typing.List[DataRequirementCodeFilter]] = pydantic.Field(
        alias="codeFilter",
        description="Code filters specify additional constraints on the data, specifying the value set of interest for a particular element of the data. Each code filter defines an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.",
    )
    date_filter: typing.Optional[typing.List[DataRequirementDateFilter]] = pydantic.Field(
        alias="dateFilter",
        description="Date filters specify additional constraints on the data in terms of the applicable date range for specific elements. Each date filter specifies an additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.",
    )
    limit: typing.Optional[PositiveInt] = pydantic.Field(
        description="Specifies a maximum number of results that are required (uses the \_count search parameter)."
    )
    sort: typing.Optional[typing.List[DataRequirementSort]] = pydantic.Field(
        description="Specifies the order of the results to be returned."
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


from .codeable_concept import CodeableConcept  # noqa: E402
from .data_requirement_code_filter import DataRequirementCodeFilter  # noqa: E402
from .data_requirement_date_filter import DataRequirementDateFilter  # noqa: E402
from .data_requirement_sort import DataRequirementSort  # noqa: E402
from .extension import Extension  # noqa: E402
from .reference import Reference  # noqa: E402

DataRequirement.update_forward_refs()
