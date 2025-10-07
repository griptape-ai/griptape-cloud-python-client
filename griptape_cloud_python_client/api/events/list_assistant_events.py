from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.list_assistant_events_response_content import ListAssistantEventsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    assistant_run_id: str,
    *,
    limit: Unset | str = UNSET,
    offset: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/assistant-runs/{assistant_run_id}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientErrorResponseContent | ListAssistantEventsResponseContent | ServiceErrorResponseContent | None:
    if response.status_code == 200:
        response_200 = ListAssistantEventsResponseContent.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ClientErrorResponseContent.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ClientErrorResponseContent.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ClientErrorResponseContent.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ClientErrorResponseContent.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = ClientErrorResponseContent.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = ClientErrorResponseContent.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ClientErrorResponseContent.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ServiceErrorResponseContent.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClientErrorResponseContent | ListAssistantEventsResponseContent | ServiceErrorResponseContent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assistant_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: Unset | str = UNSET,
    offset: Unset | str = UNSET,
) -> Response[ClientErrorResponseContent | ListAssistantEventsResponseContent | ServiceErrorResponseContent]:
    """Args:
        assistant_run_id (str):
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListAssistantEventsResponseContent, ServiceErrorResponseContent]]
    """
    kwargs = _get_kwargs(
        assistant_run_id=assistant_run_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assistant_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: Unset | str = UNSET,
    offset: Unset | str = UNSET,
) -> ClientErrorResponseContent | ListAssistantEventsResponseContent | ServiceErrorResponseContent | None:
    """Args:
        assistant_run_id (str):
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListAssistantEventsResponseContent, ServiceErrorResponseContent]
    """
    return sync_detailed(
        assistant_run_id=assistant_run_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    assistant_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: Unset | str = UNSET,
    offset: Unset | str = UNSET,
) -> Response[ClientErrorResponseContent | ListAssistantEventsResponseContent | ServiceErrorResponseContent]:
    """Args:
        assistant_run_id (str):
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListAssistantEventsResponseContent, ServiceErrorResponseContent]]
    """
    kwargs = _get_kwargs(
        assistant_run_id=assistant_run_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assistant_run_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: Unset | str = UNSET,
    offset: Unset | str = UNSET,
) -> ClientErrorResponseContent | ListAssistantEventsResponseContent | ServiceErrorResponseContent | None:
    """Args:
        assistant_run_id (str):
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListAssistantEventsResponseContent, ServiceErrorResponseContent]
    """
    return (
        await asyncio_detailed(
            assistant_run_id=assistant_run_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
