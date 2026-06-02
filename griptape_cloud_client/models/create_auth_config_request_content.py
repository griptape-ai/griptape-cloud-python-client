from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAuthConfigRequestContent")


@_attrs_define
class CreateAuthConfigRequestContent:
    """
    Attributes:
        api_key_secret_id (str):
        base_url (str):
        name (str):
        kwargs (Union[Unset, Any]):
    """

    api_key_secret_id: str
    base_url: str
    name: str
    kwargs: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_secret_id = self.api_key_secret_id

        base_url = self.base_url

        name = self.name

        kwargs = self.kwargs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key_secret_id": api_key_secret_id,
                "base_url": base_url,
                "name": name,
            }
        )
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_secret_id = d.pop("api_key_secret_id")

        base_url = d.pop("base_url")

        name = d.pop("name")

        kwargs = d.pop("kwargs", UNSET)

        create_auth_config_request_content = cls(
            api_key_secret_id=api_key_secret_id,
            base_url=base_url,
            name=name,
            kwargs=kwargs,
        )

        create_auth_config_request_content.additional_properties = d
        return create_auth_config_request_content

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
