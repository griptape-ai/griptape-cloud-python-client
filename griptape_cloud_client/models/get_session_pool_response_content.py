import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetSessionPoolResponseContent")


@_attrs_define
class GetSessionPoolResponseContent:
    """
    Attributes:
        active_count (float):
        created_at (datetime.datetime):
        organization_id (str):
        session_pool_id (str):
        total_sessions (float):
        updated_at (datetime.datetime):
    """

    active_count: float
    created_at: datetime.datetime
    organization_id: str
    session_pool_id: str
    total_sessions: float
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_count = self.active_count

        created_at = self.created_at.isoformat()

        organization_id = self.organization_id

        session_pool_id = self.session_pool_id

        total_sessions = self.total_sessions

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_count": active_count,
                "created_at": created_at,
                "organization_id": organization_id,
                "session_pool_id": session_pool_id,
                "total_sessions": total_sessions,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_count = d.pop("active_count")

        created_at = isoparse(d.pop("created_at"))

        organization_id = d.pop("organization_id")

        session_pool_id = d.pop("session_pool_id")

        total_sessions = d.pop("total_sessions")

        updated_at = isoparse(d.pop("updated_at"))

        get_session_pool_response_content = cls(
            active_count=active_count,
            created_at=created_at,
            organization_id=organization_id,
            session_pool_id=session_pool_id,
            total_sessions=total_sessions,
            updated_at=updated_at,
        )

        get_session_pool_response_content.additional_properties = d
        return get_session_pool_response_content

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
