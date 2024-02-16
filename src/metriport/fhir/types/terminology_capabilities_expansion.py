# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .extension import Extension
from .markdown import Markdown
from .terminology_capabilities_parameter import TerminologyCapabilitiesParameter

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TerminologyCapabilitiesExpansion(pydantic.BaseModel):
    """
    A TerminologyCapabilities resource documents a set of capabilities (behaviors) of a FHIR Terminology Server that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
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
    hierarchical: typing.Optional[bool] = pydantic.Field(description="Whether the server can return nested value sets.")
    paging: typing.Optional[bool] = pydantic.Field(description="Whether the server supports paging on expansion.")
    incomplete: typing.Optional[bool] = pydantic.Field(description="Allow request for incomplete expansions?")
    parameter: typing.Optional[typing.List[TerminologyCapabilitiesParameter]] = pydantic.Field(
        description="Supported expansion parameter."
    )
    text_filter: typing.Optional[Markdown] = pydantic.Field(
        alias="textFilter", description="Documentation about text searching works."
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