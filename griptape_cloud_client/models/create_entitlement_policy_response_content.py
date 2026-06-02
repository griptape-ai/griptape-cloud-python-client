import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateEntitlementPolicyResponseContent")


@_attrs_define
class CreateEntitlementPolicyResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        entitlement_policy_id (str):
        name (str):
        organization_id (str):
        policy_document (Any):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
    """

    created_at: datetime.datetime
    entitlement_policy_id: str
    name: str
    organization_id: str
    policy_document: Any
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        entitlement_policy_id = self.entitlement_policy_id

        name = self.name

        organization_id = self.organization_id

        policy_document = self.policy_document

        updated_at = self.updated_at.isoformat()

        description = self.description

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "entitlement_policy_id": entitlement_policy_id,
                "name": name,
                "organization_id": organization_id,
                "policy_document": policy_document,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        entitlement_policy_id = d.pop("entitlement_policy_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        policy_document = d.pop("policy_document")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        create_entitlement_policy_response_content = cls(
            created_at=created_at,
            entitlement_policy_id=entitlement_policy_id,
            name=name,
            organization_id=organization_id,
            policy_document=policy_document,
            updated_at=updated_at,
            description=description,
            metadata=metadata,
        )

        create_entitlement_policy_response_content.additional_properties = d
        return create_entitlement_policy_response_content

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
