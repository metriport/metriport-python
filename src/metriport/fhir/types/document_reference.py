# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .document_reference_content import DocumentReferenceContent
from .document_reference_context import DocumentReferenceContext
from .document_reference_relates_to import DocumentReferenceRelatesTo
from .document_reference_status import DocumentReferenceStatus
from .identifier import Identifier
from .instant import Instant
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DocumentReference(BaseResource):
    """
    A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.
    """

    resource_type: typing.Literal["DocumentReference"] = pydantic.Field(alias="resourceType")
    master_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="masterIdentifier",
        default=None,
        description="Document identifier as assigned by the source of the document. This identifier is specific to this version of the document. This unique identifier may be used elsewhere to identify this version of the document.",
    )
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        default=None,
        description="Other identifiers associated with the document, including version independent identifiers.",
    )
    status: typing.Optional[DocumentReferenceStatus] = pydantic.Field(
        default=None, description="The status of this document reference."
    )
    doc_status: typing.Optional[Code] = pydantic.Field(
        alias="docStatus", default=None, description="The status of the underlying document."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="Specifies the particular kind of document referenced (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the document referenced.",
    )
    category: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        default=None,
        description="A categorization for the type of document referenced - helps for indexing and searching. This may be implied by or derived from the code specified in the DocumentReference.type.",
    )
    subject: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="Who or what the document is about. The document can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of farm animals, or a set of patients that share a common exposure).",
    )
    date: typing.Optional[Instant] = pydantic.Field(
        default=None, description="When the document reference was created."
    )
    author: typing.Optional[typing.List[Reference]] = pydantic.Field(
        default=None, description="Identifies who is responsible for adding the information to the document."
    )
    authenticator: typing.Optional[Reference] = pydantic.Field(
        default=None, description="Which person or organization authenticates that this document is valid."
    )
    custodian: typing.Optional[Reference] = pydantic.Field(
        default=None,
        description="Identifies the organization or group who is responsible for ongoing maintenance of and access to the document.",
    )
    relates_to: typing.Optional[typing.List[DocumentReferenceRelatesTo]] = pydantic.Field(
        alias="relatesTo",
        default=None,
        description="Relationships that this document has with other document references that already exist.",
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None, description="Human-readable description of the source document."
    )
    security_label: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="securityLabel",
        default=None,
        description='A set of Security-Tag codes specifying the level of privacy/security of the Document. Note that DocumentReference.meta.security contains the security labels of the "reference" to the document, while DocumentReference.securityLabel contains a snapshot of the security labels on the document the reference refers to.',
    )
    content: typing.List[DocumentReferenceContent] = pydantic.Field(
        description="The document and format referenced. There may be multiple content element repetitions, each with a different format."
    )
    context: typing.Optional[DocumentReferenceContext] = pydantic.Field(
        default=None, description="The clinical context in which the document was prepared."
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
