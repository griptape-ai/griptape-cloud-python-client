import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthConfigDetail")


@_attrs_define
class AuthConfigDetail:
    """
    Attributes:
        api_key_secret_id (str):
        auth_config_id (str):
        base_url (str):
        created_at (datetime.datetime):
        name (str):
        updated_at (datetime.datetime):
        kwargs (Union[Unset, Any]):
    """

    api_key_secret_id: str
    auth_config_id: str
    base_url: str
    created_at: datetime.datetime
    name: str
    updated_at: datetime.datetime
    kwargs: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_secret_id = self.api_key_secret_id

        auth_config_id = self.auth_config_id

        base_url = self.base_url

        created_at = self.created_at.isoformat()

        name = self.name

        updated_at = self.updated_at.isoformat()

        kwargs = self.kwargs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key_secret_id": api_key_secret_id,
                "auth_config_id": auth_config_id,
                "base_url": base_url,
                "created_at": created_at,
                "name": name,
                "updated_at": updated_at,
            }
        )
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_secret_id = d.pop("api_key_secret_id")

        auth_config_id = d.pop("auth_config_id")

        base_url = d.pop("base_url")

        created_at = isoparse(d.pop("created_at"))

        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        kwargs = d.pop("kwargs", UNSET)

        auth_config_detail = cls(
            api_key_secret_id=api_key_secret_id,
            auth_config_id=auth_config_id,
            base_url=base_url,
            created_at=created_at,
            name=name,
            updated_at=updated_at,
            kwargs=kwargs,
        )

        auth_config_detail.additional_properties = d
        return auth_config_detail

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
