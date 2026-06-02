import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_type import ModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_config_detail import AuthConfigDetail


T = TypeVar("T", bound="UpdateModelResponseContent")


@_attrs_define
class UpdateModelResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        default (bool):
        model_name (str):
        model_type (ModelType):
        updated_at (datetime.datetime):
        active (Union[Unset, bool]):
        auth_config (Union[Unset, AuthConfigDetail]):
        description (Union[Unset, str]):
        editable (Union[Unset, bool]):
        kwargs (Union[Unset, Any]):
        model_config_id (Union[Unset, str]):
        source (Union[Unset, str]):
    """

    created_at: datetime.datetime
    default: bool
    model_name: str
    model_type: ModelType
    updated_at: datetime.datetime
    active: Union[Unset, bool] = UNSET
    auth_config: Union[Unset, "AuthConfigDetail"] = UNSET
    description: Union[Unset, str] = UNSET
    editable: Union[Unset, bool] = UNSET
    kwargs: Union[Unset, Any] = UNSET
    model_config_id: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        default = self.default

        model_name = self.model_name

        model_type = self.model_type.value

        updated_at = self.updated_at.isoformat()

        active = self.active

        auth_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()

        description = self.description

        editable = self.editable

        kwargs = self.kwargs

        model_config_id = self.model_config_id

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "default": default,
                "model_name": model_name,
                "model_type": model_type,
                "updated_at": updated_at,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if auth_config is not UNSET:
            field_dict["auth_config"] = auth_config
        if description is not UNSET:
            field_dict["description"] = description
        if editable is not UNSET:
            field_dict["editable"] = editable
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs
        if model_config_id is not UNSET:
            field_dict["model_config_id"] = model_config_id
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_config_detail import AuthConfigDetail

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        default = d.pop("default")

        model_name = d.pop("model_name")

        model_type = ModelType(d.pop("model_type"))

        updated_at = isoparse(d.pop("updated_at"))

        active = d.pop("active", UNSET)

        _auth_config = d.pop("auth_config", UNSET)
        auth_config: Union[Unset, AuthConfigDetail]
        if isinstance(_auth_config, Unset):
            auth_config = UNSET
        else:
            auth_config = AuthConfigDetail.from_dict(_auth_config)

        description = d.pop("description", UNSET)

        editable = d.pop("editable", UNSET)

        kwargs = d.pop("kwargs", UNSET)

        model_config_id = d.pop("model_config_id", UNSET)

        source = d.pop("source", UNSET)

        update_model_response_content = cls(
            created_at=created_at,
            default=default,
            model_name=model_name,
            model_type=model_type,
            updated_at=updated_at,
            active=active,
            auth_config=auth_config,
            description=description,
            editable=editable,
            kwargs=kwargs,
            model_config_id=model_config_id,
            source=source,
        )

        update_model_response_content.additional_properties = d
        return update_model_response_content

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
