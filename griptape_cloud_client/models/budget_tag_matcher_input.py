from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetTagMatcherInput")


@_attrs_define
class BudgetTagMatcherInput:
    """One matcher chain as written. `matcher_id` is server-assigned, so it has no place on the way in.

    Attributes:
        value (list[str]): Tag values, leaf first and root last: [B, A] is B under A. Root-anchored, so it matches the
            chains [B, A] and [C, B, A] but not [B, X] — the same leaf under a different parent is a different thing to
            count.
        key (Union[Unset, str]): The tag dimension this chain is matched in. Defaults to `project`.
    """

    value: list[str]
    key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = cast(list[str], d.pop("value"))

        key = d.pop("key", UNSET)

        budget_tag_matcher_input = cls(
            value=value,
            key=key,
        )

        budget_tag_matcher_input.additional_properties = d
        return budget_tag_matcher_input

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
