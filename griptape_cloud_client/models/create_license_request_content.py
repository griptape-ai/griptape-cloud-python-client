import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.license_type import LicenseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateLicenseRequestContent")


@_attrs_define
class CreateLicenseRequestContent:
    """
    Attributes:
        expires_at (datetime.datetime):
        license_type (LicenseType):
        name (str):
        entitlement_policy_ids (Union[Unset, list[str]]):
        metadata (Union[Unset, Metadata]):
        user_id (Union[Unset, str]):
    """

    expires_at: datetime.datetime
    license_type: LicenseType
    name: str
    entitlement_policy_ids: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        license_type = self.license_type.value

        name = self.name

        entitlement_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.entitlement_policy_ids, Unset):
            entitlement_policy_ids = self.entitlement_policy_ids

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_at": expires_at,
                "license_type": license_type,
                "name": name,
            }
        )
        if entitlement_policy_ids is not UNSET:
            field_dict["entitlement_policy_ids"] = entitlement_policy_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        expires_at = isoparse(d.pop("expires_at"))

        license_type = LicenseType(d.pop("license_type"))

        name = d.pop("name")

        entitlement_policy_ids = cast(list[str], d.pop("entitlement_policy_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        user_id = d.pop("user_id", UNSET)

        create_license_request_content = cls(
            expires_at=expires_at,
            license_type=license_type,
            name=name,
            entitlement_policy_ids=entitlement_policy_ids,
            metadata=metadata,
            user_id=user_id,
        )

        create_license_request_content.additional_properties = d
        return create_license_request_content

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
