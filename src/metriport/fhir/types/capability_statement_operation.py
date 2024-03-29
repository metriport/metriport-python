# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .canonical import Canonical
from .extension import Extension
from .markdown import Markdown

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CapabilityStatementOperation(pydantic.BaseModel):
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
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
    name: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The name of the operation or query. For an operation, this is the name prefixed with $ and used in the URL. For a query, this is the name used in the \_query parameter when the query is called.",
    )
    definition: Canonical = pydantic.Field(
        description="Where the formal definition can be found. If a server references the base definition of an Operation (i.e. from the specification itself such as `http://hl7.org/fhir/OperationDefinition/ValueSet-expand`), that means it supports the full capabilities of the operation - e.g. both GET and POST invocation. If it only supports a subset, it must define its own custom [[[OperationDefinition]]] with a 'base' of the original OperationDefinition. The custom definition would describe the specific subset of functionality supported."
    )
    documentation: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="Documentation that describes anything special about the operation behavior, possibly detailing different behavior for system, type and instance-level invocation of the operation.",
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
