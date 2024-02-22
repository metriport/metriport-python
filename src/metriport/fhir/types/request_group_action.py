# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .age import Age
from .code import Code
from .codeable_concept import CodeableConcept
from .duration import Duration
from .extension import Extension
from .period import Period
from .range import Range
from .reference import Reference
from .related_artifact import RelatedArtifact
from .request_group_condition import RequestGroupCondition
from .request_group_related_action import RequestGroupRelatedAction
from .timing import Timing

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RequestGroupAction(pydantic.BaseModel):
    """
    A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
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
    prefix: typing.Optional[str] = pydantic.Field(default=None, description="A user-visible prefix for the action.")
    title: typing.Optional[str] = pydantic.Field(
        default=None, description="The title of the action displayed to a user."
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None, description="A short description of the action used to provide a summary to display to the user."
    )
    text_equivalent: typing.Optional[str] = pydantic.Field(
        alias="textEquivalent",
        default=None,
        description="A text equivalent of the action to be performed. This provides a human-interpretable description of the action when the definition is consumed by a system that might not be capable of interpreting it dynamically.",
    )
    priority: typing.Optional[Code] = pydantic.Field(
        default=None, description="Indicates how quickly the action should be addressed with respect to other actions."
    )
    code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="A code that provides meaning for the action or action group. For example, a section may have a LOINC code for a section of a documentation template.",
    )
    documentation: typing.Optional[typing.List[RelatedArtifact]] = pydantic.Field(
        default=None,
        description="Didactic or other informational resources associated with the action that can be provided to the CDS recipient. Information resources can include inline text commentary and links to web resources.",
    )
    condition: typing.Optional[typing.List[RequestGroupCondition]] = pydantic.Field(
        default=None,
        description="An expression that describes applicability criteria, or start/stop conditions for the action.",
    )
    related_action: typing.Optional[typing.List[RequestGroupRelatedAction]] = pydantic.Field(
        alias="relatedAction",
        default=None,
        description='A relationship to another action such as "before" or "30-60 minutes after start of".',
    )
    timing_date_time: typing.Optional[str] = pydantic.Field(
        alias="timingDateTime",
        default=None,
        description="An optional value describing when the action should be performed.",
    )
    timing_age: typing.Optional[Age] = pydantic.Field(
        alias="timingAge", default=None, description="An optional value describing when the action should be performed."
    )
    timing_period: typing.Optional[Period] = pydantic.Field(
        alias="timingPeriod",
        default=None,
        description="An optional value describing when the action should be performed.",
    )
    timing_duration: typing.Optional[Duration] = pydantic.Field(
        alias="timingDuration",
        default=None,
        description="An optional value describing when the action should be performed.",
    )
    timing_range: typing.Optional[Range] = pydantic.Field(
        alias="timingRange",
        default=None,
        description="An optional value describing when the action should be performed.",
    )
    timing_timing: typing.Optional[Timing] = pydantic.Field(
        alias="timingTiming",
        default=None,
        description="An optional value describing when the action should be performed.",
    )
    participant: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="The participant that should perform or be responsible for this action."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="The type of action to perform (create, update, remove)."
    )
    grouping_behavior: typing.Optional[Code] = pydantic.Field(
        alias="groupingBehavior",
        default=None,
        description="Defines the grouping behavior for the action and its children.",
    )
    selection_behavior: typing.Optional[Code] = pydantic.Field(
        alias="selectionBehavior",
        default=None,
        description="Defines the selection behavior for the action and its children.",
    )
    required_behavior: typing.Optional[Code] = pydantic.Field(
        alias="requiredBehavior", default=None, description="Defines expectations around whether an action is required."
    )
    precheck_behavior: typing.Optional[Code] = pydantic.Field(
        alias="precheckBehavior", default=None, description="Defines whether the action should usually be preselected."
    )
    cardinality_behavior: typing.Optional[Code] = pydantic.Field(
        alias="cardinalityBehavior",
        default=None,
        description="Defines whether the action can be selected multiple times.",
    )
    resource: typing.Optional[Reference] = pydantic.Field(
        default=None, description="The resource that is the target of the action (e.g. CommunicationRequest)."
    )
    action: typing.Optional[typing.List[RequestGroupAction]] = pydantic.Field(default=None, description="Sub actions.")

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


RequestGroupAction.update_forward_refs()
