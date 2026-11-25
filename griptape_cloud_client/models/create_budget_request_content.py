from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_enforcement import BudgetEnforcement
from ..models.budget_reset_period import BudgetResetPeriod
from ..models.budget_scope_type import BudgetScopeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_tag_matcher_input import BudgetTagMatcherInput
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateBudgetRequestContent")


@_attrs_define
class CreateBudgetRequestContent:
    """
    Attributes:
        enforcement (BudgetEnforcement): What exceeding the limit does. SOFT observes and alerts while the work still
            runs; HARD refuses the invocation. A frozen budget refuses whatever its enforcement. Where the organization's
            `can_manage_budgets` is false, budgets keep counting spend but don't refuse or alert.
        limit_credits (float):
        name (str):
        reset_period (BudgetResetPeriod): How often the spend counter starts over. Boundaries are UTC calendar
            boundaries, and WEEKLY starts on the ISO Monday. LIFETIME is one window, opened at creation and never closed.
        scope_type (BudgetScopeType): What a budget is drawn around. ORG covers every credit-consuming invocation in the
            organization; TAG covers the chains its matchers name; LICENSE and LICENSE_GROUP cover an identity.
        alert_thresholds (Union[Unset, list[float]]):
        enabled (Union[Unset, bool]):
        frozen (Union[Unset, bool]):
        includes_byok (Union[Unset, bool]):
        includes_reported (Union[Unset, bool]):
        matchers (Union[Unset, list['BudgetTagMatcherInput']]): Required when scope_type is TAG, and rejected otherwise.
        metadata (Union[Unset, Metadata]):
        scope_license_group_id (Union[Unset, str]):
        scope_license_id (Union[Unset, str]):
    """

    enforcement: BudgetEnforcement
    limit_credits: float
    name: str
    reset_period: BudgetResetPeriod
    scope_type: BudgetScopeType
    alert_thresholds: Union[Unset, list[float]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    frozen: Union[Unset, bool] = UNSET
    includes_byok: Union[Unset, bool] = UNSET
    includes_reported: Union[Unset, bool] = UNSET
    matchers: Union[Unset, list["BudgetTagMatcherInput"]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    scope_license_group_id: Union[Unset, str] = UNSET
    scope_license_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enforcement = self.enforcement.value

        limit_credits = self.limit_credits

        name = self.name

        reset_period = self.reset_period.value

        scope_type = self.scope_type.value

        alert_thresholds: Union[Unset, list[float]] = UNSET
        if not isinstance(self.alert_thresholds, Unset):
            alert_thresholds = self.alert_thresholds

        enabled = self.enabled

        frozen = self.frozen

        includes_byok = self.includes_byok

        includes_reported = self.includes_reported

        matchers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matchers, Unset):
            matchers = []
            for matchers_item_data in self.matchers:
                matchers_item = matchers_item_data.to_dict()
                matchers.append(matchers_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        scope_license_group_id = self.scope_license_group_id

        scope_license_id = self.scope_license_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enforcement": enforcement,
                "limit_credits": limit_credits,
                "name": name,
                "reset_period": reset_period,
                "scope_type": scope_type,
            }
        )
        if alert_thresholds is not UNSET:
            field_dict["alert_thresholds"] = alert_thresholds
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if includes_byok is not UNSET:
            field_dict["includes_byok"] = includes_byok
        if includes_reported is not UNSET:
            field_dict["includes_reported"] = includes_reported
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if scope_license_group_id is not UNSET:
            field_dict["scope_license_group_id"] = scope_license_group_id
        if scope_license_id is not UNSET:
            field_dict["scope_license_id"] = scope_license_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_tag_matcher_input import BudgetTagMatcherInput
        from ..models.metadata import Metadata

        d = dict(src_dict)
        enforcement = BudgetEnforcement(d.pop("enforcement"))

        limit_credits = d.pop("limit_credits")

        name = d.pop("name")

        reset_period = BudgetResetPeriod(d.pop("reset_period"))

        scope_type = BudgetScopeType(d.pop("scope_type"))

        alert_thresholds = cast(list[float], d.pop("alert_thresholds", UNSET))

        enabled = d.pop("enabled", UNSET)

        frozen = d.pop("frozen", UNSET)

        includes_byok = d.pop("includes_byok", UNSET)

        includes_reported = d.pop("includes_reported", UNSET)

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

        scope_license_group_id = d.pop("scope_license_group_id", UNSET)

        scope_license_id = d.pop("scope_license_id", UNSET)

        create_budget_request_content = cls(
            enforcement=enforcement,
            limit_credits=limit_credits,
            name=name,
            reset_period=reset_period,
            scope_type=scope_type,
            alert_thresholds=alert_thresholds,
            enabled=enabled,
            frozen=frozen,
            includes_byok=includes_byok,
            includes_reported=includes_reported,
            matchers=matchers,
            metadata=metadata,
            scope_license_group_id=scope_license_group_id,
            scope_license_id=scope_license_id,
        )

        create_budget_request_content.additional_properties = d
        return create_budget_request_content

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
