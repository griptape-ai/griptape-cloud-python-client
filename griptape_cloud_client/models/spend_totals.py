from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.customer_account_totals import CustomerAccountTotals
    from ..models.griptape_credits_totals import GriptapeCreditsTotals


T = TypeVar("T", bound="SpendTotals")


@_attrs_define
class SpendTotals:
    """Subtotals per funding source.

    Attributes:
        customer_account (CustomerAccountTotals): Cost the customer's own accounts carried. estimated_credits values
            exact usage we brokered but did not pay for; declared_credits is client-reported.
        griptape_credits (GriptapeCreditsTotals): Credits drawn from the organization's balance. Exact: it is what was
            debited.
    """

    customer_account: "CustomerAccountTotals"
    griptape_credits: "GriptapeCreditsTotals"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_account = self.customer_account.to_dict()

        griptape_credits = self.griptape_credits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_account": customer_account,
                "griptape_credits": griptape_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_account_totals import CustomerAccountTotals
        from ..models.griptape_credits_totals import GriptapeCreditsTotals

        d = dict(src_dict)
        customer_account = CustomerAccountTotals.from_dict(d.pop("customer_account"))

        griptape_credits = GriptapeCreditsTotals.from_dict(d.pop("griptape_credits"))

        spend_totals = cls(
            customer_account=customer_account,
            griptape_credits=griptape_credits,
        )

        spend_totals.additional_properties = d
        return spend_totals

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
