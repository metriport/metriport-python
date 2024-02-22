# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .attachment import Attachment
from .base_resource import BaseResource
from .code import Code
from .codeable_concept import CodeableConcept
from .decimal import Decimal
from .identifier import Identifier
from .instant import Instant
from .period import Period
from .positive_int import PositiveInt
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Media(BaseResource):
    """
    A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
    """

    resource_type: typing.Literal["Media"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Identifiers associated with the image - these may include identifiers for the image itself, identifiers for the context of its collection (e.g. series ids) and context ids such as accession numbers or other workflow identifiers."
    )
    based_on: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="basedOn", description="A procedure that is fulfilled in whole or in part by the creation of this media."
    )
    part_of: typing.Optional[typing.List[Reference]] = pydantic.Field(
        alias="partOf", description="A larger event of which this particular event is a component or step."
    )
    status: typing.Optional[Code] = pydantic.Field(description="The current state of the {{title}}.")
    type: typing.Optional[CodeableConcept] = pydantic.Field(
        description="A code that classifies whether the media is an image, video or audio recording or some other media category."
    )
    modality: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Details of the type of the media - usually, how it was acquired (what type of device). If images sourced from a DICOM system, are wrapped in a Media resource, then this is the modality."
    )
    view: typing.Optional[CodeableConcept] = pydantic.Field(
        description="The name of the imaging view e.g. Lateral or Antero-posterior (AP)."
    )
    subject: typing.Optional[Reference] = pydantic.Field(description="Who/What this Media is a record of.")
    encounter: typing.Optional[Reference] = pydantic.Field(
        description="The encounter that establishes the context for this media."
    )
    created_date_time: typing.Optional[str] = pydantic.Field(
        alias="createdDateTime", description="The date and time(s) at which the media was collected."
    )
    created_period: typing.Optional[Period] = pydantic.Field(
        alias="createdPeriod", description="The date and time(s) at which the media was collected."
    )
    issued: typing.Optional[Instant] = pydantic.Field(
        description="The date and time this version of the media was made available to providers, typically after having been reviewed."
    )
    operator: typing.Optional[Reference] = pydantic.Field(
        description="The person who administered the collection of the image."
    )
    reason_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="reasonCode", description="Describes why the event occurred in coded or textual form."
    )
    body_site: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="bodySite",
        description="Indicates the site on the subject's body where the observation was made (i.e. the target site).",
    )
    device_name: typing.Optional[str] = pydantic.Field(
        alias="deviceName",
        description="The name of the device / manufacturer of the device that was used to make the recording.",
    )
    device: typing.Optional[Reference] = pydantic.Field(description="The device used to collect the media.")
    height: typing.Optional[PositiveInt] = pydantic.Field(description="Height of the image in pixels (photo/video).")
    width: typing.Optional[PositiveInt] = pydantic.Field(description="Width of the image in pixels (photo/video).")
    frames: typing.Optional[PositiveInt] = pydantic.Field(
        description="The number of frames in a photo. This is used with a multi-page fax, or an imaging acquisition context that takes multiple slices in a single image, or an animated gif. If there is more than one frame, this SHALL have a value in order to alert interface software that a multi-frame capable rendering widget is required."
    )
    duration: typing.Optional[Decimal] = pydantic.Field(
        description="The duration of the recording in seconds - for audio and video."
    )
    content: Attachment = pydantic.Field(
        description="The actual content of the media - inline or by direct reference to the media source file."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Comments made about the media by the performer, subject or other participants."
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
