# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .extension import Extension
from .implementation_guide_grouping import ImplementationGuideGrouping
from .implementation_guide_page import ImplementationGuidePage
from .implementation_guide_parameter import ImplementationGuideParameter
from .implementation_guide_resource import ImplementationGuideResource
from .implementation_guide_template import ImplementationGuideTemplate

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ImplementationGuideDefinition(pydantic.BaseModel):
    """
    A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
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
    grouping: typing.Optional[typing.List[ImplementationGuideGrouping]] = pydantic.Field(
        description="A logical group of resources. Logical groups can be used when building pages."
    )
    resource: typing.List[ImplementationGuideResource] = pydantic.Field(
        description="A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resource."
    )
    page: typing.Optional[ImplementationGuidePage] = pydantic.Field(
        description="A page / section in the implementation guide. The root page is the implementation guide home page."
    )
    parameter: typing.Optional[typing.List[ImplementationGuideParameter]] = pydantic.Field(
        description="Defines how IG is built by tools."
    )
    template: typing.Optional[typing.List[ImplementationGuideTemplate]] = pydantic.Field(
        description="A template for building resources."
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
