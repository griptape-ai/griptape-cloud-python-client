from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_check_entry import BudgetCheckEntry
    from ..models.budget_check_rejection import BudgetCheckRejection


T = TypeVar("T", bound="CreateBudgetCheckResponseContent")


@_attrs_define
class CreateBudgetCheckResponseContent:
    """
    Attributes:
        allowed (bool):
        blocked_by (list['BudgetCheckRejection']):
        checked_budgets (list['BudgetCheckEntry']):
        correlation_id (Union[Unset, str]):
        effective_remaining_credits (Union[Unset, float]): The least headroom among budgets that count reported spend;
            null when none do.
        spend_id (Union[Unset, str]): The BLOCKED receipt, when refused.
    """

    allowed: bool
    blocked_by: list["BudgetCheckRejection"]
    checked_budgets: list["BudgetCheckEntry"]
    correlation_id: Union[Unset, str] = UNSET
    effective_remaining_credits: Union[Unset, float] = UNSET
    spend_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        blocked_by = []
        for blocked_by_item_data in self.blocked_by:
            blocked_by_item = blocked_by_item_data.to_dict()
            blocked_by.append(blocked_by_item)

        checked_budgets = []
        for checked_budgets_item_data in self.checked_budgets:
            checked_budgets_item = checked_budgets_item_data.to_dict()
            checked_budgets.append(checked_budgets_item)

        correlation_id = self.correlation_id

        effective_remaining_credits = self.effective_remaining_credits

        spend_id = self.spend_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed": allowed,
                "blocked_by": blocked_by,
                "checked_budgets": checked_budgets,
            }
        )
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if effective_remaining_credits is not UNSET:
            field_dict["effective_remaining_credits"] = effective_remaining_credits
        if spend_id is not UNSET:
            field_dict["spend_id"] = spend_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_check_entry import BudgetCheckEntry
        from ..models.budget_check_rejection import BudgetCheckRejection

        d = dict(src_dict)
        allowed = d.pop("allowed")

        blocked_by = []
        _blocked_by = d.pop("blocked_by")
        for blocked_by_item_data in _blocked_by:
            blocked_by_item = BudgetCheckRejection.from_dict(blocked_by_item_data)

            blocked_by.append(blocked_by_item)

        checked_budgets = []
        _checked_budgets = d.pop("checked_budgets")
        for checked_budgets_item_data in _checked_budgets:
            checked_budgets_item = BudgetCheckEntry.from_dict(checked_budgets_item_data)

            checked_budgets.append(checked_budgets_item)

        correlation_id = d.pop("correlation_id", UNSET)

        effective_remaining_credits = d.pop("effective_remaining_credits", UNSET)

        spend_id = d.pop("spend_id", UNSET)

        create_budget_check_response_content = cls(
            allowed=allowed,
            blocked_by=blocked_by,
            checked_budgets=checked_budgets,
            correlation_id=correlation_id,
            effective_remaining_credits=effective_remaining_credits,
            spend_id=spend_id,
        )

        create_budget_check_response_content.additional_properties = d
        return create_budget_check_response_content

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
