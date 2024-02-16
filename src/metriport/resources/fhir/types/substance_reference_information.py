# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .substance_reference_information_classification import SubstanceReferenceInformationClassification
from .substance_reference_information_gene import SubstanceReferenceInformationGene
from .substance_reference_information_gene_element import SubstanceReferenceInformationGeneElement
from .substance_reference_information_target import SubstanceReferenceInformationTarget

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SubstanceReferenceInformation(BaseResource):
    """
    Todo.
    """

    resource_type: typing_extensions.Literal["SubstanceReferenceInformation"] = pydantic.Field(alias="resourceType")
    comment: typing.Optional[str] = pydantic.Field(description="Todo.")
    gene: typing.Optional[typing.List[SubstanceReferenceInformationGene]] = pydantic.Field(description="Todo.")
    gene_element: typing.Optional[typing.List[SubstanceReferenceInformationGeneElement]] = pydantic.Field(
        alias="geneElement", description="Todo."
    )
    classification: typing.Optional[typing.List[SubstanceReferenceInformationClassification]] = pydantic.Field(
        description="Todo."
    )
    target: typing.Optional[typing.List[SubstanceReferenceInformationTarget]] = pydantic.Field(description="Todo.")

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
