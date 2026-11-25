import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.license_type import LicenseType

T = TypeVar("T", bound="GetLicenseInfoResponseContent")


@_attrs_define
class GetLicenseInfoResponseContent:
    """
    Attributes:
        expires_at (datetime.datetime):
        license_id (str):
        license_type (LicenseType):
        name (str):
        organization_id (str):
    """

    expires_at: datetime.datetime
    license_id: str
    license_type: LicenseType
    name: str
    organization_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        license_id = self.license_id

        license_type = self.license_type.value

        name = self.name

        organization_id = self.organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_at": expires_at,
                "license_id": license_id,
                "license_type": license_type,
                "name": name,
                "organization_id": organization_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = isoparse(d.pop("expires_at"))

        license_id = d.pop("license_id")

        license_type = LicenseType(d.pop("license_type"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        get_license_info_response_content = cls(
            expires_at=expires_at,
            license_id=license_id,
            license_type=license_type,
            name=name,
            organization_id=organization_id,
        )

        get_license_info_response_content.additional_properties = d
        return get_license_info_response_content

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
