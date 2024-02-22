# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .quantity import Quantity
from .range import Range

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DeviceRequestParameter(pydantic.BaseModel):
    """
    Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.
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
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="A code or string that identifies the device detail being asserted."
    )
    value_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="valueCodeableConcept", default=None, description="The value of the device detail."
    )
    value_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="valueQuantity", default=None, description="The value of the device detail."
    )
    value_range: typing.Optional[Range] = pydantic.Field(
        alias="valueRange", default=None, description="The value of the device detail."
    )
    value_boolean: typing.Optional[bool] = pydantic.Field(
        alias="valueBoolean", default=None, description="The value of the device detail."
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
