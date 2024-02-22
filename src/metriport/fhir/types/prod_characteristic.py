# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .codeable_concept import CodeableConcept
from .extension import Extension
from .quantity import Quantity

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProdCharacteristic(pydantic.BaseModel):
    """
    The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
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
    height: typing.Optional[Quantity] = pydantic.Field(
        default=None,
        description="Where applicable, the height can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.",
    )
    width: typing.Optional[Quantity] = pydantic.Field(
        default=None,
        description="Where applicable, the width can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.",
    )
    depth: typing.Optional[Quantity] = pydantic.Field(
        default=None,
        description="Where applicable, the depth can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.",
    )
    weight: typing.Optional[Quantity] = pydantic.Field(
        default=None,
        description="Where applicable, the weight can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.",
    )
    nominal_volume: typing.Optional[Quantity] = pydantic.Field(
        alias="nominalVolume",
        default=None,
        description="Where applicable, the nominal volume can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.",
    )
    external_diameter: typing.Optional[Quantity] = pydantic.Field(
        alias="externalDiameter",
        default=None,
        description="Where applicable, the external diameter can be specified using a numerical value and its unit of measurement The unit of measurement shall be specified in accordance with ISO 11240 and the resulting terminology The symbol and the symbol identifier shall be used.",
    )
    shape: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Where applicable, the shape can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used.",
    )
    color: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None,
        description="Where applicable, the color can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used.",
    )
    imprint: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, description="Where applicable, the imprint can be specified as text."
    )
    image: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        default=None,
        description="Where applicable, the image can be provided The format of the image attachment shall be specified by regional implementations.",
    )
    scoring: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="Where applicable, the scoring can be specified An appropriate controlled vocabulary shall be used The term and the term identifier shall be used.",
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
