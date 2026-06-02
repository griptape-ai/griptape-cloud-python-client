import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.entitlement import Entitlement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_model_config import OrganizationModelConfig


T = TypeVar("T", bound="GetOrganizationResponseContent")


@_attrs_define
class GetOrganizationResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        default_bucket_id (str):
        description (str):
        entitlement (Entitlement):  Default: Entitlement.FREE.
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        model_config (Union[Unset, OrganizationModelConfig]):
    """

    created_at: datetime.datetime
    created_by: str
    default_bucket_id: str
    description: str
    name: str
    organization_id: str
    updated_at: datetime.datetime
    entitlement: Entitlement = Entitlement.FREE
    model_config: Union[Unset, "OrganizationModelConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        default_bucket_id = self.default_bucket_id

        description = self.description

        entitlement = self.entitlement.value

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        model_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model_config, Unset):
            model_config = self.model_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "default_bucket_id": default_bucket_id,
                "description": description,
                "entitlement": entitlement,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
            }
        )
        if model_config is not UNSET:
            field_dict["model_config"] = model_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_model_config import OrganizationModelConfig

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        default_bucket_id = d.pop("default_bucket_id")

        description = d.pop("description")

        entitlement = Entitlement(d.pop("entitlement"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = isoparse(d.pop("updated_at"))

        _model_config = d.pop("model_config", UNSET)
        model_config: Union[Unset, OrganizationModelConfig]
        if isinstance(_model_config, Unset):
            model_config = UNSET
        else:
            model_config = OrganizationModelConfig.from_dict(_model_config)

        get_organization_response_content = cls(
            created_at=created_at,
            created_by=created_by,
            default_bucket_id=default_bucket_id,
            description=description,
            entitlement=entitlement,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            model_config=model_config,
        )

        get_organization_response_content.additional_properties = d
        return get_organization_response_content

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
