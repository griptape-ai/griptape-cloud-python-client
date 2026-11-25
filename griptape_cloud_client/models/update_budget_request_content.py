from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_enforcement import BudgetEnforcement
from ..models.budget_reset_period import BudgetResetPeriod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_tag_matcher_input import BudgetTagMatcherInput
    from ..models.metadata import Metadata


T = TypeVar("T", bound="UpdateBudgetRequestContent")


@_attrs_define
class UpdateBudgetRequestContent:
    """
    Attributes:
        alert_thresholds (Union[Unset, list[float]]):
        enabled (Union[Unset, bool]):
        enforcement (Union[Unset, BudgetEnforcement]): What exceeding the limit does. SOFT observes and alerts while the
            work still runs; HARD refuses the invocation. A frozen budget refuses whatever its enforcement. Where the
            organization's `can_manage_budgets` is false, budgets keep counting spend but don't refuse or alert.
        frozen (Union[Unset, bool]):
        includes_byok (Union[Unset, bool]):
        includes_reported (Union[Unset, bool]):
        limit_credits (Union[Unset, float]):
        matchers (Union[Unset, list['BudgetTagMatcherInput']]): Replaces the budget's matcher list wholesale rather than
            adding to it, so a budget can be narrowed without deleting it.
        metadata (Union[Unset, Metadata]):
        name (Union[Unset, str]):
        reset_period (Union[Unset, BudgetResetPeriod]): How often the spend counter starts over. Boundaries are UTC
            calendar boundaries, and WEEKLY starts on the ISO Monday. LIFETIME is one window, opened at creation and never
            closed.
    """

    alert_thresholds: Union[Unset, list[float]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    enforcement: Union[Unset, BudgetEnforcement] = UNSET
    frozen: Union[Unset, bool] = UNSET
    includes_byok: Union[Unset, bool] = UNSET
    includes_reported: Union[Unset, bool] = UNSET
    limit_credits: Union[Unset, float] = UNSET
    matchers: Union[Unset, list["BudgetTagMatcherInput"]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    name: Union[Unset, str] = UNSET
    reset_period: Union[Unset, BudgetResetPeriod] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_thresholds: Union[Unset, list[float]] = UNSET
        if not isinstance(self.alert_thresholds, Unset):
            alert_thresholds = self.alert_thresholds

        enabled = self.enabled

        enforcement: Union[Unset, str] = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        frozen = self.frozen

        includes_byok = self.includes_byok

        includes_reported = self.includes_reported

        limit_credits = self.limit_credits

        matchers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matchers, Unset):
            matchers = []
            for matchers_item_data in self.matchers:
                matchers_item = matchers_item_data.to_dict()
                matchers.append(matchers_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        reset_period: Union[Unset, str] = UNSET
        if not isinstance(self.reset_period, Unset):
            reset_period = self.reset_period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_thresholds is not UNSET:
            field_dict["alert_thresholds"] = alert_thresholds
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if includes_byok is not UNSET:
            field_dict["includes_byok"] = includes_byok
        if includes_reported is not UNSET:
            field_dict["includes_reported"] = includes_reported
        if limit_credits is not UNSET:
            field_dict["limit_credits"] = limit_credits
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if reset_period is not UNSET:
            field_dict["reset_period"] = reset_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_tag_matcher_input import BudgetTagMatcherInput
        from ..models.metadata import Metadata

        d = dict(src_dict)
        alert_thresholds = cast(list[float], d.pop("alert_thresholds", UNSET))

        enabled = d.pop("enabled", UNSET)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: Union[Unset, BudgetEnforcement]
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = BudgetEnforcement(_enforcement)

        frozen = d.pop("frozen", UNSET)

        includes_byok = d.pop("includes_byok", UNSET)

        includes_reported = d.pop("includes_reported", UNSET)

        limit_credits = d.pop("limit_credits", UNSET)

        matchers = []
        _matchers = d.pop("matchers", UNSET)
        for matchers_item_data in _matchers or []:
            matchers_item = BudgetTagMatcherInput.from_dict(matchers_item_data)

            matchers.append(matchers_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        _reset_period = d.pop("reset_period", UNSET)
        reset_period: Union[Unset, BudgetResetPeriod]
        if isinstance(_reset_period, Unset):
            reset_period = UNSET
        else:
            reset_period = BudgetResetPeriod(_reset_period)

        update_budget_request_content = cls(
            alert_thresholds=alert_thresholds,
            enabled=enabled,
            enforcement=enforcement,
            frozen=frozen,
            includes_byok=includes_byok,
            includes_reported=includes_reported,
            limit_credits=limit_credits,
            matchers=matchers,
            metadata=metadata,
            name=name,
            reset_period=reset_period,
        )

        update_budget_request_content.additional_properties = d
        return update_budget_request_content

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
