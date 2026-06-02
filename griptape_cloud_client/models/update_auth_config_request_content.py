from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAuthConfigRequestContent")


@_attrs_define
class UpdateAuthConfigRequestContent:
    """
    Attributes:
        api_key_secret_id (Union[Unset, str]):
        base_url (Union[Unset, str]):
        kwargs (Union[Unset, Any]):
        name (Union[Unset, str]):
    """

    api_key_secret_id: Union[Unset, str] = UNSET
    base_url: Union[Unset, str] = UNSET
    kwargs: Union[Unset, Any] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_secret_id = self.api_key_secret_id

        base_url = self.base_url

        kwargs = self.kwargs

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_secret_id is not UNSET:
            field_dict["api_key_secret_id"] = api_key_secret_id
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_secret_id = d.pop("api_key_secret_id", UNSET)

        base_url = d.pop("base_url", UNSET)

        kwargs = d.pop("kwargs", UNSET)

        name = d.pop("name", UNSET)

        update_auth_config_request_content = cls(
            api_key_secret_id=api_key_secret_id,
            base_url=base_url,
            kwargs=kwargs,
            name=name,
        )

        update_auth_config_request_content.additional_properties = d
        return update_auth_config_request_content

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
