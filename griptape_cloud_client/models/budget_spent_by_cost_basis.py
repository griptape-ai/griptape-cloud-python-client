from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BudgetSpentByCostBasis")


@_attrs_define
class BudgetSpentByCostBasis:
    """Settled spend in the open window, split by how good each figure is. Which of the three a limit enforces is per-
    budget opt-in, so all three accrue from the day the window opens.

        Attributes:
            billed (float):
            declared (float):
            estimated (float):
    """

    billed: float
    declared: float
    estimated: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billed = self.billed

        declared = self.declared

        estimated = self.estimated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billed": billed,
                "declared": declared,
                "estimated": estimated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billed = d.pop("billed")

        declared = d.pop("declared")

        estimated = d.pop("estimated")

        budget_spent_by_cost_basis = cls(
            billed=billed,
            declared=declared,
            estimated=estimated,
        )

        budget_spent_by_cost_basis.additional_properties = d
        return budget_spent_by_cost_basis

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
