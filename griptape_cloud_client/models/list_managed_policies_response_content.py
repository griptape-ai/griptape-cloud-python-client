from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.managed_policy_detail import ManagedPolicyDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListManagedPoliciesResponseContent")


@_attrs_define
class ListManagedPoliciesResponseContent:
    """
    Attributes:
        managed_policies (list['ManagedPolicyDetail']):
        pagination (Pagination):
    """

    managed_policies: list["ManagedPolicyDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managed_policies = []
        for managed_policies_item_data in self.managed_policies:
            managed_policies_item = managed_policies_item_data.to_dict()
            managed_policies.append(managed_policies_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "managed_policies": managed_policies,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.managed_policy_detail import ManagedPolicyDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        managed_policies = []
        _managed_policies = d.pop("managed_policies")
        for managed_policies_item_data in _managed_policies:
            managed_policies_item = ManagedPolicyDetail.from_dict(managed_policies_item_data)

            managed_policies.append(managed_policies_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_managed_policies_response_content = cls(
            managed_policies=managed_policies,
            pagination=pagination,
        )

        list_managed_policies_response_content.additional_properties = d
        return list_managed_policies_response_content

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
