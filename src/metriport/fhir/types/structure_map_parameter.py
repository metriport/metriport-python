# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .extension import Extension

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class StructureMapParameter(pydantic.BaseModel):
    """
    A Map of relationships between 2 structures that can be used to transform data.
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
    value_id: typing.Optional[str] = pydantic.Field(
        alias="valueId", default=None, description="Parameter value - variable or literal."
    )
    value_string: typing.Optional[str] = pydantic.Field(
        alias="valueString", default=None, description="Parameter value - variable or literal."
    )
    value_boolean: typing.Optional[bool] = pydantic.Field(
        alias="valueBoolean", default=None, description="Parameter value - variable or literal."
    )
    value_integer: typing.Optional[float] = pydantic.Field(
        alias="valueInteger", default=None, description="Parameter value - variable or literal."
    )
    value_decimal: typing.Optional[float] = pydantic.Field(
        alias="valueDecimal", default=None, description="Parameter value - variable or literal."
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
