from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="UpdateLicenseGroupRequestContent")


@_attrs_define
class UpdateLicenseGroupRequestContent:
    """
    Attributes:
        description (Union[Unset, str]):
        entitlement_policy_ids (Union[Unset, list[str]]):
        license_ids (Union[Unset, list[str]]):
        metadata (Union[Unset, Metadata]):
        name (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    entitlement_policy_ids: Union[Unset, list[str]] = UNSET
    license_ids: Union[Unset, list[str]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if entitlement_policy_ids is not UNSET:
            field_dict["entitlement_policy_ids"] = entitlement_policy_ids
        if license_ids is not UNSET:
            field_dict["license_ids"] = license_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        entitlement_policy_ids = cast(list[str], d.pop("entitlement_policy_ids", UNSET))

        license_ids = cast(list[str], d.pop("license_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        update_license_group_request_content = cls(
            description=description,
            entitlement_policy_ids=entitlement_policy_ids,
            license_ids=license_ids,
            metadata=metadata,
            name=name,
        )

        update_license_group_request_content.additional_properties = d
        return update_license_group_request_content

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
