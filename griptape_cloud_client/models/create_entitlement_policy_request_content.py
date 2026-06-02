from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateEntitlementPolicyRequestContent")


@_attrs_define
class CreateEntitlementPolicyRequestContent:
    """
    Attributes:
        name (str):
        policy_document (Any):
        description (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
    """

    name: str
    policy_document: Any
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        policy_document = self.policy_document

        description = self.description

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "policy_document": policy_document,
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
        name = d.pop("name")

        policy_document = d.pop("policy_document")

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        create_entitlement_policy_request_content = cls(
            name=name,
            policy_document=policy_document,
            description=description,
            metadata=metadata,
        )

        create_entitlement_policy_request_content.additional_properties = d
        return create_entitlement_policy_request_content

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
