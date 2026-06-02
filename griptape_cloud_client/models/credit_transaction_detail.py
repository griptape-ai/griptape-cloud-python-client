import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.credit_transaction_type import CreditTransactionType

T = TypeVar("T", bound="CreditTransactionDetail")


@_attrs_define
class CreditTransactionDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        credits_ (float):
        organization_id (str):
        transaction_id (str):
        transaction_type (CreditTransactionType):  Default: CreditTransactionType.DEBIT.
    """

    created_at: datetime.datetime
    credits_: float
    organization_id: str
    transaction_id: str
    transaction_type: CreditTransactionType = CreditTransactionType.DEBIT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        credits_ = self.credits_

        organization_id = self.organization_id

        transaction_id = self.transaction_id

        transaction_type = self.transaction_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "credits": credits_,
                "organization_id": organization_id,
                "transaction_id": transaction_id,
                "transaction_type": transaction_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        credits_ = d.pop("credits")

        organization_id = d.pop("organization_id")

        transaction_id = d.pop("transaction_id")

        transaction_type = CreditTransactionType(d.pop("transaction_type"))

        credit_transaction_detail = cls(
            created_at=created_at,
            credits_=credits_,
            organization_id=organization_id,
            transaction_id=transaction_id,
            transaction_type=transaction_type,
        )

        credit_transaction_detail.additional_properties = d
        return credit_transaction_detail

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
