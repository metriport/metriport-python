# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import MetriportEnvironment
from .medical.client import AsyncMedicalClient, MedicalClient


class Metriport:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MetriportEnvironment = MetriportEnvironment.PRODUCTION,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.medical = MedicalClient(client_wrapper=self._client_wrapper)


class AsyncMetriport:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MetriportEnvironment = MetriportEnvironment.PRODUCTION,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.medical = AsyncMedicalClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MetriportEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
