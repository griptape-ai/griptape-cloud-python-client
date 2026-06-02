from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.license_status import LicenseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="UpdateLicenseRequestContent")


@_attrs_define
class UpdateLicenseRequestContent:
    """
    Attributes:
        entitlement_policy_ids (Union[Unset, list[str]]):
        metadata (Union[Unset, Metadata]):
        name (Union[Unset, str]):
        status (Union[Unset, LicenseStatus]):
    """

    entitlement_policy_ids: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, LicenseStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entitlement_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.entitlement_policy_ids, Unset):
            entitlement_policy_ids = self.entitlement_policy_ids

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entitlement_policy_ids is not UNSET:
            field_dict["entitlement_policy_ids"] = entitlement_policy_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        entitlement_policy_ids = cast(list[str], d.pop("entitlement_policy_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LicenseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LicenseStatus(_status)

        update_license_request_content = cls(
            entitlement_policy_ids=entitlement_policy_ids,
            metadata=metadata,
            name=name,
            status=status,
        )

        update_license_request_content.additional_properties = d
        return update_license_request_content

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
