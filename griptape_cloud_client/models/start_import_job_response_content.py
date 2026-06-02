import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.import_job_status import ImportJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="StartImportJobResponseContent")


@_attrs_define
class StartImportJobResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        data_lake_asset_path (str):
        import_job_id (str):
        import_type (str):
        organization_id (str):
        status (ImportJobStatus):
        updated_at (datetime.datetime):
        completed_at (Union[None, Unset, datetime.datetime]):
        import_data (Union[Unset, Any]):
        metadata (Union[Unset, Metadata]):
        resource_suffix (Union[Unset, str]):
        status_detail (Union[Unset, Any]):
    """

    created_at: datetime.datetime
    created_by: str
    data_lake_asset_path: str
    import_job_id: str
    import_type: str
    organization_id: str
    status: ImportJobStatus
    updated_at: datetime.datetime
    completed_at: Union[None, Unset, datetime.datetime] = UNSET
    import_data: Union[Unset, Any] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    resource_suffix: Union[Unset, str] = UNSET
    status_detail: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        data_lake_asset_path = self.data_lake_asset_path

        import_job_id = self.import_job_id

        import_type = self.import_type

        organization_id = self.organization_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        import_data = self.import_data

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        resource_suffix = self.resource_suffix

        status_detail = self.status_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "data_lake_asset_path": data_lake_asset_path,
                "import_job_id": import_job_id,
                "import_type": import_type,
                "organization_id": organization_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if import_data is not UNSET:
            field_dict["import_data"] = import_data
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if resource_suffix is not UNSET:
            field_dict["resource_suffix"] = resource_suffix
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        data_lake_asset_path = d.pop("data_lake_asset_path")

        import_job_id = d.pop("import_job_id")

        import_type = d.pop("import_type")

        organization_id = d.pop("organization_id")

        status = ImportJobStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_completed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        import_data = d.pop("import_data", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        resource_suffix = d.pop("resource_suffix", UNSET)

        status_detail = d.pop("status_detail", UNSET)

        start_import_job_response_content = cls(
            created_at=created_at,
            created_by=created_by,
            data_lake_asset_path=data_lake_asset_path,
            import_job_id=import_job_id,
            import_type=import_type,
            organization_id=organization_id,
            status=status,
            updated_at=updated_at,
            completed_at=completed_at,
            import_data=import_data,
            metadata=metadata,
            resource_suffix=resource_suffix,
            status_detail=status_detail,
        )

        start_import_job_response_content.additional_properties = d
        return start_import_job_response_content

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
