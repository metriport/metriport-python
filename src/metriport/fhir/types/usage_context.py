# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UsageContext(pydantic.BaseModel):
    """
    Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    code: Coding = pydantic.Field(
        description="A code that identifies the type of context being specified by this usage context."
    )
    value_codeable_concept: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="valueCodeableConcept",
        description="A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.",
    )
    value_quantity: typing.Optional[Quantity] = pydantic.Field(
        alias="valueQuantity",
        description="A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.",
    )
    value_range: typing.Optional[Range] = pydantic.Field(
        alias="valueRange",
        description="A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.",
    )
    value_reference: typing.Optional[Reference] = pydantic.Field(
        alias="valueReference",
        description="A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.",
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


from .codeable_concept import CodeableConcept  # noqa: E402
from .coding import Coding  # noqa: E402
from .extension import Extension  # noqa: E402
from .quantity import Quantity  # noqa: E402
from .range import Range  # noqa: E402
from .reference import Reference  # noqa: E402

UsageContext.update_forward_refs()
