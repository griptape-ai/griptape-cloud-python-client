from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagValueProfile")


@_attrs_define
class TagValueProfile:
    """One entry of a tag's value, with the profile describing it if there is one.

    Attributes:
        value (str):
        display_name (Union[Unset, str]): Null when no profile describes this value or it names none.
        tag_profile_id (Union[Unset, str]): Null when no profile describes this value.
    """

    value: str
    display_name: Union[Unset, str] = UNSET
    tag_profile_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        display_name = self.display_name

        tag_profile_id = self.tag_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if tag_profile_id is not UNSET:
            field_dict["tag_profile_id"] = tag_profile_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        display_name = d.pop("display_name", UNSET)

        tag_profile_id = d.pop("tag_profile_id", UNSET)

        tag_value_profile = cls(
            value=value,
            display_name=display_name,
            tag_profile_id=tag_profile_id,
        )

        tag_value_profile.additional_properties = d
        return tag_value_profile

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
