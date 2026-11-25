import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.spend_cost_basis import SpendCostBasis
from ..models.spend_funding import SpendFunding
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spend_tag_filter import SpendTagFilter


T = TypeVar("T", bound="SearchSpendRequestContent")


@_attrs_define
class SearchSpendRequestContent:
    """The filters a spend search takes, shared with a spend export so the export holds exactly the rows the search
    matches.

        Attributes:
            cost_basis (Union[Unset, SpendCostBasis]):
            end (Union[Unset, datetime.datetime]): Only spend that occurred at or before this instant.
            funding (Union[Unset, SpendFunding]):
            license_group_id (Union[Unset, str]): Only spend whose license belonged to this group when the work happened,
                which is not necessarily its membership now.
            license_id (Union[Unset, str]): Only spend the given license was billed for. A snapshot, so it still matches
                after the license is deleted.
            model_id (Union[Unset, str]): Only spend against this model. Null on rows where the request let the organization
                default win, so those match no model filter.
            provider (Union[Unset, str]): Only spend served by this vendor. Matches against the row's snapshot, so it still
                finds spend from a provider we no longer integrate.
            start (Union[Unset, datetime.datetime]): Only spend that occurred at or after this instant.
            tag_filters (Union[Unset, list['SpendTagFilter']]): Tag dimensions to filter on, each carrying the modifiers
                that apply to it. Filters combine with AND: spend must match every one given.
    """

    cost_basis: Union[Unset, SpendCostBasis] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    funding: Union[Unset, SpendFunding] = UNSET
    license_group_id: Union[Unset, str] = UNSET
    license_id: Union[Unset, str] = UNSET
    model_id: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    tag_filters: Union[Unset, list["SpendTagFilter"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_basis: Union[Unset, str] = UNSET
        if not isinstance(self.cost_basis, Unset):
            cost_basis = self.cost_basis.value

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        funding: Union[Unset, str] = UNSET
        if not isinstance(self.funding, Unset):
            funding = self.funding.value

        license_group_id = self.license_group_id

        license_id = self.license_id

        model_id = self.model_id

        provider = self.provider

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        tag_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tag_filters, Unset):
            tag_filters = []
            for tag_filters_item_data in self.tag_filters:
                tag_filters_item = tag_filters_item_data.to_dict()
                tag_filters.append(tag_filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_basis is not UNSET:
            field_dict["cost_basis"] = cost_basis
        if end is not UNSET:
            field_dict["end"] = end
        if funding is not UNSET:
            field_dict["funding"] = funding
        if license_group_id is not UNSET:
            field_dict["license_group_id"] = license_group_id
        if license_id is not UNSET:
            field_dict["license_id"] = license_id
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if start is not UNSET:
            field_dict["start"] = start
        if tag_filters is not UNSET:
            field_dict["tag_filters"] = tag_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_tag_filter import SpendTagFilter

        d = dict(src_dict)
        _cost_basis = d.pop("cost_basis", UNSET)
        cost_basis: Union[Unset, SpendCostBasis]
        if isinstance(_cost_basis, Unset):
            cost_basis = UNSET
        else:
            cost_basis = SpendCostBasis(_cost_basis)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        _funding = d.pop("funding", UNSET)
        funding: Union[Unset, SpendFunding]
        if isinstance(_funding, Unset):
            funding = UNSET
        else:
            funding = SpendFunding(_funding)

        license_group_id = d.pop("license_group_id", UNSET)

        license_id = d.pop("license_id", UNSET)

        model_id = d.pop("model_id", UNSET)

        provider = d.pop("provider", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        tag_filters = []
        _tag_filters = d.pop("tag_filters", UNSET)
        for tag_filters_item_data in _tag_filters or []:
            tag_filters_item = SpendTagFilter.from_dict(tag_filters_item_data)

            tag_filters.append(tag_filters_item)

        search_spend_request_content = cls(
            cost_basis=cost_basis,
            end=end,
            funding=funding,
            license_group_id=license_group_id,
            license_id=license_id,
            model_id=model_id,
            provider=provider,
            start=start,
            tag_filters=tag_filters,
        )

        search_spend_request_content.additional_properties = d
        return search_spend_request_content

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
