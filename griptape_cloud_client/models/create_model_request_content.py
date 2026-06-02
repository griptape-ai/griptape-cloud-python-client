from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateModelRequestContent")


@_attrs_define
class CreateModelRequestContent:
    """
    Attributes:
        auth_config_id (str):
        model_name (str):
        model_type (ModelType):
        active (Union[Unset, bool]):
        description (Union[Unset, str]):
        kwargs (Union[Unset, Any]):
    """

    auth_config_id: str
    model_name: str
    model_type: ModelType
    active: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    kwargs: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_config_id = self.auth_config_id

        model_name = self.model_name

        model_type = self.model_type.value

        active = self.active

        description = self.description

        kwargs = self.kwargs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_config_id": auth_config_id,
                "model_name": model_name,
                "model_type": model_type,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if description is not UNSET:
            field_dict["description"] = description
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_config_id = d.pop("auth_config_id")

        model_name = d.pop("model_name")

        model_type = ModelType(d.pop("model_type"))

        active = d.pop("active", UNSET)

        description = d.pop("description", UNSET)

        kwargs = d.pop("kwargs", UNSET)

        create_model_request_content = cls(
            auth_config_id=auth_config_id,
            model_name=model_name,
            model_type=model_type,
            active=active,
            description=description,
            kwargs=kwargs,
        )

        create_model_request_content.additional_properties = d
        return create_model_request_content

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
