import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetEngineManifestResponseContent")


@_attrs_define
class GetEngineManifestResponseContent:
    """
    Attributes:
        engine_id (str):
        generated_at (datetime.datetime):
        hash_ (str):
        manifest (Any):
        updated_at (datetime.datetime):
    """

    engine_id: str
    generated_at: datetime.datetime
    hash_: str
    manifest: Any
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engine_id = self.engine_id

        generated_at = self.generated_at.isoformat()

        hash_ = self.hash_

        manifest = self.manifest

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "engine_id": engine_id,
                "generated_at": generated_at,
                "hash": hash_,
                "manifest": manifest,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        engine_id = d.pop("engine_id")

        generated_at = isoparse(d.pop("generated_at"))

        hash_ = d.pop("hash")

        manifest = d.pop("manifest")

        updated_at = isoparse(d.pop("updated_at"))

        get_engine_manifest_response_content = cls(
            engine_id=engine_id,
            generated_at=generated_at,
            hash_=hash_,
            manifest=manifest,
            updated_at=updated_at,
        )

        get_engine_manifest_response_content.additional_properties = d
        return get_engine_manifest_response_content

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
