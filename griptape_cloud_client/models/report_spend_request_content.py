import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportSpendRequestContent")


@_attrs_define
class ReportSpendRequestContent:
    """
    Attributes:
        idempotency_key (str): Client-minted and stable across retries of the same report. Keys starting with `check:`
            are reserved.
        activity_type (Union[Unset, str]):
        correlation_id (Union[Unset, str]): Echoes the correlation_id of the budget check this report follows, if any.
        declared_cost_micro_usd (Union[Unset, float]): What the work cost, in micro-USD (1,000,000 == $1). Required
            unless reversing.
        model (Union[Unset, str]):
        occurred_at (Union[Unset, datetime.datetime]): When the work happened. Kept for the record; the row counts
            against the window open when the report arrives.
        provider (Union[Unset, str]):
        reverses_spend_id (Union[Unset, str]): The reported row to cancel. Sent alone: a reversal declares nothing.
        tags (Union[Unset, Any]): Attribution, in the shape the X-Griptape-Attribution header's tags carry.
    """

    idempotency_key: str
    activity_type: Union[Unset, str] = UNSET
    correlation_id: Union[Unset, str] = UNSET
    declared_cost_micro_usd: Union[Unset, float] = UNSET
    model: Union[Unset, str] = UNSET
    occurred_at: Union[Unset, datetime.datetime] = UNSET
    provider: Union[Unset, str] = UNSET
    reverses_spend_id: Union[Unset, str] = UNSET
    tags: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        activity_type = self.activity_type

        correlation_id = self.correlation_id

        declared_cost_micro_usd = self.declared_cost_micro_usd

        model = self.model

        occurred_at: Union[Unset, str] = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        provider = self.provider

        reverses_spend_id = self.reverses_spend_id

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
            }
        )
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if declared_cost_micro_usd is not UNSET:
            field_dict["declared_cost_micro_usd"] = declared_cost_micro_usd
        if model is not UNSET:
            field_dict["model"] = model
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if provider is not UNSET:
            field_dict["provider"] = provider
        if reverses_spend_id is not UNSET:
            field_dict["reverses_spend_id"] = reverses_spend_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        activity_type = d.pop("activity_type", UNSET)

        correlation_id = d.pop("correlation_id", UNSET)

        declared_cost_micro_usd = d.pop("declared_cost_micro_usd", UNSET)

        model = d.pop("model", UNSET)

        _occurred_at = d.pop("occurred_at", UNSET)
        occurred_at: Union[Unset, datetime.datetime]
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)

        provider = d.pop("provider", UNSET)

        reverses_spend_id = d.pop("reverses_spend_id", UNSET)

        tags = d.pop("tags", UNSET)

        report_spend_request_content = cls(
            idempotency_key=idempotency_key,
            activity_type=activity_type,
            correlation_id=correlation_id,
            declared_cost_micro_usd=declared_cost_micro_usd,
            model=model,
            occurred_at=occurred_at,
            provider=provider,
            reverses_spend_id=reverses_spend_id,
            tags=tags,
        )

        report_spend_request_content.additional_properties = d
        return report_spend_request_content

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
