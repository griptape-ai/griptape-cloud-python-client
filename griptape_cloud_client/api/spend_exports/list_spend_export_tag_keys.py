import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.list_spend_export_tag_keys_response_content import ListSpendExportTagKeysResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start: datetime.datetime,
    end: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/spend-exports/tag-keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListSpendExportTagKeysResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]:
    """The tag keys on the organization's spend in a window, by key, other than the ones every export has
    columns for (`project`, `workflow`, `node_type`, `engine_id`). What a client can offer as an
    export's `tag_keys`. The list isn't capped, but an export can name at most 50; to export more, name
    none, which exports every key. Only for organizations whose `can_audit_usage` is true; others get
    403.

    Args:
        start (datetime.datetime): Spend that occurred at or after this instant. At most 366 days
            before `end`.
        end (datetime.datetime): Spend that occurred at or before this instant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]:
    """The tag keys on the organization's spend in a window, by key, other than the ones every export has
    columns for (`project`, `workflow`, `node_type`, `engine_id`). What a client can offer as an
    export's `tag_keys`. The list isn't capped, but an export can name at most 50; to export more, name
    none, which exports every key. Only for organizations whose `can_audit_usage` is true; others get
    403.

    Args:
        start (datetime.datetime): Spend that occurred at or after this instant. At most 366 days
            before `end`.
        end (datetime.datetime): Spend that occurred at or before this instant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]:
    """The tag keys on the organization's spend in a window, by key, other than the ones every export has
    columns for (`project`, `workflow`, `node_type`, `engine_id`). What a client can offer as an
    export's `tag_keys`. The list isn't capped, but an export can name at most 50; to export more, name
    none, which exports every key. Only for organizations whose `can_audit_usage` is true; others get
    403.

    Args:
        start (datetime.datetime): Spend that occurred at or after this instant. At most 366 days
            before `end`.
        end (datetime.datetime): Spend that occurred at or before this instant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]]:
    """The tag keys on the organization's spend in a window, by key, other than the ones every export has
    columns for (`project`, `workflow`, `node_type`, `engine_id`). What a client can offer as an
    export's `tag_keys`. The list isn't capped, but an export can name at most 50; to export more, name
    none, which exports every key. Only for organizations whose `can_audit_usage` is true; others get
    403.

    Args:
        start (datetime.datetime): Spend that occurred at or after this instant. At most 366 days
            before `end`.
        end (datetime.datetime): Spend that occurred at or before this instant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListSpendExportTagKeysResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
        )
    ).parsed
