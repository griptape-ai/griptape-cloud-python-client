import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="LicenseGroupDetail")


@_attrs_define
class LicenseGroupDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        license_group_id (str):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
        entitlement_policy_ids (Union[Unset, list[str]]):
        license_ids (Union[Unset, list[str]]):
        metadata (Union[Unset, Metadata]):
    """

    created_at: datetime.datetime
    license_group_id: str
    name: str
    organization_id: str
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    entitlement_policy_ids: Union[Unset, list[str]] = UNSET
    license_ids: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        license_group_id = self.license_group_id

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        description = self.description

        entitlement_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.entitlement_policy_ids, Unset):
            entitlement_policy_ids = self.entitlement_policy_ids

        license_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.license_ids, Unset):
            license_ids = self.license_ids

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "license_group_id": license_group_id,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entitlement_policy_ids is not UNSET:
            field_dict["entitlement_policy_ids"] = entitlement_policy_ids
        if license_ids is not UNSET:
            field_dict["license_ids"] = license_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        license_group_id = d.pop("license_group_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        entitlement_policy_ids = cast(list[str], d.pop("entitlement_policy_ids", UNSET))

        license_ids = cast(list[str], d.pop("license_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        license_group_detail = cls(
            created_at=created_at,
            license_group_id=license_group_id,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            description=description,
            entitlement_policy_ids=entitlement_policy_ids,
            license_ids=license_ids,
            metadata=metadata,
        )

        license_group_detail.additional_properties = d
        return license_group_detail

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
