from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entitlement_policy_detail import EntitlementPolicyDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListEntitlementPoliciesResponseContent")


@_attrs_define
class ListEntitlementPoliciesResponseContent:
    """
    Attributes:
        entitlement_policies (list['EntitlementPolicyDetail']):
        pagination (Pagination):
    """

    entitlement_policies: list["EntitlementPolicyDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entitlement_policies = []
        for entitlement_policies_item_data in self.entitlement_policies:
            entitlement_policies_item = entitlement_policies_item_data.to_dict()
            entitlement_policies.append(entitlement_policies_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entitlement_policies": entitlement_policies,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entitlement_policy_detail import EntitlementPolicyDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        entitlement_policies = []
        _entitlement_policies = d.pop("entitlement_policies")
        for entitlement_policies_item_data in _entitlement_policies:
            entitlement_policies_item = EntitlementPolicyDetail.from_dict(entitlement_policies_item_data)

            entitlement_policies.append(entitlement_policies_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_entitlement_policies_response_content = cls(
            entitlement_policies=entitlement_policies,
            pagination=pagination,
        )

        list_entitlement_policies_response_content.additional_properties = d
        return list_entitlement_policies_response_content

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
