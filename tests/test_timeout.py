"""Public-request regressions for configured and per-request timeouts."""

import asyncio
import typing

import httpx
import pytest

from metriport.client import AsyncMetriport, Metriport
from metriport.core.api_error import ApiError


RESOURCES = [
    ("organization", "get", {}),
    ("facility", "list", {}),
    ("patient", "list", {}),
    ("document", "get_query_status", {"patient_id": "synthetic-patient"}),
    ("fhir", "get_consolidated_query_status", {"id": "synthetic-patient"}),
]
SETTINGS = [
    "default",
    "constructor",
    "disabled",
    "empty_options",
    "override",
    "zero",
    "custom_client",
]


def run_case(
    resource: str,
    method: str,
    arguments: typing.Dict[str, str],
    setting: str,
    asynchronous: bool,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: typing.List[httpx.Request] = []
    expected = httpx.Timeout(60).as_dict()
    kwargs: typing.Dict[str, typing.Any] = {
        "api_key": "synthetic-key",
        "base_url": "https://example.invalid",
    }
    options: typing.Any = None
    if setting in ("constructor", "empty_options", "override", "zero"):
        kwargs["timeout"] = 15
        expected = httpx.Timeout(15).as_dict()
    if setting == "disabled":
        kwargs["timeout"] = None
        expected = httpx.Timeout(None).as_dict()
    if setting == "empty_options":
        options = {}
    if setting in ("override", "zero"):
        timeout = 7 if setting == "override" else 0
        options = {"timeout_in_seconds": timeout}
        expected = httpx.Timeout(timeout).as_dict()
    custom_timeout = httpx.Timeout(2, connect=1, write=3, pool=4)

    def response(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(
            503, json={"error": "synthetic response"}, request=request
        )

    if asynchronous:

        async def send_async(
            self: httpx.AsyncClient, request: httpx.Request, **kw: typing.Any
        ) -> httpx.Response:
            return response(request)

        monkeypatch.setattr(httpx.AsyncClient, "send", send_async)

        async def execute() -> None:
            async with httpx.AsyncClient(timeout=custom_timeout) as transport:
                if setting == "custom_client":
                    kwargs["httpx_client"] = transport
                client = AsyncMetriport(**kwargs)
                try:
                    with pytest.raises(ApiError) as error:
                        await getattr(getattr(client.medical, resource), method)(
                            **arguments, request_options=options
                        )
                    assert error.value.status_code == 503
                finally:
                    await client._client_wrapper.httpx_client.aclose()

        asyncio.run(execute())
    else:

        def send_sync(
            self: httpx.Client, request: httpx.Request, **kw: typing.Any
        ) -> httpx.Response:
            return response(request)

        monkeypatch.setattr(httpx.Client, "send", send_sync)
        with httpx.Client(timeout=custom_timeout) as transport:
            if setting == "custom_client":
                kwargs["httpx_client"] = transport
            client = Metriport(**kwargs)
            try:
                with pytest.raises(ApiError) as error:
                    getattr(getattr(client.medical, resource), method)(
                        **arguments, request_options=options
                    )
                assert error.value.status_code == 503
            finally:
                client._client_wrapper.httpx_client.close()
    if setting == "custom_client":
        expected = custom_timeout.as_dict()
    assert len(captured) == 1
    assert captured[0].url.host == "example.invalid"
    assert captured[0].headers["X-API-Key"] == "synthetic-key"
    assert captured[0].extensions["timeout"] == expected


@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("setting", SETTINGS)
@pytest.mark.parametrize("resource,method,arguments", RESOURCES)
def test_request_timeout(
    resource: str,
    method: str,
    arguments: typing.Dict[str, str],
    setting: str,
    asynchronous: bool,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    run_case(resource, method, arguments, setting, asynchronous, monkeypatch)
