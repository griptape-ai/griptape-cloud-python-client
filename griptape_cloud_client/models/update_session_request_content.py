from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.session_status import SessionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSessionRequestContent")


@_attrs_define
class UpdateSessionRequestContent:
    """
    Attributes:
        grace_period (Union[Unset, float]): Grace period in seconds applied when transitioning to RELEASED.
            Ignored if status is not RELEASED. Max 900 (15 minutes).
        status (Union[Unset, SessionStatus]):
    """

    grace_period: Union[Unset, float] = UNSET
    status: Union[Unset, SessionStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grace_period = self.grace_period

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grace_period is not UNSET:
            field_dict["grace_period"] = grace_period
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grace_period = d.pop("grace_period", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SessionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SessionStatus(_status)

        update_session_request_content = cls(
            grace_period=grace_period,
            status=status,
        )

        update_session_request_content.additional_properties = d
        return update_session_request_content

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
