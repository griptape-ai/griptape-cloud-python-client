from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="UpdateEntitlementPolicyRequestContent")


@_attrs_define
class UpdateEntitlementPolicyRequestContent:
    """
    Attributes:
        description (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
        name (Union[Unset, str]):
        policy_document (Union[Unset, Any]):
    """

    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    name: Union[Unset, str] = UNSET
    policy_document: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        policy_document = self.policy_document

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if policy_document is not UNSET:
            field_dict["policy_document"] = policy_document

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        policy_document = d.pop("policy_document", UNSET)

        update_entitlement_policy_request_content = cls(
            description=description,
            metadata=metadata,
            name=name,
            policy_document=policy_document,
        )

        update_entitlement_policy_request_content.additional_properties = d
        return update_entitlement_policy_request_content

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
