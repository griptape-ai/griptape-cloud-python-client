import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.credit_rate_kind import CreditRateKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_price_line_cell import CreditPriceLineCell


T = TypeVar("T", bound="CreditPriceLine")


@_attrs_define
class CreditPriceLine:
    """
    Attributes:
        cell (CreditPriceLineCell): The dimension values a price line is priced for, keyed by dimension slug.
        description (str):
        dollar_price (str): The price of the line's unit quantity, in dollars.
        kind (CreditRateKind): A cost rate's kind, as the catalog's CostRateKind defines it. Always LIST on the rate-
            card path.
        meter (str): The meter slug, or the activity name on the rate-card path.
        model_id (Union[None, Unset, str]): The model the meter's usage is charged under. Null when unknown, and always
            null on the rate-card path.
        promo_ends_at (Union[None, Unset, datetime.datetime]): A promo's effective_until. Null otherwise.
        unit (Union[None, Unset, str]): What one unit of volume counts. Null on the rate-card path.
        unit_scale (Union[None, Unset, float]): How many units dollar_price covers. Null on the rate-card path.
    """

    cell: "CreditPriceLineCell"
    description: str
    dollar_price: str
    kind: CreditRateKind
    meter: str
    model_id: Union[None, Unset, str] = UNSET
    promo_ends_at: Union[None, Unset, datetime.datetime] = UNSET
    unit: Union[None, Unset, str] = UNSET
    unit_scale: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cell = self.cell.to_dict()

        description = self.description

        dollar_price = self.dollar_price

        kind = self.kind.value

        meter = self.meter

        model_id: Union[None, Unset, str]
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        promo_ends_at: Union[None, Unset, str]
        if isinstance(self.promo_ends_at, Unset):
            promo_ends_at = UNSET
        elif isinstance(self.promo_ends_at, datetime.datetime):
            promo_ends_at = self.promo_ends_at.isoformat()
        else:
            promo_ends_at = self.promo_ends_at

        unit: Union[None, Unset, str]
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        unit_scale: Union[None, Unset, float]
        if isinstance(self.unit_scale, Unset):
            unit_scale = UNSET
        else:
            unit_scale = self.unit_scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cell": cell,
                "description": description,
                "dollar_price": dollar_price,
                "kind": kind,
                "meter": meter,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if promo_ends_at is not UNSET:
            field_dict["promo_ends_at"] = promo_ends_at
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_scale is not UNSET:
            field_dict["unit_scale"] = unit_scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_price_line_cell import CreditPriceLineCell

        d = dict(src_dict)
        cell = CreditPriceLineCell.from_dict(d.pop("cell"))

        description = d.pop("description")

        dollar_price = d.pop("dollar_price")

        kind = CreditRateKind(d.pop("kind"))

        meter = d.pop("meter")

        def _parse_model_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_promo_ends_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                promo_ends_at_type_0 = isoparse(data)

                return promo_ends_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        promo_ends_at = _parse_promo_ends_at(d.pop("promo_ends_at", UNSET))

        def _parse_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_unit_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        unit_scale = _parse_unit_scale(d.pop("unit_scale", UNSET))

        credit_price_line = cls(
            cell=cell,
            description=description,
            dollar_price=dollar_price,
            kind=kind,
            meter=meter,
            model_id=model_id,
            promo_ends_at=promo_ends_at,
            unit=unit,
            unit_scale=unit_scale,
        )

        credit_price_line.additional_properties = d
        return credit_price_line

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
