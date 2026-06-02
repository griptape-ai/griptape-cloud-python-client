import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.session_status import SessionStatus

T = TypeVar("T", bound="SessionDetail")


@_attrs_define
class SessionDetail:
    """
    Attributes:
        application_id (str):
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        license_id (str):
        organization_id (str):
        session_id (str):
        status (SessionStatus):
        updated_at (datetime.datetime):
    """

    application_id: str
    created_at: datetime.datetime
    expires_at: datetime.datetime
    license_id: str
    organization_id: str
    session_id: str
    status: SessionStatus
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        license_id = self.license_id

        organization_id = self.organization_id

        session_id = self.session_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application_id": application_id,
                "created_at": created_at,
                "expires_at": expires_at,
                "license_id": license_id,
                "organization_id": organization_id,
                "session_id": session_id,
                "status": status,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_id = d.pop("application_id")

        created_at = isoparse(d.pop("created_at"))

        expires_at = isoparse(d.pop("expires_at"))

        license_id = d.pop("license_id")

        organization_id = d.pop("organization_id")

        session_id = d.pop("session_id")

        status = SessionStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        session_detail = cls(
            application_id=application_id,
            created_at=created_at,
            expires_at=expires_at,
            license_id=license_id,
            organization_id=organization_id,
            session_id=session_id,
            status=status,
            updated_at=updated_at,
        )

        session_detail.additional_properties = d
        return session_detail

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
