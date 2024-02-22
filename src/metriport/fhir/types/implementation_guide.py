# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_detail import ContactDetail
from .date_time import DateTime
from .id import Id
from .implementation_guide_definition import ImplementationGuideDefinition
from .implementation_guide_depends_on import ImplementationGuideDependsOn
from .implementation_guide_fhir_version_item import ImplementationGuideFhirVersionItem
from .implementation_guide_global import ImplementationGuideGlobal
from .implementation_guide_license import ImplementationGuideLicense
from .implementation_guide_manifest import ImplementationGuideManifest
from .implementation_guide_status import ImplementationGuideStatus
from .markdown import Markdown
from .uri import Uri
from .usage_context import UsageContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ImplementationGuide(BaseResource):
    """
    A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
    """

    resource_type: typing.Literal["ImplementationGuide"] = pydantic.Field(alias="resourceType")
    url: typing.Optional[Uri] = pydantic.Field(
        description="An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers."
    )
    version: typing.Optional[str] = pydantic.Field(
        description="The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence."
    )
    name: typing.Optional[str] = pydantic.Field(
        description="A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation."
    )
    title: typing.Optional[str] = pydantic.Field(
        description="A short, descriptive, user-friendly title for the implementation guide."
    )
    status: typing.Optional[ImplementationGuideStatus] = pydantic.Field(
        description="The status of this implementation guide. Enables tracking the life-cycle of the content."
    )
    experimental: typing.Optional[bool] = pydantic.Field(
        description="A Boolean value to indicate that this implementation guide is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage."
    )
    date: typing.Optional[DateTime] = pydantic.Field(
        description="The date (and optionally time) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes."
    )
    publisher: typing.Optional[str] = pydantic.Field(
        description="The name of the organization or individual that published the implementation guide."
    )
    contact: typing.Optional[typing.List[ContactDetail]] = pydantic.Field(
        description="Contact details to assist a user in finding and communicating with the publisher."
    )
    description: typing.Optional[Markdown] = pydantic.Field(
        description="A free text natural language description of the implementation guide from a consumer's perspective."
    )
    use_context: typing.Optional[typing.List[UsageContext]] = pydantic.Field(
        alias="useContext",
        description="The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate implementation guide instances.",
    )
    jurisdiction: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A legal or geographic region in which the implementation guide is intended to be used."
    )
    copyright: typing.Optional[Markdown] = pydantic.Field(
        description="A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide."
    )
    package_id: typing.Optional[Id] = pydantic.Field(
        alias="packageId",
        description="The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.",
    )
    license: typing.Optional[ImplementationGuideLicense] = pydantic.Field(
        description="The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'."
    )
    fhir_version: typing.Optional[typing.List[ImplementationGuideFhirVersionItem]] = pydantic.Field(
        alias="fhirVersion",
        description="The version(s) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.",
    )
    depends_on: typing.Optional[typing.List[ImplementationGuideDependsOn]] = pydantic.Field(
        alias="dependsOn",
        description="Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.",
    )
    global_: typing.Optional[typing.List[ImplementationGuideGlobal]] = pydantic.Field(
        alias="global",
        description="A set of profiles that all resources covered by this implementation guide must conform to.",
    )
    definition: typing.Optional[ImplementationGuideDefinition] = pydantic.Field(
        description="The information needed by an IG publisher tool to publish the whole implementation guide."
    )
    manifest: typing.Optional[ImplementationGuideManifest] = pydantic.Field(
        description="Information about an assembled implementation guide, created by the publication tooling."
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
