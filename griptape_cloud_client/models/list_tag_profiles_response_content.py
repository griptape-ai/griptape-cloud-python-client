from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.tag_profile_detail import TagProfileDetail


T = TypeVar("T", bound="ListTagProfilesResponseContent")


@_attrs_define
class ListTagProfilesResponseContent:
    """
    Attributes:
        pagination (Pagination):
        tag_profiles (list['TagProfileDetail']):
    """

    pagination: "Pagination"
    tag_profiles: list["TagProfileDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        tag_profiles = []
        for tag_profiles_item_data in self.tag_profiles:
            tag_profiles_item = tag_profiles_item_data.to_dict()
            tag_profiles.append(tag_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "tag_profiles": tag_profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.tag_profile_detail import TagProfileDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        tag_profiles = []
        _tag_profiles = d.pop("tag_profiles")
        for tag_profiles_item_data in _tag_profiles:
            tag_profiles_item = TagProfileDetail.from_dict(tag_profiles_item_data)

            tag_profiles.append(tag_profiles_item)

        list_tag_profiles_response_content = cls(
            pagination=pagination,
            tag_profiles=tag_profiles,
        )

        list_tag_profiles_response_content.additional_properties = d
        return list_tag_profiles_response_content

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
