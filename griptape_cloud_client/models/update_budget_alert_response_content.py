import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBudgetAlertResponseContent")


@_attrs_define
class UpdateBudgetAlertResponseContent:
    """One threshold crossing, recorded once per budget, window and threshold however many invocations re-cross it.

    Attributes:
        acknowledged (bool):
        admission_refused (bool): The alert was recorded because a HARD budget refused a request, not because spend
            crossed the threshold. A HARD budget refuses when the next request will not fit, so it stops before settled
            spend reaches the limit: this alert means the budget can no longer run work. Only ever true at threshold_pct
            100.
        alert_id (str):
        budget_id (str):
        budget_name (str):
        created_at (datetime.datetime):
        limit_credits (float): The budget's limit when the crossing was recorded.
        organization_id (str):
        spent_credits (float): Enforced spend in the window when the crossing was recorded. Below limit_credits on a
            100% alert where admission_refused is true.
        threshold_pct (float): The percentage of the limit crossed. 100 is the implicit threshold every budget has,
            whether or not alert_thresholds lists it.
        window_start (datetime.datetime): The start of the budget window the crossing happened in. A new window can
            cross the same threshold again.
        notified_at (Union[Unset, datetime.datetime]): When the alert was delivered. Null until a delivery channel has
            sent it.
    """

    acknowledged: bool
    admission_refused: bool
    alert_id: str
    budget_id: str
    budget_name: str
    created_at: datetime.datetime
    limit_credits: float
    organization_id: str
    spent_credits: float
    threshold_pct: float
    window_start: datetime.datetime
    notified_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged = self.acknowledged

        admission_refused = self.admission_refused

        alert_id = self.alert_id

        budget_id = self.budget_id

        budget_name = self.budget_name

        created_at = self.created_at.isoformat()

        limit_credits = self.limit_credits

        organization_id = self.organization_id

        spent_credits = self.spent_credits

        threshold_pct = self.threshold_pct

        window_start = self.window_start.isoformat()

        notified_at: Union[Unset, str] = UNSET
        if not isinstance(self.notified_at, Unset):
            notified_at = self.notified_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledged": acknowledged,
                "admission_refused": admission_refused,
                "alert_id": alert_id,
                "budget_id": budget_id,
                "budget_name": budget_name,
                "created_at": created_at,
                "limit_credits": limit_credits,
                "organization_id": organization_id,
                "spent_credits": spent_credits,
                "threshold_pct": threshold_pct,
                "window_start": window_start,
            }
        )
        if notified_at is not UNSET:
            field_dict["notified_at"] = notified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledged = d.pop("acknowledged")

        admission_refused = d.pop("admission_refused")

        alert_id = d.pop("alert_id")

        budget_id = d.pop("budget_id")

        budget_name = d.pop("budget_name")

        created_at = isoparse(d.pop("created_at"))

        limit_credits = d.pop("limit_credits")

        organization_id = d.pop("organization_id")

        spent_credits = d.pop("spent_credits")

        threshold_pct = d.pop("threshold_pct")

        window_start = isoparse(d.pop("window_start"))

        _notified_at = d.pop("notified_at", UNSET)
        notified_at: Union[Unset, datetime.datetime]
        if isinstance(_notified_at, Unset):
            notified_at = UNSET
        else:
            notified_at = isoparse(_notified_at)

        update_budget_alert_response_content = cls(
            acknowledged=acknowledged,
            admission_refused=admission_refused,
            alert_id=alert_id,
            budget_id=budget_id,
            budget_name=budget_name,
            created_at=created_at,
            limit_credits=limit_credits,
            organization_id=organization_id,
            spent_credits=spent_credits,
            threshold_pct=threshold_pct,
            window_start=window_start,
            notified_at=notified_at,
        )

        update_budget_alert_response_content.additional_properties = d
        return update_budget_alert_response_content

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
