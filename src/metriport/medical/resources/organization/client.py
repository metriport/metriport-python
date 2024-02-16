# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ....core.api_error import ApiError
from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.jsonable_encoder import jsonable_encoder
from ....core.remove_none_from_dict import remove_none_from_dict
from ....commons.types.address import Address
from .types.org_type import OrgType
from .types.organization import Organization
from .types.organization_create import OrganizationCreate

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class OrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: OrganizationCreate) -> Organization:
        """
        Registers your Organization in Metriport.

        Parameters:
            - request: OrganizationCreate.
        ---
        from metriport import Address, UsState
        from metriport.client import Metriport
        from metriport.resources.medical import OrganizationCreate, OrgType

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.organization.create(
            request=OrganizationCreate(
                name="Metriport Inc.",
                type=OrgType.AMBULATORY,
                location=Address(
                    address_line_1="2261 Market Street",
                    address_line_2="#4818",
                    city="San Francisco",
                    state=UsState.CA,
                    zip="94114",
                    country="USA",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/organization"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Organization, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self) -> Organization:
        """
        Gets the Organization representing your legal corporate entity.

        ---
        from metriport.client import Metriport

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.organization.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/organization"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Organization, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, id: str, *, name: str, type: OrgType, location: Address, e_tag: typing.Optional[str] = None
    ) -> Organization:
        """
        Updates your Organization's details.

        Parameters:
            - id: str. The ID of your organization.

            - name: str. The name of your organization.
                         This is usually your legal corporate entity name -
                         for example `Metriport Inc.`.

            - type: OrgType. The type of your organization.

            - location: Address.

            - e_tag: typing.Optional[str].
        ---
        from metriport import Address, UsState
        from metriport.client import Metriport
        from metriport.resources.medical import OrgType

        client = Metriport(
            api_key="YOUR_API_KEY",
        )
        client.medical.organization.update(
            id="12345678",
            name="Metriport Inc.",
            type=OrgType.AMBULATORY,
            location=Address(
                address_line_1="2261 Market Street",
                address_line_2="#4818",
                city="San Francisco",
                state=UsState.CA,
                zip="94114",
                country="USA",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/organization/{id}"),
            json=jsonable_encoder({"name": name, "type": type, "location": location}),
            headers=remove_none_from_dict({**self._client_wrapper.get_headers(), "ETag": e_tag}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Organization, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, request: OrganizationCreate) -> Organization:
        """
        Registers your Organization in Metriport.

        Parameters:
            - request: OrganizationCreate.
        ---
        from metriport import Address, UsState
        from metriport.client import AsyncMetriport
        from metriport.resources.medical import OrganizationCreate, OrgType

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.organization.create(
            request=OrganizationCreate(
                name="Metriport Inc.",
                type=OrgType.AMBULATORY,
                location=Address(
                    address_line_1="2261 Market Street",
                    address_line_2="#4818",
                    city="San Francisco",
                    state=UsState.CA,
                    zip="94114",
                    country="USA",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/organization"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Organization, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self) -> Organization:
        """
        Gets the Organization representing your legal corporate entity.

        ---
        from metriport.client import AsyncMetriport

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.organization.get()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "medical/v1/organization"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Organization, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, id: str, *, name: str, type: OrgType, location: Address, e_tag: typing.Optional[str] = None
    ) -> Organization:
        """
        Updates your Organization's details.

        Parameters:
            - id: str. The ID of your organization.

            - name: str. The name of your organization.
                         This is usually your legal corporate entity name -
                         for example `Metriport Inc.`.

            - type: OrgType. The type of your organization.

            - location: Address.

            - e_tag: typing.Optional[str].
        ---
        from metriport import Address, UsState
        from metriport.client import AsyncMetriport
        from metriport.resources.medical import OrgType

        client = AsyncMetriport(
            api_key="YOUR_API_KEY",
        )
        await client.medical.organization.update(
            id="12345678",
            name="Metriport Inc.",
            type=OrgType.AMBULATORY,
            location=Address(
                address_line_1="2261 Market Street",
                address_line_2="#4818",
                city="San Francisco",
                state=UsState.CA,
                zip="94114",
                country="USA",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"medical/v1/organization/{id}"),
            json=jsonable_encoder({"name": name, "type": type, "location": location}),
            headers=remove_none_from_dict({**self._client_wrapper.get_headers(), "ETag": e_tag}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Organization, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)