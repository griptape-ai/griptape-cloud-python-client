from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.license_group_detail import LicenseGroupDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListLicenseGroupsResponseContent")


@_attrs_define
class ListLicenseGroupsResponseContent:
    """
    Attributes:
        license_groups (list['LicenseGroupDetail']):
        pagination (Pagination):
    """

    license_groups: list["LicenseGroupDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_groups = []
        for license_groups_item_data in self.license_groups:
            license_groups_item = license_groups_item_data.to_dict()
            license_groups.append(license_groups_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "license_groups": license_groups,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_group_detail import LicenseGroupDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        license_groups = []
        _license_groups = d.pop("license_groups")
        for license_groups_item_data in _license_groups:
            license_groups_item = LicenseGroupDetail.from_dict(license_groups_item_data)

            license_groups.append(license_groups_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_license_groups_response_content = cls(
            license_groups=license_groups,
            pagination=pagination,
        )

        list_license_groups_response_content.additional_properties = d
        return list_license_groups_response_content

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
