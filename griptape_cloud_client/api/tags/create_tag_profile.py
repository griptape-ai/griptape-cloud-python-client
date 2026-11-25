from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.create_tag_profile_request_content import CreateTagProfileRequestContent
from ...models.create_tag_profile_response_content import CreateTagProfileResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTagProfileRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tag-profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 201:
        response_201 = CreateTagProfileResponseContent.from_dict(response.json())

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
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateTagProfileRequestContent,
) -> Response[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]:
    """Describe a recorded tag value. A value has at most one profile, so profiling it again is a 409. Only
    for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        body (CreateTagProfileRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]
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
    client: Union[AuthenticatedClient, Client],
    body: CreateTagProfileRequestContent,
) -> Optional[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]:
    """Describe a recorded tag value. A value has at most one profile, so profiling it again is a 409. Only
    for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        body (CreateTagProfileRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateTagProfileRequestContent,
) -> Response[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]:
    """Describe a recorded tag value. A value has at most one profile, so profiling it again is a 409. Only
    for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        body (CreateTagProfileRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateTagProfileRequestContent,
) -> Optional[Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]]:
    """Describe a recorded tag value. A value has at most one profile, so profiling it again is a 409. Only
    for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        body (CreateTagProfileRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, CreateTagProfileResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
