# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .age import Age
from .annotation import Annotation
from .codeable_concept import CodeableConcept
from .extension import Extension
from .period import Period
from .range import Range

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FamilyMemberHistoryCondition(pydantic.BaseModel):
    """
    Significant health conditions for a person related to the patient relevant in the context of care for the patient.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    code: CodeableConcept = pydantic.Field(
        description="The actual condition specified. Could be a coded condition (like MI or Diabetes) or a less specific string like 'cancer' depending on how much is known about the condition and the capabilities of the creating system."
    )
    outcome: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="Indicates what happened following the condition. If the condition resulted in death, deceased date is captured on the relation.",
    )
    contributed_to_death: typing.Optional[bool] = pydantic.Field(
        alias="contributedToDeath",
        default=None,
        description="This condition contributed to the cause of death of the related person. If contributedToDeath is not populated, then it is unknown.",
    )
    onset_age: typing.Optional[Age] = pydantic.Field(
        alias="onsetAge",
        default=None,
        description="Either the age of onset, range of approximate age or descriptive string can be recorded. For conditions with multiple occurrences, this describes the first known occurrence.",
    )
    onset_range: typing.Optional[Range] = pydantic.Field(
        alias="onsetRange",
        default=None,
        description="Either the age of onset, range of approximate age or descriptive string can be recorded. For conditions with multiple occurrences, this describes the first known occurrence.",
    )
    onset_period: typing.Optional[Period] = pydantic.Field(
        alias="onsetPeriod",
        default=None,
        description="Either the age of onset, range of approximate age or descriptive string can be recorded. For conditions with multiple occurrences, this describes the first known occurrence.",
    )
    onset_string: typing.Optional[str] = pydantic.Field(
        alias="onsetString",
        default=None,
        description="Either the age of onset, range of approximate age or descriptive string can be recorded. For conditions with multiple occurrences, this describes the first known occurrence.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None, description="An area where general notes can be placed about this specific condition."
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
