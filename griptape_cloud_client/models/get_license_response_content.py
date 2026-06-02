import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.license_status import LicenseStatus
from ..models.license_type import LicenseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="GetLicenseResponseContent")


@_attrs_define
class GetLicenseResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        license_id (str):
        license_type (LicenseType):
        name (str):
        organization_id (str):
        status (LicenseStatus):
        token_version (float):
        updated_at (datetime.datetime):
        effective_entitlement_policy_ids (Union[Unset, list[str]]):
        entitlement_policy_ids (Union[Unset, list[str]]):
        license_group_ids (Union[Unset, list[str]]):
        metadata (Union[Unset, Metadata]):
        user_id (Union[Unset, str]):
    """

    created_at: datetime.datetime
    expires_at: datetime.datetime
    license_id: str
    license_type: LicenseType
    name: str
    organization_id: str
    status: LicenseStatus
    token_version: float
    updated_at: datetime.datetime
    effective_entitlement_policy_ids: Union[Unset, list[str]] = UNSET
    entitlement_policy_ids: Union[Unset, list[str]] = UNSET
    license_group_ids: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        license_id = self.license_id

        license_type = self.license_type.value

        name = self.name

        organization_id = self.organization_id

        status = self.status.value

        token_version = self.token_version

        updated_at = self.updated_at.isoformat()

        effective_entitlement_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.effective_entitlement_policy_ids, Unset):
            effective_entitlement_policy_ids = self.effective_entitlement_policy_ids

        entitlement_policy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.entitlement_policy_ids, Unset):
            entitlement_policy_ids = self.entitlement_policy_ids

        license_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.license_group_ids, Unset):
            license_group_ids = self.license_group_ids

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "expires_at": expires_at,
                "license_id": license_id,
                "license_type": license_type,
                "name": name,
                "organization_id": organization_id,
                "status": status,
                "token_version": token_version,
                "updated_at": updated_at,
            }
        )
        if effective_entitlement_policy_ids is not UNSET:
            field_dict["effective_entitlement_policy_ids"] = effective_entitlement_policy_ids
        if entitlement_policy_ids is not UNSET:
            field_dict["entitlement_policy_ids"] = entitlement_policy_ids
        if license_group_ids is not UNSET:
            field_dict["license_group_ids"] = license_group_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        expires_at = isoparse(d.pop("expires_at"))

        license_id = d.pop("license_id")

        license_type = LicenseType(d.pop("license_type"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        status = LicenseStatus(d.pop("status"))

        token_version = d.pop("token_version")

        updated_at = isoparse(d.pop("updated_at"))

        effective_entitlement_policy_ids = cast(list[str], d.pop("effective_entitlement_policy_ids", UNSET))

        entitlement_policy_ids = cast(list[str], d.pop("entitlement_policy_ids", UNSET))

        license_group_ids = cast(list[str], d.pop("license_group_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        user_id = d.pop("user_id", UNSET)

        get_license_response_content = cls(
            created_at=created_at,
            expires_at=expires_at,
            license_id=license_id,
            license_type=license_type,
            name=name,
            organization_id=organization_id,
            status=status,
            token_version=token_version,
            updated_at=updated_at,
            effective_entitlement_policy_ids=effective_entitlement_policy_ids,
            entitlement_policy_ids=entitlement_policy_ids,
            license_group_ids=license_group_ids,
            metadata=metadata,
            user_id=user_id,
        )

        get_license_response_content.additional_properties = d
        return get_license_response_content

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
