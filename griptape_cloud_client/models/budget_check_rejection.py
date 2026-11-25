from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_enforcement import BudgetEnforcement
from ..models.budget_reset_period import BudgetResetPeriod
from ..models.budget_scope_type import BudgetScopeType

T = TypeVar("T", bound="BudgetCheckRejection")


@_attrs_define
class BudgetCheckRejection:
    """A budget that refused, and the figures it refused on.

    Attributes:
        budget_id (str):
        budget_name (str):
        enforcement (BudgetEnforcement): What exceeding the limit does. SOFT observes and alerts while the work still
            runs; HARD refuses the invocation. A frozen budget refuses whatever its enforcement. Where the organization's
            `can_manage_budgets` is false, budgets keep counting spend but don't refuse or alert.
        frozen (bool):
        includes_byok (bool):
        includes_reported (bool):
        limit_credits (float):
        remaining_credits (float):
        requested_credits (float):
        reset_period (BudgetResetPeriod): How often the spend counter starts over. Boundaries are UTC calendar
            boundaries, and WEEKLY starts on the ISO Monday. LIFETIME is one window, opened at creation and never closed.
        scope_type (BudgetScopeType): What a budget is drawn around. ORG covers every credit-consuming invocation in the
            organization; TAG covers the chains its matchers name; LICENSE and LICENSE_GROUP cover an identity.
        spent_by_cost_basis (Any):
        spent_credits (float):
    """

    budget_id: str
    budget_name: str
    enforcement: BudgetEnforcement
    frozen: bool
    includes_byok: bool
    includes_reported: bool
    limit_credits: float
    remaining_credits: float
    requested_credits: float
    reset_period: BudgetResetPeriod
    scope_type: BudgetScopeType
    spent_by_cost_basis: Any
    spent_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_id = self.budget_id

        budget_name = self.budget_name

        enforcement = self.enforcement.value

        frozen = self.frozen

        includes_byok = self.includes_byok

        includes_reported = self.includes_reported

        limit_credits = self.limit_credits

        remaining_credits = self.remaining_credits

        requested_credits = self.requested_credits

        reset_period = self.reset_period.value

        scope_type = self.scope_type.value

        spent_by_cost_basis = self.spent_by_cost_basis

        spent_credits = self.spent_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_id": budget_id,
                "budget_name": budget_name,
                "enforcement": enforcement,
                "frozen": frozen,
                "includes_byok": includes_byok,
                "includes_reported": includes_reported,
                "limit_credits": limit_credits,
                "remaining_credits": remaining_credits,
                "requested_credits": requested_credits,
                "reset_period": reset_period,
                "scope_type": scope_type,
                "spent_by_cost_basis": spent_by_cost_basis,
                "spent_credits": spent_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_id = d.pop("budget_id")

        budget_name = d.pop("budget_name")

        enforcement = BudgetEnforcement(d.pop("enforcement"))

        frozen = d.pop("frozen")

        includes_byok = d.pop("includes_byok")

        includes_reported = d.pop("includes_reported")

        limit_credits = d.pop("limit_credits")

        remaining_credits = d.pop("remaining_credits")

        requested_credits = d.pop("requested_credits")

        reset_period = BudgetResetPeriod(d.pop("reset_period"))

        scope_type = BudgetScopeType(d.pop("scope_type"))

        spent_by_cost_basis = d.pop("spent_by_cost_basis")

        spent_credits = d.pop("spent_credits")

        budget_check_rejection = cls(
            budget_id=budget_id,
            budget_name=budget_name,
            enforcement=enforcement,
            frozen=frozen,
            includes_byok=includes_byok,
            includes_reported=includes_reported,
            limit_credits=limit_credits,
            remaining_credits=remaining_credits,
            requested_credits=requested_credits,
            reset_period=reset_period,
            scope_type=scope_type,
            spent_by_cost_basis=spent_by_cost_basis,
            spent_credits=spent_credits,
        )

        budget_check_rejection.additional_properties = d
        return budget_check_rejection

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
