from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.license_detail import LicenseDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListLicensesResponseContent")


@_attrs_define
class ListLicensesResponseContent:
    """
    Attributes:
        licenses (list['LicenseDetail']):
        pagination (Pagination):
    """

    licenses: list["LicenseDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()
            licenses.append(licenses_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "licenses": licenses,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_detail import LicenseDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        licenses = []
        _licenses = d.pop("licenses")
        for licenses_item_data in _licenses:
            licenses_item = LicenseDetail.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_licenses_response_content = cls(
            licenses=licenses,
            pagination=pagination,
        )

        list_licenses_response_content.additional_properties = d
        return list_licenses_response_content

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
