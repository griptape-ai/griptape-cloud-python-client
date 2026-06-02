from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateImportJobRequestContent")


@_attrs_define
class CreateImportJobRequestContent:
    """
    Attributes:
        import_type (str):
        data_lake_asset_path (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
        resource_suffix (Union[Unset, str]):
    """

    import_type: str
    data_lake_asset_path: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    resource_suffix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_type = self.import_type

        data_lake_asset_path = self.data_lake_asset_path

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        resource_suffix = self.resource_suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import_type": import_type,
            }
        )
        if data_lake_asset_path is not UNSET:
            field_dict["data_lake_asset_path"] = data_lake_asset_path
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if resource_suffix is not UNSET:
            field_dict["resource_suffix"] = resource_suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        import_type = d.pop("import_type")

        data_lake_asset_path = d.pop("data_lake_asset_path", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        resource_suffix = d.pop("resource_suffix", UNSET)

        create_import_job_request_content = cls(
            import_type=import_type,
            data_lake_asset_path=data_lake_asset_path,
            metadata=metadata,
            resource_suffix=resource_suffix,
        )

        create_import_job_request_content.additional_properties = d
        return create_import_job_request_content

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
