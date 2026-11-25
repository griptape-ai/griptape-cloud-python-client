from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendTagFilter")


@_attrs_define
class SpendTagFilter:
    """One tag dimension to filter on, with the modifiers that apply to that dimension.

    Attributes:
        key (str): The tag key to filter on.
        value (list[str]): The value to match: ordered leaf first and root last, so [B, A] is B under A. Matched root-
            anchored, per the operation's description. A bare string is read as a one-entry value, as it is in the
            attribution header.
        rollup (Union[Unset, bool]): Whether this filter counts the spend beneath its value. Absent is true, which is
            total spend: the value plus everything under it. false is direct spend, only work the value's leaf itself was
            attributed to.
    """

    key: str
    value: list[str]
    rollup: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        rollup = self.rollup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if rollup is not UNSET:
            field_dict["rollup"] = rollup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = cast(list[str], d.pop("value"))

        rollup = d.pop("rollup", UNSET)

        spend_tag_filter = cls(
            key=key,
            value=value,
            rollup=rollup,
        )

        spend_tag_filter.additional_properties = d
        return spend_tag_filter

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
