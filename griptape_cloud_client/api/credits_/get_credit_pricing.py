import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.get_credit_pricing_response_content import GetCreditPricingResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    at: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_at: Union[Unset, str] = UNSET
    if not isinstance(at, Unset):
        json_at = at.isoformat()
    params["at"] = json_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/credits/pricing",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = GetCreditPricingResponseContent.from_dict(response.json())

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
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        at (Union[Unset, datetime.datetime]): Price as of this instant. Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        at=at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        at (Union[Unset, datetime.datetime]): Price as of this instant. Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        at (Union[Unset, datetime.datetime]): Price as of this instant. Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        at (Union[Unset, datetime.datetime]): Price as of this instant. Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, GetCreditPricingResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
        )
    ).parsed
