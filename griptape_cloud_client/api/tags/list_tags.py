import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.list_tags_response_content import ListTagsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    key: Union[Unset, str] = UNSET,
    matched: Union[Unset, bool] = UNSET,
    leaf: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["key"] = key

    params["matched"] = matched

    params["leaf"] = leaf

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListTagsResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    key: Union[Unset, str] = UNSET,
    matched: Union[Unset, bool] = UNSET,
    leaf: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]:
    """The distinct tags reported for one key in a window, one per value, most recently seen first.
    `matched=false` lists the tags no enabled budget covers. Only for organizations whose
    `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        key (Union[Unset, str]): The tag dimension to list. Defaults to `project`; only keys
            budgets can match on are accepted.
        matched (Union[Unset, bool]): true for tags some enabled budget covers, false for those
            none does.
        leaf (Union[Unset, str]): Only tags whose value starts with this leaf.
        start (Union[Unset, datetime.datetime]): Defaults to 90 days before end. The window may
            span at most 366 days.
        end (Union[Unset, datetime.datetime]): Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        key=key,
        matched=matched,
        leaf=leaf,
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
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    key: Union[Unset, str] = UNSET,
    matched: Union[Unset, bool] = UNSET,
    leaf: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]:
    """The distinct tags reported for one key in a window, one per value, most recently seen first.
    `matched=false` lists the tags no enabled budget covers. Only for organizations whose
    `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        key (Union[Unset, str]): The tag dimension to list. Defaults to `project`; only keys
            budgets can match on are accepted.
        matched (Union[Unset, bool]): true for tags some enabled budget covers, false for those
            none does.
        leaf (Union[Unset, str]): Only tags whose value starts with this leaf.
        start (Union[Unset, datetime.datetime]): Defaults to 90 days before end. The window may
            span at most 366 days.
        end (Union[Unset, datetime.datetime]): Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        key=key,
        matched=matched,
        leaf=leaf,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    key: Union[Unset, str] = UNSET,
    matched: Union[Unset, bool] = UNSET,
    leaf: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]:
    """The distinct tags reported for one key in a window, one per value, most recently seen first.
    `matched=false` lists the tags no enabled budget covers. Only for organizations whose
    `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        key (Union[Unset, str]): The tag dimension to list. Defaults to `project`; only keys
            budgets can match on are accepted.
        matched (Union[Unset, bool]): true for tags some enabled budget covers, false for those
            none does.
        leaf (Union[Unset, str]): Only tags whose value starts with this leaf.
        start (Union[Unset, datetime.datetime]): Defaults to 90 days before end. The window may
            span at most 366 days.
        end (Union[Unset, datetime.datetime]): Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        key=key,
        matched=matched,
        leaf=leaf,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    key: Union[Unset, str] = UNSET,
    matched: Union[Unset, bool] = UNSET,
    leaf: Union[Unset, str] = UNSET,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]]:
    """The distinct tags reported for one key in a window, one per value, most recently seen first.
    `matched=false` lists the tags no enabled budget covers. Only for organizations whose
    `can_audit_usage` is true; others get 403.

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        key (Union[Unset, str]): The tag dimension to list. Defaults to `project`; only keys
            budgets can match on are accepted.
        matched (Union[Unset, bool]): true for tags some enabled budget covers, false for those
            none does.
        leaf (Union[Unset, str]): Only tags whose value starts with this leaf.
        start (Union[Unset, datetime.datetime]): Defaults to 90 days before end. The window may
            span at most 366 days.
        end (Union[Unset, datetime.datetime]): Defaults to now.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListTagsResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            key=key,
            matched=matched,
            leaf=leaf,
            start=start,
            end=end,
        )
    ).parsed
