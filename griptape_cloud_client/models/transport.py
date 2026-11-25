from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Transport")


@_attrs_define
class Transport:
    """
    Attributes:
        kind (str):
        bind_host (Union[Unset, str]):
        port (Union[Unset, float]):
        status (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    kind: str
    bind_host: Union[Unset, str] = UNSET
    port: Union[Unset, float] = UNSET
    status: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        bind_host = self.bind_host

        port = self.port

        status = self.status

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if bind_host is not UNSET:
            field_dict["bind_host"] = bind_host
        if port is not UNSET:
            field_dict["port"] = port
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        bind_host = d.pop("bind_host", UNSET)

        port = d.pop("port", UNSET)

        status = d.pop("status", UNSET)

        url = d.pop("url", UNSET)

        transport = cls(
            kind=kind,
            bind_host=bind_host,
            port=port,
            status=status,
            url=url,
        )

        transport.additional_properties = d
        return transport

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
