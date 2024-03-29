# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .canonical import Canonical
from .charge_item_definition_applicability import ChargeItemDefinitionApplicability
from .charge_item_definition_property_group import ChargeItemDefinitionPropertyGroup
from .charge_item_definition_status import ChargeItemDefinitionStatus
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .identifier import Identifier
from .markdown import Markdown
from .period import Period
from .reference import Reference
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ChargeItemDefinition(BaseResource):
    """
    The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
    """

    resource_type: typing.Literal["ChargeItemDefinition"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        default=None,
        description="An absolute URI that is used to identify this charge item definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this charge item definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the charge item definition is stored on different servers.",
    )
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="A formal identifier that is used to identify this charge item definition when it is represented in other formats, or referenced in a specification, model, design or an instance.",
    )
    version: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The identifier that is used to identify this version of the charge item definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the charge item definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. To provide a version consistent with the Decision Support Service specification, use the format Major.Minor.Revision (e.g. 1.0.0). For more information on versioning knowledge assets, refer to the Decision Support Service specification. Note that a version is required for non-experimental active assets.",
    )
    title: typing.Optional[str] = pydantic.Field(
        default=None, description="A short, descriptive, user-friendly title for the charge item definition."
    )
    derived_from_uri: typing.Optional[typing.List[Uri]] = pydantic.Field(
        alias="derivedFromUri",
        default=None,
        description="The URL pointing to an externally-defined charge item definition that is adhered to in whole or in part by this definition.",
    )
    part_of: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        alias="partOf",
        default=None,
        description="A larger definition of which this particular definition is a component or step.",
    )
    replaces: typing.Optional[typing.List[Canonical]] = pydantic.Field(
        default=None,
        description="As new versions of a protocol or guideline are defined, allows identification of what versions are replaced by a new instance.",
    )
    status: typing.Optional[ChargeItemDefinitionStatus] = pydantic.Field(
        default=None, description="The current state of the ChargeItemDefinition."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="A Boolean value to indicate that this charge item definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.",
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        default=None,
        description="The date (and optionally time) when the charge item definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the charge item definition changes.",
    )
    publisher: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The name of the organization or individual that published the charge item definition.",
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        default=None, description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="A free text natural language description of the charge item definition from a consumer's perspective.",
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        default=None,
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate charge item definition instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="A legal or geographic region in which the charge item definition is intended to be used.",
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        default=None,
        description="A copyright statement relating to the charge item definition and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the charge item definition.",
    )
    approval_date: typing.Optional[dt.date] = pydantic.Field(
        alias="approvalDate",
        default=None,
        description="The date on which the resource content was approved by the publisher. Approval happens once when the content is officially approved for usage.",
    )
    last_review_date: typing.Optional[dt.date] = pydantic.Field(
        alias="lastReviewDate",
        default=None,
        description="The date on which the resource content was last reviewed. Review happens periodically after approval but does not change the original approval date.",
    )
    effective_period: typing.Optional[Period] = pydantic.Field(
        alias="effectivePeriod",
        default=None,
        description="The period during which the charge item definition content was or is planned to be in active use.",
    )
    code: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None, description="The defined billing details in this resource pertain to the given billing code."
    )
    instance: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None,
        description="The defined billing details in this resource pertain to the given product instance(s).",
    )
    applicability: typing.Optional[typing.List[ChargeItemDefinitionApplicability]] = pydantic.Field(
        default=None, description="Expressions that describe applicability criteria for the billing code."
    )
    property_group: typing.Optional[typing.List[ChargeItemDefinitionPropertyGroup]] = pydantic.Field(
        alias="propertyGroup",
        default=None,
        description="Group of properties which are applicable under the same conditions. If no applicability rules are established for the group, then all properties always apply.",
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
