from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.create_chat_message_stream_request_content import CreateChatMessageStreamRequestContent
from ...models.create_chat_message_stream_response_content import CreateChatMessageStreamResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    *,
    body: CreateChatMessageStreamRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/messages/stream",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientErrorResponseContent | CreateChatMessageStreamResponseContent | ServiceErrorResponseContent | None:
    if response.status_code == 201:
        response_201 = CreateChatMessageStreamResponseContent.from_dict(response.json())

        return response_201

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
) -> Response[ClientErrorResponseContent | CreateChatMessageStreamResponseContent | ServiceErrorResponseContent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateChatMessageStreamRequestContent,
) -> Response[ClientErrorResponseContent | CreateChatMessageStreamResponseContent | ServiceErrorResponseContent]:
    """Args:
        body (CreateChatMessageStreamRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, CreateChatMessageStreamResponseContent, ServiceErrorResponseContent]]
    """
    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateChatMessageStreamRequestContent,
) -> ClientErrorResponseContent | CreateChatMessageStreamResponseContent | ServiceErrorResponseContent | None:
    """Args:
        body (CreateChatMessageStreamRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, CreateChatMessageStreamResponseContent, ServiceErrorResponseContent]
    """
    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateChatMessageStreamRequestContent,
) -> Response[ClientErrorResponseContent | CreateChatMessageStreamResponseContent | ServiceErrorResponseContent]:
    """Args:
        body (CreateChatMessageStreamRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, CreateChatMessageStreamResponseContent, ServiceErrorResponseContent]]
    """
    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateChatMessageStreamRequestContent,
) -> ClientErrorResponseContent | CreateChatMessageStreamResponseContent | ServiceErrorResponseContent | None:
    """Args:
        body (CreateChatMessageStreamRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, CreateChatMessageStreamResponseContent, ServiceErrorResponseContent]
    """
    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
