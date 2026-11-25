from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GriptapeCreditsTotals")


@_attrs_define
class GriptapeCreditsTotals:
    """Credits drawn from the organization's balance. Exact: it is what was debited.

    Attributes:
        billed_credits (float):
    """

    billed_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billed_credits = self.billed_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billed_credits": billed_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billed_credits = d.pop("billed_credits")

        griptape_credits_totals = cls(
            billed_credits=billed_credits,
        )

        griptape_credits_totals.additional_properties = d
        return griptape_credits_totals

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
