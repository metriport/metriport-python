# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .example_scenario_contained_instance import ExampleScenarioContainedInstance
from .extension import Extension
from .markdown import Markdown

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ExampleScenarioOperation(pydantic.BaseModel):
    """
    Example of workflow instance.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    number: typing.Optional[str] = pydantic.Field(description="The sequential number of the interaction, e.g. 1.2.5.")
    type: typing.Optional[str] = pydantic.Field(description="The type of operation - CRUD.")
    name: typing.Optional[str] = pydantic.Field(description="The human-friendly name of the interaction.")
    initiator: typing.Optional[str] = pydantic.Field(description="Who starts the transaction.")
    receiver: typing.Optional[str] = pydantic.Field(description="Who receives the transaction.")
    description: typing.Optional[Markdown] = pydantic.Field(description="A comment to be inserted in the diagram.")
    initiator_active: typing.Optional[bool] = pydantic.Field(
        alias="initiatorActive", description="Whether the initiator is deactivated right after the transaction."
    )
    receiver_active: typing.Optional[bool] = pydantic.Field(
        alias="receiverActive", description="Whether the receiver is deactivated right after the transaction."
    )
    request: typing.Optional[ExampleScenarioContainedInstance] = pydantic.Field(
        description="Each resource instance used by the initiator."
    )
    response: typing.Optional[ExampleScenarioContainedInstance] = pydantic.Field(
        description="Each resource instance used by the responder."
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