from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.session_detail import SessionDetail


T = TypeVar("T", bound="ListSessionsResponseContent")


@_attrs_define
class ListSessionsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        sessions (list['SessionDetail']):
    """

    pagination: "Pagination"
    sessions: list["SessionDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        sessions = []
        for sessions_item_data in self.sessions:
            sessions_item = sessions_item_data.to_dict()
            sessions.append(sessions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "sessions": sessions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.session_detail import SessionDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        sessions = []
        _sessions = d.pop("sessions")
        for sessions_item_data in _sessions:
            sessions_item = SessionDetail.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        list_sessions_response_content = cls(
            pagination=pagination,
            sessions=sessions,
        )

        list_sessions_response_content.additional_properties = d
        return list_sessions_response_content

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
