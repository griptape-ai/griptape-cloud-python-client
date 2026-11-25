from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.report_spend_request_content import ReportSpendRequestContent
from ...models.report_spend_response_content import ReportSpendResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    *,
    body: ReportSpendRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/spend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 201:
        response_201 = ReportSpendResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportSpendRequestContent,
) -> Response[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]:
    """Report spend incurred directly with a provider, or reverse a report by sending `reverses_spend_id`
    alone.

    `tags` has the shape of the X-Griptape-Attribution header's tags; unusable attribution falls back to
    the Default chain rather than rejecting.

    201 for a new row; 200 with the original row on a retry with the same key and body; 409 when the key
    was used for a different report or the row is already reversed; 422 when `occurred_at` is over 24
    hours old or more than 5 minutes ahead, or the amount is implausibly large.

    Args:
        body (ReportSpendRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]
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
    body: ReportSpendRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]:
    """Report spend incurred directly with a provider, or reverse a report by sending `reverses_spend_id`
    alone.

    `tags` has the shape of the X-Griptape-Attribution header's tags; unusable attribution falls back to
    the Default chain rather than rejecting.

    201 for a new row; 200 with the original row on a retry with the same key and body; 409 when the key
    was used for a different report or the row is already reversed; 422 when `occurred_at` is over 24
    hours old or more than 5 minutes ahead, or the amount is implausibly large.

    Args:
        body (ReportSpendRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportSpendRequestContent,
) -> Response[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]:
    """Report spend incurred directly with a provider, or reverse a report by sending `reverses_spend_id`
    alone.

    `tags` has the shape of the X-Griptape-Attribution header's tags; unusable attribution falls back to
    the Default chain rather than rejecting.

    201 for a new row; 200 with the original row on a retry with the same key and body; 409 when the key
    was used for a different report or the row is already reversed; 422 when `occurred_at` is over 24
    hours old or more than 5 minutes ahead, or the amount is implausibly large.

    Args:
        body (ReportSpendRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReportSpendRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]]:
    """Report spend incurred directly with a provider, or reverse a report by sending `reverses_spend_id`
    alone.

    `tags` has the shape of the X-Griptape-Attribution header's tags; unusable attribution falls back to
    the Default chain rather than rejecting.

    201 for a new row; 200 with the original row on a retry with the same key and body; 409 when the key
    was used for a different report or the row is already reversed; 422 when `occurred_at` is over 24
    hours old or more than 5 minutes ahead, or the amount is implausibly large.

    Args:
        body (ReportSpendRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ReportSpendResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
