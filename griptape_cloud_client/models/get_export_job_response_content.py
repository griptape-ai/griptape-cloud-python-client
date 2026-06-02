import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.export_job_status import ExportJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="GetExportJobResponseContent")


@_attrs_define
class GetExportJobResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        export_job_id (str):
        organization_id (str):
        status (ExportJobStatus):
        updated_at (datetime.datetime):
        completed_at (Union[None, Unset, datetime.datetime]):
        data_lake_asset_path (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
        status_detail (Union[Unset, str]):
    """

    created_at: datetime.datetime
    created_by: str
    export_job_id: str
    organization_id: str
    status: ExportJobStatus
    updated_at: datetime.datetime
    completed_at: Union[None, Unset, datetime.datetime] = UNSET
    data_lake_asset_path: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    status_detail: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        export_job_id = self.export_job_id

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

        data_lake_asset_path = self.data_lake_asset_path

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        status_detail = self.status_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "export_job_id": export_job_id,
                "organization_id": organization_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if data_lake_asset_path is not UNSET:
            field_dict["data_lake_asset_path"] = data_lake_asset_path
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        export_job_id = d.pop("export_job_id")

        organization_id = d.pop("organization_id")

        status = ExportJobStatus(d.pop("status"))

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

        data_lake_asset_path = d.pop("data_lake_asset_path", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        status_detail = d.pop("status_detail", UNSET)

        get_export_job_response_content = cls(
            created_at=created_at,
            created_by=created_by,
            export_job_id=export_job_id,
            organization_id=organization_id,
            status=status,
            updated_at=updated_at,
            completed_at=completed_at,
            data_lake_asset_path=data_lake_asset_path,
            metadata=metadata,
            status_detail=status_detail,
        )

        get_export_job_response_content.additional_properties = d
        return get_export_job_response_content

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
