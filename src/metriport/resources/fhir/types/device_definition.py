# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .base_resource import BaseResource
from .codeable_concept import CodeableConcept
from .contact_point import ContactPoint
from .device_definition_capability import DeviceDefinitionCapability
from .device_definition_classification import DeviceDefinitionClassification
from .device_definition_device_name import DeviceDefinitionDeviceName
from .device_definition_material import DeviceDefinitionMaterial
from .device_definition_property import DeviceDefinitionProperty
from .device_definition_specialization import DeviceDefinitionSpecialization
from .device_definition_udi_device_identifier import DeviceDefinitionUdiDeviceIdentifier
from .identifier import Identifier
from .prod_characteristic import ProdCharacteristic
from .product_shelf_life import ProductShelfLife
from .quantity import Quantity
from .reference import Reference
from .uri import Uri

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DeviceDefinition(BaseResource):
    """
    The characteristics, operational status and capabilities of a medical-related component of a medical device.
    """

    resource_type: typing_extensions.Literal["DeviceDefinition"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="Unique instance identifiers assigned to a device by the software, manufacturers, other organizations or owners. For example: handle ID."
    )
    udi_device_identifier: typing.Optional[typing.List[DeviceDefinitionUdiDeviceIdentifier]] = pydantic.Field(
        alias="udiDeviceIdentifier",
        description="Unique device identifier (UDI) assigned to device label or package. Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.",
    )
    manufacturer_string: typing.Optional[str] = pydantic.Field(
        alias="manufacturerString", description="A name of the manufacturer."
    )
    manufacturer_reference: typing.Optional[Reference] = pydantic.Field(
        alias="manufacturerReference", description="A name of the manufacturer."
    )
    device_name: typing.Optional[typing.List[DeviceDefinitionDeviceName]] = pydantic.Field(
        alias="deviceName", description="A name given to the device to identify it."
    )
    model_number: typing.Optional[str] = pydantic.Field(
        alias="modelNumber", description="The model number for the device."
    )
    type: typing.Optional[CodeableConcept] = pydantic.Field(description="What kind of device or device system this is.")
    specialization: typing.Optional[typing.List[DeviceDefinitionSpecialization]] = pydantic.Field(
        description="The capabilities supported on a device, the standards to which the device conforms for a particular purpose, and used for the communication."
    )
    version: typing.Optional[typing.List[str]] = pydantic.Field(
        description="The available versions of the device, e.g., software versions."
    )
    safety: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        description="Safety characteristics of the device."
    )
    shelf_life_storage: typing.Optional[typing.List[ProductShelfLife]] = pydantic.Field(
        alias="shelfLifeStorage", description="Shelf Life and storage information."
    )
    physical_characteristics: typing.Optional[ProdCharacteristic] = pydantic.Field(
        alias="physicalCharacteristics", description="Dimensions, color etc."
    )
    language_code: typing.Optional[typing.List[CodeableConcept]] = pydantic.Field(
        alias="languageCode",
        description="Language code for the human-readable text strings produced by the device (all supported).",
    )
    capability: typing.Optional[typing.List[DeviceDefinitionCapability]] = pydantic.Field(
        description="Device capabilities."
    )
    property: typing.Optional[typing.List[DeviceDefinitionProperty]] = pydantic.Field(
        description="The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties."
    )
    owner: typing.Optional[Reference] = pydantic.Field(
        description="An organization that is responsible for the provision and ongoing maintenance of the device."
    )
    contact: typing.Optional[typing.List[ContactPoint]] = pydantic.Field(
        description="Contact details for an organization or a particular human that is responsible for the device."
    )
    url: typing.Optional[Uri] = pydantic.Field(
        description="A network address on which the device may be contacted directly."
    )
    online_information: typing.Optional[Uri] = pydantic.Field(
        alias="onlineInformation", description="Access to on-line information about the device."
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        description="Descriptive information, usage information or implantation information that is not captured in an existing element."
    )
    quantity: typing.Optional[Quantity] = pydantic.Field(
        description="The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)."
    )
    parent_device: typing.Optional[Reference] = pydantic.Field(
        alias="parentDevice", description="The parent device it can be part of."
    )
    material: typing.Optional[typing.List[DeviceDefinitionMaterial]] = pydantic.Field(
        description="A substance used to create the material(s) of which the device is made."
    )
    classification: typing.Optional[typing.List[DeviceDefinitionClassification]] = pydantic.Field(
        description="What kind of device or device system this is."
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
