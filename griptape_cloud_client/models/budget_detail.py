import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.budget_enforcement import BudgetEnforcement
from ..models.budget_reset_period import BudgetResetPeriod
from ..models.budget_scope_type import BudgetScopeType
from ..models.effective_remaining_basis import EffectiveRemainingBasis
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_current_window import BudgetCurrentWindow
    from ..models.budget_tag_matcher import BudgetTagMatcher
    from ..models.metadata import Metadata


T = TypeVar("T", bound="BudgetDetail")


@_attrs_define
class BudgetDetail:
    """
    Attributes:
        alert_thresholds (list[float]): Percentages of the limit to alert at, deduped and ascending. Never empty: a
            budget with no threshold alerts on nothing. Alerts only where the organization's `can_manage_budgets` is true.
        budget_id (str):
        created_at (datetime.datetime):
        direct_spend_credits (float): Spend attributed at this budget's own scope, excluding anything nested beneath it.
            Only a TAG budget can nest, so for every other scope_type this equals rollup_spend_credits.
        effective_remaining_basis (EffectiveRemainingBasis): How an effective-remaining figure was arrived at. A read
            names no chain, so it can only report the worst case across every budget that could sit above this one.
        effective_remaining_budget_id (str): The budget imposing effective_remaining_credits, which is this budget
            itself when nothing above it binds first.
        effective_remaining_budget_name (str):
        effective_remaining_credits (float): The smallest headroom this budget and every budget above it leave. A budget
            with 400 left underneath one with 13 left has 13 to spend.
        enabled (bool):
        enforcement (BudgetEnforcement): What exceeding the limit does. SOFT observes and alerts while the work still
            runs; HARD refuses the invocation. A frozen budget refuses whatever its enforcement. Where the organization's
            `can_manage_budgets` is false, budgets keep counting spend but don't refuse or alert.
        frozen (bool): Refuse invocations this budget covers regardless of how much is left, whatever its enforcement.
            The organization default cannot be frozen. Refuses only where the organization's `can_manage_budgets` is true.
        includes_byok (bool): Count spend the customer's own provider credentials paid for against this limit.
        includes_reported (bool): Count client-reported spend against this limit.
        is_default (bool): The organization default: the catch-all every unmatched invocation counts against.
            Provisioned by the service, one per organization, on its first budget list read or create where
            `can_manage_budgets` is true; an organization that later loses budgets keeps it. It cannot be deleted, made
            HARD, or frozen.
        is_favorite (bool): The calling account has starred this budget. Private to that account.
        limit_credits (float): The cap, in credits. Zero is valid and is the block-everything idiom.
        matchers (list['BudgetTagMatcher']): Empty unless scope_type is TAG.
        metadata (Metadata):
        name (str):
        organization_id (str):
        pending_credits (float):
        percent_used (float): Spend against the limit. A zero-limit budget reads 0 until anything is spent and 100
            after.
        remaining_credits (float): Headroom left in the open window. Negative when the budget is over its limit, by the
            amount it is over.
        reset_period (BudgetResetPeriod): How often the spend counter starts over. Boundaries are UTC calendar
            boundaries, and WEEKLY starts on the ISO Monday. LIFETIME is one window, opened at creation and never closed.
        rollup_spend_credits (float): Spend attributed at this budget's scope plus everything nested beneath it.
            Enforcement reads this figure.
        scope_type (BudgetScopeType): What a budget is drawn around. ORG covers every credit-consuming invocation in the
            organization; TAG covers the chains its matchers name; LICENSE and LICENSE_GROUP cover an identity.
        updated_at (datetime.datetime):
        current_window (Union[Unset, BudgetCurrentWindow]): The counter for the window that is open now, or null when
            nothing has opened one yet — a budget whose window has seen no spend has no counter row.
        scope_license_group_id (Union[Unset, str]): Set only when scope_type is LICENSE_GROUP.
        scope_license_id (Union[Unset, str]): Set only when scope_type is LICENSE.
    """

    alert_thresholds: list[float]
    budget_id: str
    created_at: datetime.datetime
    direct_spend_credits: float
    effective_remaining_basis: EffectiveRemainingBasis
    effective_remaining_budget_id: str
    effective_remaining_budget_name: str
    effective_remaining_credits: float
    enabled: bool
    enforcement: BudgetEnforcement
    frozen: bool
    includes_byok: bool
    includes_reported: bool
    is_default: bool
    is_favorite: bool
    limit_credits: float
    matchers: list["BudgetTagMatcher"]
    metadata: "Metadata"
    name: str
    organization_id: str
    pending_credits: float
    percent_used: float
    remaining_credits: float
    reset_period: BudgetResetPeriod
    rollup_spend_credits: float
    scope_type: BudgetScopeType
    updated_at: datetime.datetime
    current_window: Union[Unset, "BudgetCurrentWindow"] = UNSET
    scope_license_group_id: Union[Unset, str] = UNSET
    scope_license_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_thresholds = self.alert_thresholds

        budget_id = self.budget_id

        created_at = self.created_at.isoformat()

        direct_spend_credits = self.direct_spend_credits

        effective_remaining_basis = self.effective_remaining_basis.value

        effective_remaining_budget_id = self.effective_remaining_budget_id

        effective_remaining_budget_name = self.effective_remaining_budget_name

        effective_remaining_credits = self.effective_remaining_credits

        enabled = self.enabled

        enforcement = self.enforcement.value

        frozen = self.frozen

        includes_byok = self.includes_byok

        includes_reported = self.includes_reported

        is_default = self.is_default

        is_favorite = self.is_favorite

        limit_credits = self.limit_credits

        matchers = []
        for matchers_item_data in self.matchers:
            matchers_item = matchers_item_data.to_dict()
            matchers.append(matchers_item)

        metadata = self.metadata.to_dict()

        name = self.name

        organization_id = self.organization_id

        pending_credits = self.pending_credits

        percent_used = self.percent_used

        remaining_credits = self.remaining_credits

        reset_period = self.reset_period.value

        rollup_spend_credits = self.rollup_spend_credits

        scope_type = self.scope_type.value

        updated_at = self.updated_at.isoformat()

        current_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_window, Unset):
            current_window = self.current_window.to_dict()

        scope_license_group_id = self.scope_license_group_id

        scope_license_id = self.scope_license_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_thresholds": alert_thresholds,
                "budget_id": budget_id,
                "created_at": created_at,
                "direct_spend_credits": direct_spend_credits,
                "effective_remaining_basis": effective_remaining_basis,
                "effective_remaining_budget_id": effective_remaining_budget_id,
                "effective_remaining_budget_name": effective_remaining_budget_name,
                "effective_remaining_credits": effective_remaining_credits,
                "enabled": enabled,
                "enforcement": enforcement,
                "frozen": frozen,
                "includes_byok": includes_byok,
                "includes_reported": includes_reported,
                "is_default": is_default,
                "is_favorite": is_favorite,
                "limit_credits": limit_credits,
                "matchers": matchers,
                "metadata": metadata,
                "name": name,
                "organization_id": organization_id,
                "pending_credits": pending_credits,
                "percent_used": percent_used,
                "remaining_credits": remaining_credits,
                "reset_period": reset_period,
                "rollup_spend_credits": rollup_spend_credits,
                "scope_type": scope_type,
                "updated_at": updated_at,
            }
        )
        if current_window is not UNSET:
            field_dict["current_window"] = current_window
        if scope_license_group_id is not UNSET:
            field_dict["scope_license_group_id"] = scope_license_group_id
        if scope_license_id is not UNSET:
            field_dict["scope_license_id"] = scope_license_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_current_window import BudgetCurrentWindow
        from ..models.budget_tag_matcher import BudgetTagMatcher
        from ..models.metadata import Metadata

        d = dict(src_dict)
        alert_thresholds = cast(list[float], d.pop("alert_thresholds"))

        budget_id = d.pop("budget_id")

        created_at = isoparse(d.pop("created_at"))

        direct_spend_credits = d.pop("direct_spend_credits")

        effective_remaining_basis = EffectiveRemainingBasis(d.pop("effective_remaining_basis"))

        effective_remaining_budget_id = d.pop("effective_remaining_budget_id")

        effective_remaining_budget_name = d.pop("effective_remaining_budget_name")

        effective_remaining_credits = d.pop("effective_remaining_credits")

        enabled = d.pop("enabled")

        enforcement = BudgetEnforcement(d.pop("enforcement"))

        frozen = d.pop("frozen")

        includes_byok = d.pop("includes_byok")

        includes_reported = d.pop("includes_reported")

        is_default = d.pop("is_default")

        is_favorite = d.pop("is_favorite")

        limit_credits = d.pop("limit_credits")

        matchers = []
        _matchers = d.pop("matchers")
        for matchers_item_data in _matchers:
            matchers_item = BudgetTagMatcher.from_dict(matchers_item_data)

            matchers.append(matchers_item)

        metadata = Metadata.from_dict(d.pop("metadata"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        pending_credits = d.pop("pending_credits")

        percent_used = d.pop("percent_used")

        remaining_credits = d.pop("remaining_credits")

        reset_period = BudgetResetPeriod(d.pop("reset_period"))

        rollup_spend_credits = d.pop("rollup_spend_credits")

        scope_type = BudgetScopeType(d.pop("scope_type"))

        updated_at = isoparse(d.pop("updated_at"))

        _current_window = d.pop("current_window", UNSET)
        current_window: Union[Unset, BudgetCurrentWindow]
        if isinstance(_current_window, Unset):
            current_window = UNSET
        else:
            current_window = BudgetCurrentWindow.from_dict(_current_window)

        scope_license_group_id = d.pop("scope_license_group_id", UNSET)

        scope_license_id = d.pop("scope_license_id", UNSET)

        budget_detail = cls(
            alert_thresholds=alert_thresholds,
            budget_id=budget_id,
            created_at=created_at,
            direct_spend_credits=direct_spend_credits,
            effective_remaining_basis=effective_remaining_basis,
            effective_remaining_budget_id=effective_remaining_budget_id,
            effective_remaining_budget_name=effective_remaining_budget_name,
            effective_remaining_credits=effective_remaining_credits,
            enabled=enabled,
            enforcement=enforcement,
            frozen=frozen,
            includes_byok=includes_byok,
            includes_reported=includes_reported,
            is_default=is_default,
            is_favorite=is_favorite,
            limit_credits=limit_credits,
            matchers=matchers,
            metadata=metadata,
            name=name,
            organization_id=organization_id,
            pending_credits=pending_credits,
            percent_used=percent_used,
            remaining_credits=remaining_credits,
            reset_period=reset_period,
            rollup_spend_credits=rollup_spend_credits,
            scope_type=scope_type,
            updated_at=updated_at,
            current_window=current_window,
            scope_license_group_id=scope_license_group_id,
            scope_license_id=scope_license_id,
        )

        budget_detail.additional_properties = d
        return budget_detail

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
