# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceDefinitionDeviceNameType(str, enum.Enum):
    """
    The type of deviceName. UDILabelName | UserFriendlyName | PatientReportedName | ManufactureDeviceName | ModelName.
    """

    UDI_LABEL_NAME = "udi-label-name"
    USER_FRIENDLY_NAME = "user-friendly-name"
    PATIENT_REPORTED_NAME = "patient-reported-name"
    MANUFACTURER_NAME = "manufacturer-name"
    MODEL_NAME = "model-name"
    OTHER = "other"

    def visit(
        self,
        udi_label_name: typing.Callable[[], T_Result],
        user_friendly_name: typing.Callable[[], T_Result],
        patient_reported_name: typing.Callable[[], T_Result],
        manufacturer_name: typing.Callable[[], T_Result],
        model_name: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeviceDefinitionDeviceNameType.UDI_LABEL_NAME:
            return udi_label_name()
        if self is DeviceDefinitionDeviceNameType.USER_FRIENDLY_NAME:
            return user_friendly_name()
        if self is DeviceDefinitionDeviceNameType.PATIENT_REPORTED_NAME:
            return patient_reported_name()
        if self is DeviceDefinitionDeviceNameType.MANUFACTURER_NAME:
            return manufacturer_name()
        if self is DeviceDefinitionDeviceNameType.MODEL_NAME:
            return model_name()
        if self is DeviceDefinitionDeviceNameType.OTHER:
            return other()
