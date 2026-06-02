from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.export_job_detail import ExportJobDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListExportJobsResponseContent")


@_attrs_define
class ListExportJobsResponseContent:
    """
    Attributes:
        export_jobs (list['ExportJobDetail']):
        pagination (Pagination):
    """

    export_jobs: list["ExportJobDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_jobs = []
        for export_jobs_item_data in self.export_jobs:
            export_jobs_item = export_jobs_item_data.to_dict()
            export_jobs.append(export_jobs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "export_jobs": export_jobs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_job_detail import ExportJobDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        export_jobs = []
        _export_jobs = d.pop("export_jobs")
        for export_jobs_item_data in _export_jobs:
            export_jobs_item = ExportJobDetail.from_dict(export_jobs_item_data)

            export_jobs.append(export_jobs_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_export_jobs_response_content = cls(
            export_jobs=export_jobs,
            pagination=pagination,
        )

        list_export_jobs_response_content.additional_properties = d
        return list_export_jobs_response_content

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
