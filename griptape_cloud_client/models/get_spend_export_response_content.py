import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.spend_export_format import SpendExportFormat
from ..models.spend_export_status import SpendExportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSpendExportResponseContent")


@_attrs_define
class GetSpendExportResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        filters (Any): The spend search filters the file covers, as Griptape Cloud applied them.
        format_ (SpendExportFormat):
        includes_emails (bool): Whether the file's `user_email` column is filled: only for an export a signed-in member
            of the organization created. Such a file is a signed-in member's to download, so a license or API key reading it
            gets a null `download_url`.
        organization_id (str):
        spend_export_id (str):
        status (SpendExportStatus):
        updated_at (datetime.datetime):
        byte_count (Union[None, Unset, float]): Size of the file in bytes, once written.
        completed_at (Union[None, Unset, datetime.datetime]):
        download_url (Union[None, Unset, str]): A signed link to the file, valid for 15 minutes and minted on each read
            of this export. Null until the export succeeds, after it expires, and in list responses: read the export to get
            a fresh link.
        expired_at (Union[None, Unset, datetime.datetime]): When the file was deleted. From then on `download_url` is
            null.
        expires_at (Union[None, Unset, datetime.datetime]): When the file is due to be deleted.
        row_count (Union[None, Unset, float]): Rows in the file, once written.
        status_detail (Union[None, Unset, str]): Why the export failed, when it did.
        tag_keys (Union[None, Unset, list[str]]): The tag keys the file has columns for, in order, as requested. Null
            when the request named none, so the file has a column for every tag key on its rows.
    """

    created_at: datetime.datetime
    filters: Any
    format_: SpendExportFormat
    includes_emails: bool
    organization_id: str
    spend_export_id: str
    status: SpendExportStatus
    updated_at: datetime.datetime
    byte_count: Union[None, Unset, float] = UNSET
    completed_at: Union[None, Unset, datetime.datetime] = UNSET
    download_url: Union[None, Unset, str] = UNSET
    expired_at: Union[None, Unset, datetime.datetime] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    row_count: Union[None, Unset, float] = UNSET
    status_detail: Union[None, Unset, str] = UNSET
    tag_keys: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        filters = self.filters

        format_ = self.format_.value

        includes_emails = self.includes_emails

        organization_id = self.organization_id

        spend_export_id = self.spend_export_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        byte_count: Union[None, Unset, float]
        if isinstance(self.byte_count, Unset):
            byte_count = UNSET
        else:
            byte_count = self.byte_count

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        download_url: Union[None, Unset, str]
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url

        expired_at: Union[None, Unset, str]
        if isinstance(self.expired_at, Unset):
            expired_at = UNSET
        elif isinstance(self.expired_at, datetime.datetime):
            expired_at = self.expired_at.isoformat()
        else:
            expired_at = self.expired_at

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        row_count: Union[None, Unset, float]
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        status_detail: Union[None, Unset, str]
        if isinstance(self.status_detail, Unset):
            status_detail = UNSET
        else:
            status_detail = self.status_detail

        tag_keys: Union[None, Unset, list[str]]
        if isinstance(self.tag_keys, Unset):
            tag_keys = UNSET
        elif isinstance(self.tag_keys, list):
            tag_keys = self.tag_keys

        else:
            tag_keys = self.tag_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "filters": filters,
                "format": format_,
                "includes_emails": includes_emails,
                "organization_id": organization_id,
                "spend_export_id": spend_export_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if byte_count is not UNSET:
            field_dict["byte_count"] = byte_count
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if expired_at is not UNSET:
            field_dict["expired_at"] = expired_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail
        if tag_keys is not UNSET:
            field_dict["tag_keys"] = tag_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        filters = d.pop("filters")

        format_ = SpendExportFormat(d.pop("format"))

        includes_emails = d.pop("includes_emails")

        organization_id = d.pop("organization_id")

        spend_export_id = d.pop("spend_export_id")

        status = SpendExportStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_byte_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        byte_count = _parse_byte_count(d.pop("byte_count", UNSET))

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

        def _parse_download_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_url = _parse_download_url(d.pop("download_url", UNSET))

        def _parse_expired_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expired_at_type_0 = isoparse(data)

                return expired_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expired_at = _parse_expired_at(d.pop("expired_at", UNSET))

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_row_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        def _parse_status_detail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_detail = _parse_status_detail(d.pop("status_detail", UNSET))

        def _parse_tag_keys(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tag_keys_type_0 = cast(list[str], data)

                return tag_keys_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tag_keys = _parse_tag_keys(d.pop("tag_keys", UNSET))

        get_spend_export_response_content = cls(
            created_at=created_at,
            filters=filters,
            format_=format_,
            includes_emails=includes_emails,
            organization_id=organization_id,
            spend_export_id=spend_export_id,
            status=status,
            updated_at=updated_at,
            byte_count=byte_count,
            completed_at=completed_at,
            download_url=download_url,
            expired_at=expired_at,
            expires_at=expires_at,
            row_count=row_count,
            status_detail=status_detail,
            tag_keys=tag_keys,
        )

        get_spend_export_response_content.additional_properties = d
        return get_spend_export_response_content

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
