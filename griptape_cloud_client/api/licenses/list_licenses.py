from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.license_status import LicenseStatus
from ...models.list_licenses_response_content import ListLicensesResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    status: Union[Unset, LicenseStatus] = UNSET,
    metadata_key: Union[Unset, str] = UNSET,
    metadata_value: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["user_id"] = user_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["metadata_key"] = metadata_key

    params["metadata_value"] = metadata_value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/licenses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListLicensesResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]:
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
    user_id: Union[Unset, str] = UNSET,
    status: Union[Unset, LicenseStatus] = UNSET,
    metadata_key: Union[Unset, str] = UNSET,
    metadata_value: Union[Unset, str] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        user_id (Union[Unset, str]):
        status (Union[Unset, LicenseStatus]):
        metadata_key (Union[Unset, str]):
        metadata_value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        user_id=user_id,
        status=status,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
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
    user_id: Union[Unset, str] = UNSET,
    status: Union[Unset, LicenseStatus] = UNSET,
    metadata_key: Union[Unset, str] = UNSET,
    metadata_value: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        user_id (Union[Unset, str]):
        status (Union[Unset, LicenseStatus]):
        metadata_key (Union[Unset, str]):
        metadata_value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        user_id=user_id,
        status=status,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    status: Union[Unset, LicenseStatus] = UNSET,
    metadata_key: Union[Unset, str] = UNSET,
    metadata_value: Union[Unset, str] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        user_id (Union[Unset, str]):
        status (Union[Unset, LicenseStatus]):
        metadata_key (Union[Unset, str]):
        metadata_value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        user_id=user_id,
        status=status,
        metadata_key=metadata_key,
        metadata_value=metadata_value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    status: Union[Unset, LicenseStatus] = UNSET,
    metadata_key: Union[Unset, str] = UNSET,
    metadata_value: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        user_id (Union[Unset, str]):
        status (Union[Unset, LicenseStatus]):
        metadata_key (Union[Unset, str]):
        metadata_value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListLicensesResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            user_id=user_id,
            status=status,
            metadata_key=metadata_key,
            metadata_value=metadata_value,
        )
    ).parsed
