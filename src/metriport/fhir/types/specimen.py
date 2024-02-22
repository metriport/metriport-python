# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .identifier import Identifier
from .reference import Reference
from .specimen_collection import SpecimenCollection
from .specimen_container import SpecimenContainer
from .specimen_processing import SpecimenProcessing
from .specimen_status import SpecimenStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Specimen(BaseResource):
    """
    A sample to be used for analysis.
    """

    resource_type: typing.Literal["Specimen"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(description="Id for specimen.")
    accession_identifier: typing.Optional[Identifier] = pydantic.Field(
        alias="accessionIdentifier",
        description="The identifier assigned by the lab when accessioning specimen(s). This is not necessarily the same as the specimen identifier, depending on local lab procedures.",
    )
    status: typing.Optional[SpecimenStatus] = pydantic.Field(description="The availability of the specimen.")
    type: typing.Optional[CodeableConcept] = pydantic.Field(description="The kind of material that forms the specimen.")
    subject: typing.Optional[Reference] = pydantic.Field(
        description="Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance or a device."
    )
    received_time: typing.Optional[DateTime] = pydantic.Field(
        alias="receivedTime", description="Time when specimen was received for processing or testing."
    )
    parent: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Reference to the parent (source) specimen which is used when the specimen was either derived from or a component of another specimen."
    )
    request: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Details concerning a service request that required a specimen to be collected."
    )
    collection: typing.Optional[SpecimenCollection] = pydantic.Field(
        description="Details concerning the specimen collection."
    )
    processing: typing.Optional[typing.List[SpecimenProcessing]] = pydantic.Field(
        description="Details concerning processing and processing steps for the specimen."
    )
    container: typing.Optional[typing.List[SpecimenContainer]] = pydantic.Field(
        description="The container holding the specimen. The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here."
    )
    condition: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="A mode or state of being that describes the nature of the specimen."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="To communicate any details or issues about the specimen or during the specimen collection. (for example: broken vial, sent with patient, frozen)."
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
