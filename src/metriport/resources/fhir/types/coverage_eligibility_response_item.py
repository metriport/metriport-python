# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .coverage_eligibility_response_benefit import CoverageEligibilityResponseBenefit
from .extension import Extension
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CoverageEligibilityResponseItem(pydantic.BaseModel):
    """
    This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
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
    category: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Code to identify the general type of benefits under which products and services are provided."
    )
    product_or_service: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="productOrService",
        description="This contains the product, service, drug or other billing code for the item.",
    )
    modifier: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Item typification or modifiers codes to convey additional context for the product or service."
    )
    provider: typing.Optional[Reference] = pydantic.Field(
        description="The practitioner who is eligible for the provision of the product or service."
    )
    excluded: typing.Optional[bool] = pydantic.Field(
        description="True if the indicated class of service is excluded from the plan, missing or False indicates the product or service is included in the coverage."
    )
    name: typing.Optional[str] = pydantic.Field(description="A short name or tag for the benefit.")
    description: typing.Optional[str] = pydantic.Field(
        description="A richer description of the benefit or services covered."
    )
    network: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Is a flag to indicate whether the benefits refer to in-network providers or out-of-network providers."
    )
    unit: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Indicates if the benefits apply to an individual or to the family."
    )
    term: typing.Optional[CodeableConcept] = pydantic.Field(
        description="The term or period of the values such as 'maximum lifetime benefit' or 'maximum annual visits'."
    )
    benefit: typing.Optional[typing.List[CoverageEligibilityResponseBenefit]] = pydantic.Field(
        description="Benefits used to date."
    )
    authorization_required: typing.Optional[bool] = pydantic.Field(
        alias="authorizationRequired",
        description="A boolean flag indicating whether a preauthorization is required prior to actual service delivery.",
    )
    authorization_supporting: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="authorizationSupporting",
        description="Codes or comments regarding information or actions associated with the preauthorization.",
    )
    authorization_url: typing.Optional[Uri] = pydantic.Field(
        alias="authorizationUrl",
        description="A web location for obtaining requirements or descriptive information regarding the preauthorization.",
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
