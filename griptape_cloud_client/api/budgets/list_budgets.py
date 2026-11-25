from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget_scope_type import BudgetScopeType
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.list_budgets_response_content import ListBudgetsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    scope_type: Union[Unset, BudgetScopeType] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    favorite: Union[Unset, bool] = UNSET,
    applies_to_value: Union[Unset, str] = UNSET,
    applies_to_license: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_scope_type: Union[Unset, str] = UNSET
    if not isinstance(scope_type, Unset):
        json_scope_type = scope_type.value

    params["scope_type"] = json_scope_type

    params["enabled"] = enabled

    params["favorite"] = favorite

    params["applies_to_value"] = applies_to_value

    params["applies_to_license"] = applies_to_license

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/budgets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListBudgetsResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]:
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
    scope_type: Union[Unset, BudgetScopeType] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    favorite: Union[Unset, bool] = UNSET,
    applies_to_value: Union[Unset, str] = UNSET,
    applies_to_license: Union[Unset, str] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        scope_type (Union[Unset, BudgetScopeType]): What a budget is drawn around. ORG covers
            every credit-consuming invocation in the organization; TAG covers the chains its matchers
            name; LICENSE and LICENSE_GROUP cover an identity.
        enabled (Union[Unset, bool]):
        favorite (Union[Unset, bool]): Only budgets the calling account has starred. Another
            account's stars are never visible.
        applies_to_value (Union[Unset, str]): Only TAG budgets one of whose matcher values ends at
            this tag value.
        applies_to_license (Union[Unset, str]): Only budgets whose scope covers this license: the
            organization budgets, the license's own, and those of the groups it belonged to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        scope_type=scope_type,
        enabled=enabled,
        favorite=favorite,
        applies_to_value=applies_to_value,
        applies_to_license=applies_to_license,
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
    scope_type: Union[Unset, BudgetScopeType] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    favorite: Union[Unset, bool] = UNSET,
    applies_to_value: Union[Unset, str] = UNSET,
    applies_to_license: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        scope_type (Union[Unset, BudgetScopeType]): What a budget is drawn around. ORG covers
            every credit-consuming invocation in the organization; TAG covers the chains its matchers
            name; LICENSE and LICENSE_GROUP cover an identity.
        enabled (Union[Unset, bool]):
        favorite (Union[Unset, bool]): Only budgets the calling account has starred. Another
            account's stars are never visible.
        applies_to_value (Union[Unset, str]): Only TAG budgets one of whose matcher values ends at
            this tag value.
        applies_to_license (Union[Unset, str]): Only budgets whose scope covers this license: the
            organization budgets, the license's own, and those of the groups it belonged to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        scope_type=scope_type,
        enabled=enabled,
        favorite=favorite,
        applies_to_value=applies_to_value,
        applies_to_license=applies_to_license,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    scope_type: Union[Unset, BudgetScopeType] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    favorite: Union[Unset, bool] = UNSET,
    applies_to_value: Union[Unset, str] = UNSET,
    applies_to_license: Union[Unset, str] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        scope_type (Union[Unset, BudgetScopeType]): What a budget is drawn around. ORG covers
            every credit-consuming invocation in the organization; TAG covers the chains its matchers
            name; LICENSE and LICENSE_GROUP cover an identity.
        enabled (Union[Unset, bool]):
        favorite (Union[Unset, bool]): Only budgets the calling account has starred. Another
            account's stars are never visible.
        applies_to_value (Union[Unset, str]): Only TAG budgets one of whose matcher values ends at
            this tag value.
        applies_to_license (Union[Unset, str]): Only budgets whose scope covers this license: the
            organization budgets, the license's own, and those of the groups it belonged to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        scope_type=scope_type,
        enabled=enabled,
        favorite=favorite,
        applies_to_value=applies_to_value,
        applies_to_license=applies_to_license,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    scope_type: Union[Unset, BudgetScopeType] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    favorite: Union[Unset, bool] = UNSET,
    applies_to_value: Union[Unset, str] = UNSET,
    applies_to_license: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        scope_type (Union[Unset, BudgetScopeType]): What a budget is drawn around. ORG covers
            every credit-consuming invocation in the organization; TAG covers the chains its matchers
            name; LICENSE and LICENSE_GROUP cover an identity.
        enabled (Union[Unset, bool]):
        favorite (Union[Unset, bool]): Only budgets the calling account has starred. Another
            account's stars are never visible.
        applies_to_value (Union[Unset, str]): Only TAG budgets one of whose matcher values ends at
            this tag value.
        applies_to_license (Union[Unset, str]): Only budgets whose scope covers this license: the
            organization budgets, the license's own, and those of the groups it belonged to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListBudgetsResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            scope_type=scope_type,
            enabled=enabled,
            favorite=favorite,
            applies_to_value=applies_to_value,
            applies_to_license=applies_to_license,
        )
    ).parsed
