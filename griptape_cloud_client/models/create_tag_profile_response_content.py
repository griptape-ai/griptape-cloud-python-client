import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateTagProfileResponseContent")


@_attrs_define
class CreateTagProfileResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        key (str):
        metadata (Metadata):
        organization_id (str):
        tag_profile_id (str):
        updated_at (datetime.datetime):
        value (str):
        display_name (Union[Unset, str]):
        updated_by_id (Union[Unset, str]):
    """

    created_at: datetime.datetime
    key: str
    metadata: "Metadata"
    organization_id: str
    tag_profile_id: str
    updated_at: datetime.datetime
    value: str
    display_name: Union[Unset, str] = UNSET
    updated_by_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        key = self.key

        metadata = self.metadata.to_dict()

        organization_id = self.organization_id

        tag_profile_id = self.tag_profile_id

        updated_at = self.updated_at.isoformat()

        value = self.value

        display_name = self.display_name

        updated_by_id = self.updated_by_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "key": key,
                "metadata": metadata,
                "organization_id": organization_id,
                "tag_profile_id": tag_profile_id,
                "updated_at": updated_at,
                "value": value,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if updated_by_id is not UNSET:
            field_dict["updated_by_id"] = updated_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        key = d.pop("key")

        metadata = Metadata.from_dict(d.pop("metadata"))

        organization_id = d.pop("organization_id")

        tag_profile_id = d.pop("tag_profile_id")

        updated_at = isoparse(d.pop("updated_at"))

        value = d.pop("value")

        display_name = d.pop("display_name", UNSET)

        updated_by_id = d.pop("updated_by_id", UNSET)

        create_tag_profile_response_content = cls(
            created_at=created_at,
            key=key,
            metadata=metadata,
            organization_id=organization_id,
            tag_profile_id=tag_profile_id,
            updated_at=updated_at,
            value=value,
            display_name=display_name,
            updated_by_id=updated_by_id,
        )

        create_tag_profile_response_content.additional_properties = d
        return create_tag_profile_response_content

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
