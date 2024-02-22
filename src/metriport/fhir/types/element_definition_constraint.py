# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .canonical import Canonical
from .element_definition_constraint_severity import ElementDefinitionConstraintSeverity
from .extension import Extension
from .id import Id

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ElementDefinitionConstraint(pydantic.BaseModel):
    """
    Captures constraints on each element within the resource, profile, or extension.
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
    key: typing.Optional[Id] = pydantic.Field(
        default=None,
        description="Allows identification of which elements have their cardinalities impacted by the constraint. Will not be referenced for constraints that do not affect cardinality.",
    )
    requirements: typing.Optional[str] = pydantic.Field(
        default=None, description="Description of why this constraint is necessary or appropriate."
    )
    severity: typing.Optional[ElementDefinitionConstraintSeverity] = pydantic.Field(
        default=None, description="Identifies the impact constraint violation has on the conformance of the instance."
    )
    human: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Text that can be used to describe the constraint in messages identifying that the constraint has been violated.",
    )
    expression: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A [FHIRPath](fhirpath.html) expression of constraint that can be executed to see if this constraint is met.",
    )
    xpath: typing.Optional[str] = pydantic.Field(
        default=None,
        description="An XPath expression of constraint that can be executed to see if this constraint is met.",
    )
    source: typing.Optional[Canonical] = pydantic.Field(
        default=None, description="A reference to the original source of the constraint, for traceability purposes."
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
