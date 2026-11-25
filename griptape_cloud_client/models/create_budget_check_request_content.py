from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBudgetCheckRequestContent")


@_attrs_define
class CreateBudgetCheckRequestContent:
    """
    Attributes:
        correlation_id (Union[Unset, str]): Client-minted; echo it on the report that follows.
        estimated_cost_micro_usd (Union[Unset, float]): What the call is expected to cost, in micro-USD. Absent blocks
            only where nothing is left.
        model (Union[Unset, str]):
        tags (Union[Unset, Any]): Attribution, in the shape the X-Griptape-Attribution header's tags carry.
    """

    correlation_id: Union[Unset, str] = UNSET
    estimated_cost_micro_usd: Union[Unset, float] = UNSET
    model: Union[Unset, str] = UNSET
    tags: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correlation_id = self.correlation_id

        estimated_cost_micro_usd = self.estimated_cost_micro_usd

        model = self.model

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if estimated_cost_micro_usd is not UNSET:
            field_dict["estimated_cost_micro_usd"] = estimated_cost_micro_usd
        if model is not UNSET:
            field_dict["model"] = model
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        correlation_id = d.pop("correlation_id", UNSET)

        estimated_cost_micro_usd = d.pop("estimated_cost_micro_usd", UNSET)

        model = d.pop("model", UNSET)

        tags = d.pop("tags", UNSET)

        create_budget_check_request_content = cls(
            correlation_id=correlation_id,
            estimated_cost_micro_usd=estimated_cost_micro_usd,
            model=model,
            tags=tags,
        )

        create_budget_check_request_content.additional_properties = d
        return create_budget_check_request_content

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
