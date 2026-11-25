import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="ManagedPolicyDetail")


@_attrs_define
class ManagedPolicyDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        managed_policy_id (str):
        name (str):
        policy_document (Any):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
        organization_id (Union[Unset, str]):
    """

    created_at: datetime.datetime
    managed_policy_id: str
    name: str
    policy_document: Any
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        managed_policy_id = self.managed_policy_id

        name = self.name

        policy_document = self.policy_document

        updated_at = self.updated_at.isoformat()

        description = self.description

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        organization_id = self.organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "managed_policy_id": managed_policy_id,
                "name": name,
                "policy_document": policy_document,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        managed_policy_id = d.pop("managed_policy_id")

        name = d.pop("name")

        policy_document = d.pop("policy_document")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        organization_id = d.pop("organization_id", UNSET)

        managed_policy_detail = cls(
            created_at=created_at,
            managed_policy_id=managed_policy_id,
            name=name,
            policy_document=policy_document,
            updated_at=updated_at,
            description=description,
            metadata=metadata,
            organization_id=organization_id,
        )

        managed_policy_detail.additional_properties = d
        return managed_policy_detail

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
