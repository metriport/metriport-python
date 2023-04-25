# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import MercoaEnvironment
from .types.download_document_response import DownloadDocumentResponse
from .types.get_documents_response import GetDocumentsResponse
from .types.trigger_documents_query_response import TriggerDocumentsQueryResponse


class DocumentClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def get(
        self, *, patient_id: str, facility_id: str, force_query: typing.Optional[str] = None
    ) -> GetDocumentsResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "medical/v1/document"),
            params={"patientId": patient_id, "facilityId": facility_id, "forceQuery": force_query},
            headers=remove_none_from_headers({"X-API-Key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDocumentsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def trigger_query(self, *, patient_id: str, facility_id: str) -> TriggerDocumentsQueryResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "medical/v1/document/query"),
            params={"patientId": patient_id, "facilityId": facility_id},
            headers=remove_none_from_headers({"X-API-Key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TriggerDocumentsQueryResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def download(self, *, file_name: str) -> DownloadDocumentResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "medical/v1/document/downloadUrl"),
            params={"fileName": file_name},
            headers=remove_none_from_headers({"X-API-Key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DownloadDocumentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def get(
        self, *, patient_id: str, facility_id: str, force_query: typing.Optional[str] = None
    ) -> GetDocumentsResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "medical/v1/document"),
                params={"patientId": patient_id, "facilityId": facility_id, "forceQuery": force_query},
                headers=remove_none_from_headers({"X-API-Key": self.api_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDocumentsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def trigger_query(self, *, patient_id: str, facility_id: str) -> TriggerDocumentsQueryResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "medical/v1/document/query"),
                params={"patientId": patient_id, "facilityId": facility_id},
                headers=remove_none_from_headers({"X-API-Key": self.api_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TriggerDocumentsQueryResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def download(self, *, file_name: str) -> DownloadDocumentResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "medical/v1/document/downloadUrl"),
                params={"fileName": file_name},
                headers=remove_none_from_headers({"X-API-Key": self.api_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DownloadDocumentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
