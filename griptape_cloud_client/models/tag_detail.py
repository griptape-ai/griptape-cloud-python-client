import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.spend_totals import SpendTotals
    from ..models.tag_matched_budget import TagMatchedBudget
    from ..models.tag_value_profile import TagValueProfile


T = TypeVar("T", bound="TagDetail")


@_attrs_define
class TagDetail:
    """
    Attributes:
        distinct_engine_ids (float): Distinct engines that reported this exact value. Per value, not per entry: a leaf
            reported under two parents is two values.
        first_seen (datetime.datetime):
        is_default (bool): The value spend resolves to when it carried no usable attribution. Never matched by a budget
            and never profiled; its spend is what the default budget absorbs.
        key (str):
        last_seen (datetime.datetime):
        matched (list['TagMatchedBudget']): Enabled budgets covering this tag. Empty means the default budget absorbs
            its spend.
        other_values (list[list[str]]): Other values for this key that report one of this value's entries under a
            different ancestry, which splits any budget matching through that entry. At most ten.
        profiles (list['TagValueProfile']): Parallel to `value`: entry i describes value[i].
        spend_count (float):
        totals (SpendTotals): Subtotals per funding source.
        value (list[str]): A tag's value. A list is ordered leaf first and root last, so [B, A] is B under A; a single
            string is a one-entry list.
    """

    distinct_engine_ids: float
    first_seen: datetime.datetime
    is_default: bool
    key: str
    last_seen: datetime.datetime
    matched: list["TagMatchedBudget"]
    other_values: list[list[str]]
    profiles: list["TagValueProfile"]
    spend_count: float
    totals: "SpendTotals"
    value: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distinct_engine_ids = self.distinct_engine_ids

        first_seen = self.first_seen.isoformat()

        is_default = self.is_default

        key = self.key

        last_seen = self.last_seen.isoformat()

        matched = []
        for matched_item_data in self.matched:
            matched_item = matched_item_data.to_dict()
            matched.append(matched_item)

        other_values = []
        for other_values_item_data in self.other_values:
            other_values_item = other_values_item_data

            other_values.append(other_values_item)

        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)

        spend_count = self.spend_count

        totals = self.totals.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "distinct_engine_ids": distinct_engine_ids,
                "first_seen": first_seen,
                "is_default": is_default,
                "key": key,
                "last_seen": last_seen,
                "matched": matched,
                "other_values": other_values,
                "profiles": profiles,
                "spend_count": spend_count,
                "totals": totals,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_totals import SpendTotals
        from ..models.tag_matched_budget import TagMatchedBudget
        from ..models.tag_value_profile import TagValueProfile

        d = dict(src_dict)
        distinct_engine_ids = d.pop("distinct_engine_ids")

        first_seen = isoparse(d.pop("first_seen"))

        is_default = d.pop("is_default")

        key = d.pop("key")

        last_seen = isoparse(d.pop("last_seen"))

        matched = []
        _matched = d.pop("matched")
        for matched_item_data in _matched:
            matched_item = TagMatchedBudget.from_dict(matched_item_data)

            matched.append(matched_item)

        other_values = []
        _other_values = d.pop("other_values")
        for other_values_item_data in _other_values:
            other_values_item = cast(list[str], other_values_item_data)

            other_values.append(other_values_item)

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = TagValueProfile.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        spend_count = d.pop("spend_count")

        totals = SpendTotals.from_dict(d.pop("totals"))

        value = cast(list[str], d.pop("value"))

        tag_detail = cls(
            distinct_engine_ids=distinct_engine_ids,
            first_seen=first_seen,
            is_default=is_default,
            key=key,
            last_seen=last_seen,
            matched=matched,
            other_values=other_values,
            profiles=profiles,
            spend_count=spend_count,
            totals=totals,
            value=value,
        )

        tag_detail.additional_properties = d
        return tag_detail

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
