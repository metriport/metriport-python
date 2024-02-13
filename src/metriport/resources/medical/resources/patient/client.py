# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .types.base_patient import BasePatient
from .types.list_patients_response import ListPatientsResponse
from .types.medical_record_status import MedicalRecordStatus
from .types.patient import Patient

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PatientClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, facility_id: str, request: BasePatient) -> Patient:
        """
        Creates a Patient in Metriport for the specified Facility where the patient is receiving care.
        The more demographic info you can provide about a Patient,
        the higher chances Metriport will be able to find a match.
        For example, nicknames, old addresses, multiple phone numbers,
        a pre-marital last name, etc.

        Parameters:
            - facility_id: str. The ID of the Facility where the Patient is receiving care.

            - request: BasePatient.
        ---
        from metriport import Address, UsState
        from metriport.client import Metriport
        from metriport.resources.medical import (
            BasePatient,
            PersonalIdentifier_DriversLicense,
        )

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.patient.create(
            facility_id="2.16.840.1.113883.3.666.5.2004.4.2005",
            request=BasePatient(
                first_name="Karen",
                last_name="Lynch",
                dob="1963-12-30",
                gender_at_birth="F",
                personal_identifiers=[
                    PersonalIdentifier_DriversLicense(
                        type="driversLicense",
                        state=UsState.CA,
                        value="51227265",
                    )
                ],
                address=[
                    Address(
                        address_line_1="2261 Market Street",
                        address_line_2="#4818",
                        city="San Francisco",
                        state=UsState.CA,
                        zip="94114",
                        country="USA",
                    )
                ],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/patient"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Patient, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str) -> Patient:
        """
        Get a Patient

        Parameters:
            - id: str. The ID of the Patient.
        ---
        from metriport.client import Metriport

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.patient.get(
            id="2.16.840.1.113883.3.666.777",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Patient, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, id: str, *, facility_id: str, request: BasePatient) -> Patient:
        """
        Updates the specified Patient.

        Parameters:
            - id: str. The ID of the Patient to update.

            - facility_id: str. The ID of the Facility where the patient is receiving care.

            - request: BasePatient.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{id}"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Patient, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, facility_id: typing.Optional[str] = None) -> ListPatientsResponse:
        """
        Lists all Patients receiving care at the specified Facility, or all Patients if no Facility is specified.

        Parameters:
            - facility_id: typing.Optional[str]. The ID of the Facility where the patient is receiving care.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/patient"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListPatientsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, facility_id: typing.Optional[str] = None) -> None:
        """
        Removes the specified Patient.

        Parameters:
            - id: str. The ID of the Patient to delete.

            - facility_id: typing.Optional[str]. The ID of the Facility where the patient is receiving care.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{id}"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_medical_record_summary(self, patient_id: str, *, conversion_type: str) -> str:
        """
        Returns the URL for a medical record summary

        Parameters:
            - patient_id: str. The ID of the Patient.

            - conversion_type: str. The type of conversion to perform. `html` or `pdf`
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{patient_id}/medical-record"
            ),
            params=remove_none_from_dict({"conversionType": conversion_type}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_medical_record_summary_status(self, patient_id: str) -> MedicalRecordStatus:
        """
        Returns the status of a medical record summary

        Parameters:
            - patient_id: str. The ID of the Patient.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{patient_id}/medical-record-status"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MedicalRecordStatus, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPatientClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, facility_id: str, request: BasePatient) -> Patient:
        """
        Creates a Patient in Metriport for the specified Facility where the patient is receiving care.
        The more demographic info you can provide about a Patient,
        the higher chances Metriport will be able to find a match.
        For example, nicknames, old addresses, multiple phone numbers,
        a pre-marital last name, etc.

        Parameters:
            - facility_id: str. The ID of the Facility where the Patient is receiving care.

            - request: BasePatient.
        ---
        from metriport import Address, UsState
        from metriport.client import AsyncMetriport
        from metriport.resources.medical import (
            BasePatient,
            PersonalIdentifier_DriversLicense,
        )

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.patient.create(
            facility_id="2.16.840.1.113883.3.666.5.2004.4.2005",
            request=BasePatient(
                first_name="Karen",
                last_name="Lynch",
                dob="1963-12-30",
                gender_at_birth="F",
                personal_identifiers=[
                    PersonalIdentifier_DriversLicense(
                        type="driversLicense",
                        state=UsState.CA,
                        value="51227265",
                    )
                ],
                address=[
                    Address(
                        address_line_1="2261 Market Street",
                        address_line_2="#4818",
                        city="San Francisco",
                        state=UsState.CA,
                        zip="94114",
                        country="USA",
                    )
                ],
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/patient"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Patient, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str) -> Patient:
        """
        Get a Patient

        Parameters:
            - id: str. The ID of the Patient.
        ---
        from metriport.client import AsyncMetriport

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.patient.get(
            id="2.16.840.1.113883.3.666.777",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Patient, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, id: str, *, facility_id: str, request: BasePatient) -> Patient:
        """
        Updates the specified Patient.

        Parameters:
            - id: str. The ID of the Patient to update.

            - facility_id: str. The ID of the Facility where the patient is receiving care.

            - request: BasePatient.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{id}"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Patient, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, facility_id: typing.Optional[str] = None) -> ListPatientsResponse:
        """
        Lists all Patients receiving care at the specified Facility, or all Patients if no Facility is specified.

        Parameters:
            - facility_id: typing.Optional[str]. The ID of the Facility where the patient is receiving care.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/patient"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListPatientsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, facility_id: typing.Optional[str] = None) -> None:
        """
        Removes the specified Patient.

        Parameters:
            - id: str. The ID of the Patient to delete.

            - facility_id: typing.Optional[str]. The ID of the Facility where the patient is receiving care.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{id}"),
            params=remove_none_from_dict({"facilityId": facility_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_medical_record_summary(self, patient_id: str, *, conversion_type: str) -> str:
        """
        Returns the URL for a medical record summary

        Parameters:
            - patient_id: str. The ID of the Patient.

            - conversion_type: str. The type of conversion to perform. `html` or `pdf`
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{patient_id}/medical-record"
            ),
            params=remove_none_from_dict({"conversionType": conversion_type}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_medical_record_summary_status(self, patient_id: str) -> MedicalRecordStatus:
        """
        Returns the status of a medical record summary

        Parameters:
            - patient_id: str. The ID of the Patient.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"medical/v1/patient/{patient_id}/medical-record-status"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MedicalRecordStatus, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
