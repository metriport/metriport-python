# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .identifier import Identifier
from .insurance_plan_general_cost import InsurancePlanGeneralCost
from .insurance_plan_specific_cost import InsurancePlanSpecificCost
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InsurancePlanPlan(pydantic.BaseModel):
    """
    Details of a Health Insurance product/plan provided by an organization.
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
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Business identifiers assigned to this health insurance plan which remain constant as the resource is updated and propagates from server to server."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        description='Type of plan. For example, "Platinum" or "High Deductable".'
    )
    coverage_area: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="coverageArea", description="The geographic region in which a health insurance plan's benefits apply."
    )
    network: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Reference to the network that providing the type of coverage."
    )
    general_cost: typing.Optional[typing.List[InsurancePlanGeneralCost]] = pydantic.Field(
        alias="generalCost", description="Overall costs associated with the plan."
    )
    specific_cost: typing.Optional[typing.List[InsurancePlanSpecificCost]] = pydantic.Field(
        alias="specificCost", description="Costs associated with the coverage provided by the product."
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
