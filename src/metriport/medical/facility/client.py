# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from .types.base_facility import BaseFacility
from .types.facility import Facility
from .types.list_facilities_response import ListFacilitiesResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FacilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: BaseFacility, request_options: typing.Optional[RequestOptions] = None) -> Facility:
        """
        Creates a Facility in Metriport where your patients receive care.

        Parameters:
            - request: BaseFacility.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport import Address, UsState
        from metriport.client import Metriport
        from metriport.medical import BaseFacility

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.facility.create(
            request=BaseFacility(
                name="Care Facility, LLC",
                npi="1234567891",
                address=Address(
                    address_line_1="2261 Market Street",
                    address_line_2="#4818",
                    city="San Francisco",
                    state=UsState.CA,
                    zip="94114",
                    country="USA",
                ),
                tin="12-3456789",
                active=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/facility"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Facility, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Facility:
        """
        Get a Facility in Metriport where your patients receive care.

        Parameters:
            - id: str. The ID assigned to this Facility. This ID will be used
                       to uniquely identify this Facility in medical documents.
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport.client import Metriport

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.facility.get(
            id="2.16.840.1.113883.3.666.123",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/facility/{id}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Facility, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, id: str, *, request: BaseFacility, request_options: typing.Optional[RequestOptions] = None
    ) -> Facility:
        """
        Updates a Facility in Metriport where your patients receive care.

        Parameters:
            - id: str. The ID of the Facility.

            - request: BaseFacility.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport import Address, UsState
        from metriport.client import Metriport
        from metriport.medical import BaseFacility

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.facility.update(
            id="2.16.840.1.113883.3.666.123",
            request=BaseFacility(
                name="Care Facility, LLC",
                npi="1234567891",
                address=Address(
                    address_line_1="2261 Market Street",
                    address_line_2="#4818",
                    city="San Francisco",
                    state=UsState.CA,
                    zip="94114",
                    country="USA",
                ),
                tin="12-3456789",
                active=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/facility/{id}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Facility, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListFacilitiesResponse:
        """
        Lists all of your Facilities.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport.client import Metriport

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.facility.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/facility"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListFacilitiesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFacilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: BaseFacility, request_options: typing.Optional[RequestOptions] = None
    ) -> Facility:
        """
        Creates a Facility in Metriport where your patients receive care.

        Parameters:
            - request: BaseFacility.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport import Address, UsState
        from metriport.client import AsyncMetriport
        from metriport.medical import BaseFacility

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.facility.create(
            request=BaseFacility(
                name="Care Facility, LLC",
                npi="1234567891",
                address=Address(
                    address_line_1="2261 Market Street",
                    address_line_2="#4818",
                    city="San Francisco",
                    state=UsState.CA,
                    zip="94114",
                    country="USA",
                ),
                tin="12-3456789",
                active=True,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/facility"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Facility, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Facility:
        """
        Get a Facility in Metriport where your patients receive care.

        Parameters:
            - id: str. The ID assigned to this Facility. This ID will be used
                       to uniquely identify this Facility in medical documents.
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport.client import AsyncMetriport

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.facility.get(
            id="2.16.840.1.113883.3.666.123",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/facility/{id}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Facility, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, id: str, *, request: BaseFacility, request_options: typing.Optional[RequestOptions] = None
    ) -> Facility:
        """
        Updates a Facility in Metriport where your patients receive care.

        Parameters:
            - id: str. The ID of the Facility.

            - request: BaseFacility.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport import Address, UsState
        from metriport.client import AsyncMetriport
        from metriport.medical import BaseFacility

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.facility.update(
            id="2.16.840.1.113883.3.666.123",
            request=BaseFacility(
                name="Care Facility, LLC",
                npi="1234567891",
                address=Address(
                    address_line_1="2261 Market Street",
                    address_line_2="#4818",
                    city="San Francisco",
                    state=UsState.CA,
                    zip="94114",
                    country="USA",
                ),
                tin="12-3456789",
                active=True,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/facility/{id}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Facility, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListFacilitiesResponse:
        """
        Lists all of your Facilities.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from metriport.client import AsyncMetriport

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.facility.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/facility"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListFacilitiesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)