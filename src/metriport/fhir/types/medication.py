# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .identifier import Identifier
from .medication_batch import MedicationBatch
from .medication_ingredient import MedicationIngredient
from .ratio import Ratio
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Medication(BaseResource):
    """
    This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    """

    resource_type: typing_extensions.Literal["Medication"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Business identifier for this medication."
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A code (or set of codes) that specify this medication, or a textual description if no code is available. Usage note: This could be a standard medication code such as a code from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local formulary code, optionally with translations to other code systems."
    )
    status: typing.Optional[Code] = pydantic.Field(description="A code to indicate if the medication is in active use.")
    manufacturer: typing.Optional[Reference] = pydantic.Field(
        description="Describes the details of the manufacturer of the medication product. This is not intended to represent the distributor of a medication product."
    )
    form: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Describes the form of the item. Powder; tablets; capsule."
    )
    amount: typing.Optional[Ratio] = pydantic.Field(
        description="Specific amount of the drug in the packaged product. For example, when specifying a product that has the same strength (For example, Insulin glargine 100 unit per mL solution for injection), this attribute provides additional clarification of the package amount (For example, 3 mL, 10mL, etc.)."
    )
    ingredient: typing.Optional[typing.List[MedicationIngredient]] = pydantic.Field(
        description="Identifies a particular constituent of interest in the product."
    )
    batch: typing.Optional[MedicationBatch] = pydantic.Field(
        description="Information that only applies to packages (not products)."
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