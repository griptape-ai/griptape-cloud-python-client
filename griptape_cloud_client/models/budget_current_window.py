import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_pending_by_cost_basis import BudgetPendingByCostBasis
    from ..models.budget_spent_by_cost_basis import BudgetSpentByCostBasis


T = TypeVar("T", bound="BudgetCurrentWindow")


@_attrs_define
class BudgetCurrentWindow:
    """The counter for the window that is open now, or null when nothing has opened one yet — a budget whose window has
    seen no spend has no counter row.

        Attributes:
            pending_by_cost_basis (BudgetPendingByCostBasis): Credits reserved by in-flight holds. Reported spend is
                declared after the fact and so has no pending state.
            seeded (bool): Whether the window was opened by counting the spend already inside it rather than from zero. True
                for a budget's first window and for the window a reset-period change opens, whether or not that count found
                anything.
            spent_by_cost_basis (BudgetSpentByCostBasis): Settled spend in the open window, split by how good each figure
                is. Which of the three a limit enforces is per-budget opt-in, so all three accrue from the day the window opens.
            window_start (datetime.datetime):
            window_end (Union[Unset, datetime.datetime]): Null for a LIFETIME budget, whose single window never closes.
    """

    pending_by_cost_basis: "BudgetPendingByCostBasis"
    seeded: bool
    spent_by_cost_basis: "BudgetSpentByCostBasis"
    window_start: datetime.datetime
    window_end: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_by_cost_basis = self.pending_by_cost_basis.to_dict()

        seeded = self.seeded

        spent_by_cost_basis = self.spent_by_cost_basis.to_dict()

        window_start = self.window_start.isoformat()

        window_end: Union[Unset, str] = UNSET
        if not isinstance(self.window_end, Unset):
            window_end = self.window_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pending_by_cost_basis": pending_by_cost_basis,
                "seeded": seeded,
                "spent_by_cost_basis": spent_by_cost_basis,
                "window_start": window_start,
            }
        )
        if window_end is not UNSET:
            field_dict["window_end"] = window_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_pending_by_cost_basis import BudgetPendingByCostBasis
        from ..models.budget_spent_by_cost_basis import BudgetSpentByCostBasis

        d = dict(src_dict)
        pending_by_cost_basis = BudgetPendingByCostBasis.from_dict(d.pop("pending_by_cost_basis"))

        seeded = d.pop("seeded")

        spent_by_cost_basis = BudgetSpentByCostBasis.from_dict(d.pop("spent_by_cost_basis"))

        window_start = isoparse(d.pop("window_start"))

        _window_end = d.pop("window_end", UNSET)
        window_end: Union[Unset, datetime.datetime]
        if isinstance(_window_end, Unset):
            window_end = UNSET
        else:
            window_end = isoparse(_window_end)

        budget_current_window = cls(
            pending_by_cost_basis=pending_by_cost_basis,
            seeded=seeded,
            spent_by_cost_basis=spent_by_cost_basis,
            window_start=window_start,
            window_end=window_end,
        )

        budget_current_window.additional_properties = d
        return budget_current_window

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
