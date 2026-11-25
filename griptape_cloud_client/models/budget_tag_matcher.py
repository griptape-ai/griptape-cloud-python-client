from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BudgetTagMatcher")


@_attrs_define
class BudgetTagMatcher:
    """One tag chain a TAG budget covers. Only TAG budgets carry matchers, and a TAG budget other than the organization
    default needs at least one.

        Attributes:
            key (str): The tag dimension this chain is matched in. Defaults to `project`.
            matcher_id (str):
            value (list[str]): Tag values, leaf first and root last: [B, A] is B under A. Root-anchored, so it matches the
                chains [B, A] and [C, B, A] but not [B, X] — the same leaf under a different parent is a different thing to
                count.
    """

    key: str
    matcher_id: str
    value: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        matcher_id = self.matcher_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "matcher_id": matcher_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        matcher_id = d.pop("matcher_id")

        value = cast(list[str], d.pop("value"))

        budget_tag_matcher = cls(
            key=key,
            matcher_id=matcher_id,
            value=value,
        )

        budget_tag_matcher.additional_properties = d
        return budget_tag_matcher

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
