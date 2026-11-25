from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.search_spend_request_content import SearchSpendRequestContent
from ...models.search_spend_response_content import SearchSpendResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchSpendRequestContent,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/spend/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = SearchSpendResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchSpendRequestContent,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
) -> Response[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]:
    """Search the organization's spend, newest first. Pagination is in the query string.

    Each entry in `tag_filters` names a tag key and the value to match within it, ordered leaf first and
    root last, so [B, A] is B under A. Matching is root-anchored: [B, A] matches [B, A] and [C, B, A],
    but not [B, X]. A bare string is read as a one-entry value. Filters combine with AND, and a key may
    be filtered on only once.

    Only for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        body (SearchSpendRequestContent): The filters a spend search takes, shared with a spend
            export so the export holds exactly the rows the search matches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        body=body,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchSpendRequestContent,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]:
    """Search the organization's spend, newest first. Pagination is in the query string.

    Each entry in `tag_filters` names a tag key and the value to match within it, ordered leaf first and
    root last, so [B, A] is B under A. Matching is root-anchored: [B, A] matches [B, A] and [C, B, A],
    but not [B, X]. A bare string is read as a one-entry value. Filters combine with AND, and a key may
    be filtered on only once.

    Only for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        body (SearchSpendRequestContent): The filters a spend search takes, shared with a spend
            export so the export holds exactly the rows the search matches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        body=body,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchSpendRequestContent,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
) -> Response[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]:
    """Search the organization's spend, newest first. Pagination is in the query string.

    Each entry in `tag_filters` names a tag key and the value to match within it, ordered leaf first and
    root last, so [B, A] is B under A. Matching is root-anchored: [B, A] matches [B, A] and [C, B, A],
    but not [B, X]. A bare string is read as a one-entry value. Filters combine with AND, and a key may
    be filtered on only once.

    Only for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        body (SearchSpendRequestContent): The filters a spend search takes, shared with a spend
            export so the export holds exactly the rows the search matches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        body=body,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchSpendRequestContent,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]]:
    """Search the organization's spend, newest first. Pagination is in the query string.

    Each entry in `tag_filters` names a tag key and the value to match within it, ordered leaf first and
    root last, so [B, A] is B under A. Matching is root-anchored: [B, A] matches [B, A] and [C, B, A],
    but not [B, X]. A bare string is read as a one-entry value. Filters combine with AND, and a key may
    be filtered on only once.

    Only for organizations whose `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        body (SearchSpendRequestContent): The filters a spend search takes, shared with a spend
            export so the export holds exactly the rows the search matches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, SearchSpendResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page=page,
            page_size=page_size,
        )
    ).parsed
