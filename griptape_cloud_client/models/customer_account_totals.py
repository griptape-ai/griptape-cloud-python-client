from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomerAccountTotals")


@_attrs_define
class CustomerAccountTotals:
    """Cost the customer's own accounts carried. estimated_credits values exact usage we brokered but did not pay for;
    declared_credits is client-reported.

        Attributes:
            declared_credits (float):
            estimated_credits (float):
    """

    declared_credits: float
    estimated_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        declared_credits = self.declared_credits

        estimated_credits = self.estimated_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "declared_credits": declared_credits,
                "estimated_credits": estimated_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declared_credits = d.pop("declared_credits")

        estimated_credits = d.pop("estimated_credits")

        customer_account_totals = cls(
            declared_credits=declared_credits,
            estimated_credits=estimated_credits,
        )

        customer_account_totals.additional_properties = d
        return customer_account_totals

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
