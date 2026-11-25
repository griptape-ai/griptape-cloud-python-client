from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credit_price_line import CreditPriceLine


T = TypeVar("T", bound="GetCreditPricingResponseContent")


@_attrs_define
class GetCreditPricingResponseContent:
    """
    Attributes:
        pricing (list['CreditPriceLine']):
    """

    pricing: list["CreditPriceLine"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pricing = []
        for pricing_item_data in self.pricing:
            pricing_item = pricing_item_data.to_dict()
            pricing.append(pricing_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pricing": pricing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_price_line import CreditPriceLine

        d = dict(src_dict)
        pricing = []
        _pricing = d.pop("pricing")
        for pricing_item_data in _pricing:
            pricing_item = CreditPriceLine.from_dict(pricing_item_data)

            pricing.append(pricing_item)

        get_credit_pricing_response_content = cls(
            pricing=pricing,
        )

        get_credit_pricing_response_content.additional_properties = d
        return get_credit_pricing_response_content

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
