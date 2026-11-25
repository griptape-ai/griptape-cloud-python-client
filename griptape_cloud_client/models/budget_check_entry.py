from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_enforcement import BudgetEnforcement
from ..models.budget_scope_type import BudgetScopeType

T = TypeVar("T", bound="BudgetCheckEntry")


@_attrs_define
class BudgetCheckEntry:
    """One budget's line in a budget check.

    Attributes:
        budget_id (str):
        budget_name (str):
        enforcement (BudgetEnforcement): What exceeding the limit does. SOFT observes and alerts while the work still
            runs; HARD refuses the invocation. A frozen budget refuses whatever its enforcement. Where the organization's
            `can_manage_budgets` is false, budgets keep counting spend but don't refuse or alert.
        gated (bool): Whether this budget could refuse: HARD, or frozen.
        scope_type (BudgetScopeType): What a budget is drawn around. ORG covers every credit-consuming invocation in the
            organization; TAG covers the chains its matchers name; LICENSE and LICENSE_GROUP cover an identity.
        would_block (bool):
    """

    budget_id: str
    budget_name: str
    enforcement: BudgetEnforcement
    gated: bool
    scope_type: BudgetScopeType
    would_block: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_id = self.budget_id

        budget_name = self.budget_name

        enforcement = self.enforcement.value

        gated = self.gated

        scope_type = self.scope_type.value

        would_block = self.would_block

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_id": budget_id,
                "budget_name": budget_name,
                "enforcement": enforcement,
                "gated": gated,
                "scope_type": scope_type,
                "would_block": would_block,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_id = d.pop("budget_id")

        budget_name = d.pop("budget_name")

        enforcement = BudgetEnforcement(d.pop("enforcement"))

        gated = d.pop("gated")

        scope_type = BudgetScopeType(d.pop("scope_type"))

        would_block = d.pop("would_block")

        budget_check_entry = cls(
            budget_id=budget_id,
            budget_name=budget_name,
            enforcement=enforcement,
            gated=gated,
            scope_type=scope_type,
            would_block=would_block,
        )

        budget_check_entry.additional_properties = d
        return budget_check_entry

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
