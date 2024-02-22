# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .canonical import Canonical
from .code import Code

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ParameterDefinition(pydantic.BaseModel):
    """
    The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    name: typing.Optional[Code] = pydantic.Field(
        default=None,
        description="The name of the parameter used to allow access to the value of the parameter in evaluation contexts.",
    )
    use: typing.Optional[Code] = pydantic.Field(
        default=None, description="Whether the parameter is input or output for the module."
    )
    min: typing.Optional[int] = pydantic.Field(
        default=None, description="The minimum number of times this parameter SHALL appear in the request or response."
    )
    max: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The maximum number of times this element is permitted to appear in the request or response.",
    )
    documentation: typing.Optional[str] = pydantic.Field(
        default=None, description="A brief discussion of what the parameter is for and how it is used by the module."
    )
    type: typing.Optional[Code] = pydantic.Field(default=None, description="The type of the parameter.")
    profile: typing.Optional[Canonical] = pydantic.Field(
        default=None,
        description="If specified, this indicates a profile that the input data must conform to, or that the output data will conform to.",
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
        json_encoders = {dt.datetime: serialize_datetime}


from .extension import Extension  # noqa: E402

ParameterDefinition.update_forward_refs()
