from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.spend_export_tag_key import SpendExportTagKey


T = TypeVar("T", bound="ListSpendExportTagKeysResponseContent")


@_attrs_define
class ListSpendExportTagKeysResponseContent:
    """
    Attributes:
        tag_keys (list['SpendExportTagKey']):
    """

    tag_keys: list["SpendExportTagKey"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_keys = []
        for tag_keys_item_data in self.tag_keys:
            tag_keys_item = tag_keys_item_data.to_dict()
            tag_keys.append(tag_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_keys": tag_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_export_tag_key import SpendExportTagKey

        d = dict(src_dict)
        tag_keys = []
        _tag_keys = d.pop("tag_keys")
        for tag_keys_item_data in _tag_keys:
            tag_keys_item = SpendExportTagKey.from_dict(tag_keys_item_data)

            tag_keys.append(tag_keys_item)

        list_spend_export_tag_keys_response_content = cls(
            tag_keys=tag_keys,
        )

        list_spend_export_tag_keys_response_content.additional_properties = d
        return list_spend_export_tag_keys_response_content

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
