from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_job_detail import ImportJobDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListImportJobsResponseContent")


@_attrs_define
class ListImportJobsResponseContent:
    """
    Attributes:
        import_jobs (list['ImportJobDetail']):
        pagination (Pagination):
    """

    import_jobs: list["ImportJobDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_jobs = []
        for import_jobs_item_data in self.import_jobs:
            import_jobs_item = import_jobs_item_data.to_dict()
            import_jobs.append(import_jobs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import_jobs": import_jobs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_job_detail import ImportJobDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        import_jobs = []
        _import_jobs = d.pop("import_jobs")
        for import_jobs_item_data in _import_jobs:
            import_jobs_item = ImportJobDetail.from_dict(import_jobs_item_data)

            import_jobs.append(import_jobs_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_import_jobs_response_content = cls(
            import_jobs=import_jobs,
            pagination=pagination,
        )

        list_import_jobs_response_content.additional_properties = d
        return list_import_jobs_response_content

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
