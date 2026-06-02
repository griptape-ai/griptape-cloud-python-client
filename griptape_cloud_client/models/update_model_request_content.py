from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateModelRequestContent")


@_attrs_define
class UpdateModelRequestContent:
    """
    Attributes:
        active (Union[Unset, bool]):
        auth_config_id (Union[Unset, str]):
        description (Union[Unset, str]):
        kwargs (Union[Unset, Any]):
        model_name (Union[Unset, str]):
        model_type (Union[Unset, ModelType]):
    """

    active: Union[Unset, bool] = UNSET
    auth_config_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    kwargs: Union[Unset, Any] = UNSET
    model_name: Union[Unset, str] = UNSET
    model_type: Union[Unset, ModelType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        auth_config_id = self.auth_config_id

        description = self.description

        kwargs = self.kwargs

        model_name = self.model_name

        model_type: Union[Unset, str] = UNSET
        if not isinstance(self.model_type, Unset):
            model_type = self.model_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if auth_config_id is not UNSET:
            field_dict["auth_config_id"] = auth_config_id
        if description is not UNSET:
            field_dict["description"] = description
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if model_type is not UNSET:
            field_dict["model_type"] = model_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        auth_config_id = d.pop("auth_config_id", UNSET)

        description = d.pop("description", UNSET)

        kwargs = d.pop("kwargs", UNSET)

        model_name = d.pop("model_name", UNSET)

        _model_type = d.pop("model_type", UNSET)
        model_type: Union[Unset, ModelType]
        if isinstance(_model_type, Unset):
            model_type = UNSET
        else:
            model_type = ModelType(_model_type)

        update_model_request_content = cls(
            active=active,
            auth_config_id=auth_config_id,
            description=description,
            kwargs=kwargs,
            model_name=model_name,
            model_type=model_type,
        )

        update_model_request_content.additional_properties = d
        return update_model_request_content

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
