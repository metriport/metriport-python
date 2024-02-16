# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .duration import Duration
from .extension import Extension
from .medication_request_initial_fill import MedicationRequestInitialFill
from .period import Period
from .quantity import Quantity
from .reference import Reference
from .unsigned_int import UnsignedInt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MedicationRequestDispenseRequest(pydantic.BaseModel):
    """
    An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
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
    initial_fill: typing.Optional[MedicationRequestInitialFill] = pydantic.Field(
        alias="initialFill", description="Indicates the quantity or duration for the first dispense of the medication."
    )
    dispense_interval: typing.Optional[Duration] = pydantic.Field(
        alias="dispenseInterval",
        description="The minimum period of time that must occur between dispenses of the medication.",
    )
    validity_period: typing.Optional[Period] = pydantic.Field(
        alias="validityPeriod",
        description="This indicates the validity period of a prescription (stale dating the Prescription).",
    )
    number_of_repeats_allowed: typing.Optional[UnsignedInt] = pydantic.Field(
        alias="numberOfRepeatsAllowed",
        description='An integer indicating the number of times, in addition to the original dispense, (aka refills or repeats) that the patient can receive the prescribed medication. Usage Notes: This integer does not include the original order dispense. This means that if an order indicates dispense 30 tablets plus "3 repeats", then the order can be dispensed a total of 4 times and the patient can receive a total of 120 tablets. A prescriber may explicitly say that zero refills are permitted after the initial dispense.',
    )
    quantity: typing.Optional[Quantity] = pydantic.Field(description="The amount that is to be dispensed for one fill.")
    expected_supply_duration: typing.Optional[Duration] = pydantic.Field(
        alias="expectedSupplyDuration",
        description="Identifies the period time over which the supplied product is expected to be used, or the length of time the dispense is expected to last.",
    )
    performer: typing.Optional[Reference] = pydantic.Field(
        description="Indicates the intended dispensing Organization specified by the prescriber."
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
