import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.spend_cost_basis import SpendCostBasis
from ..models.spend_funding import SpendFunding
from ..models.spend_path import SpendPath
from ..models.spend_status import SpendStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spend_tags import SpendTags


T = TypeVar("T", bound="SpendDetail")


@_attrs_define
class SpendDetail:
    """
    Attributes:
        billable (bool):
        byok (bool): The caller supplied their own provider credentials, so we brokered the call but paid nothing.
        cost_basis (SpendCostBasis):
        funding (SpendFunding):
        occurred_at (datetime.datetime): When the work counts. For reported spend this is when the report arrived, so a
            late report lands in the window open now.
        organization_id (str):
        path (SpendPath):
        recorded_at (datetime.datetime):
        resolved_tags (SpendTags): A tag namespace: each key maps to its value, ordered leaf first, so the leaf a budget
            matches is the first entry.
        spend_id (str):
        status (SpendStatus):
        tags (SpendTags): A tag namespace: each key maps to its value, ordered leaf first, so the leaf a budget matches
            is the first entry.
        activity_type (Union[Unset, str]):
        activity_volume (Union[Unset, float]):
        correlation_id (Union[Unset, str]): Client-minted id a budget check and the report that followed it both carry.
            Binds nothing.
        cost_credits (Union[Unset, float]): Credits actually debited from the organization's balance.
        estimated_credits (Union[Unset, float]): What this invocation would have cost, for work the service brokered but
            did not pay for.
        external_ref (Union[Unset, str]):
        generation_id (Union[Unset, str]): Exactly one dedupe anchor is set per row.
        idempotency_key (Union[Unset, str]):
        license_group_ids (Union[Unset, list[str]]): The license's group membership when the work happened, not its
            membership now.
        license_id (Union[Unset, str]):
        modality (Union[Unset, str]): The media type the activity produces: image, video, 3d, text, or audio.
        model_id (Union[Unset, str]):
        provider (Union[Unset, str]): Which vendor served the work.
        rate_snapshot (Union[Unset, Any]): The unit rate applied and its basis, stamped at time of work so a repricing
            cannot rewrite it.
        reported_occurred_at (Union[Unset, datetime.datetime]): For reported spend, when the client says the work
            happened.
        reverses_spend_id (Union[Unset, str]): On a reversal, the reported row it cancels.
        settled_at (Union[Unset, datetime.datetime]):
        usage (Union[Unset, Any]): Provider-reported usage quantities, such as per-direction chat token counts.
    """

    billable: bool
    byok: bool
    cost_basis: SpendCostBasis
    funding: SpendFunding
    occurred_at: datetime.datetime
    organization_id: str
    path: SpendPath
    recorded_at: datetime.datetime
    resolved_tags: "SpendTags"
    spend_id: str
    status: SpendStatus
    tags: "SpendTags"
    activity_type: Union[Unset, str] = UNSET
    activity_volume: Union[Unset, float] = UNSET
    correlation_id: Union[Unset, str] = UNSET
    cost_credits: Union[Unset, float] = UNSET
    estimated_credits: Union[Unset, float] = UNSET
    external_ref: Union[Unset, str] = UNSET
    generation_id: Union[Unset, str] = UNSET
    idempotency_key: Union[Unset, str] = UNSET
    license_group_ids: Union[Unset, list[str]] = UNSET
    license_id: Union[Unset, str] = UNSET
    modality: Union[Unset, str] = UNSET
    model_id: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    rate_snapshot: Union[Unset, Any] = UNSET
    reported_occurred_at: Union[Unset, datetime.datetime] = UNSET
    reverses_spend_id: Union[Unset, str] = UNSET
    settled_at: Union[Unset, datetime.datetime] = UNSET
    usage: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billable = self.billable

        byok = self.byok

        cost_basis = self.cost_basis.value

        funding = self.funding.value

        occurred_at = self.occurred_at.isoformat()

        organization_id = self.organization_id

        path = self.path.value

        recorded_at = self.recorded_at.isoformat()

        resolved_tags = self.resolved_tags.to_dict()

        spend_id = self.spend_id

        status = self.status.value

        tags = self.tags.to_dict()

        activity_type = self.activity_type

        activity_volume = self.activity_volume

        correlation_id = self.correlation_id

        cost_credits = self.cost_credits

        estimated_credits = self.estimated_credits

        external_ref = self.external_ref

        generation_id = self.generation_id

        idempotency_key = self.idempotency_key

        license_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.license_group_ids, Unset):
            license_group_ids = self.license_group_ids

        license_id = self.license_id

        modality = self.modality

        model_id = self.model_id

        provider = self.provider

        rate_snapshot = self.rate_snapshot

        reported_occurred_at: Union[Unset, str] = UNSET
        if not isinstance(self.reported_occurred_at, Unset):
            reported_occurred_at = self.reported_occurred_at.isoformat()

        reverses_spend_id = self.reverses_spend_id

        settled_at: Union[Unset, str] = UNSET
        if not isinstance(self.settled_at, Unset):
            settled_at = self.settled_at.isoformat()

        usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billable": billable,
                "byok": byok,
                "cost_basis": cost_basis,
                "funding": funding,
                "occurred_at": occurred_at,
                "organization_id": organization_id,
                "path": path,
                "recorded_at": recorded_at,
                "resolved_tags": resolved_tags,
                "spend_id": spend_id,
                "status": status,
                "tags": tags,
            }
        )
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if activity_volume is not UNSET:
            field_dict["activity_volume"] = activity_volume
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if cost_credits is not UNSET:
            field_dict["cost_credits"] = cost_credits
        if estimated_credits is not UNSET:
            field_dict["estimated_credits"] = estimated_credits
        if external_ref is not UNSET:
            field_dict["external_ref"] = external_ref
        if generation_id is not UNSET:
            field_dict["generation_id"] = generation_id
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if license_group_ids is not UNSET:
            field_dict["license_group_ids"] = license_group_ids
        if license_id is not UNSET:
            field_dict["license_id"] = license_id
        if modality is not UNSET:
            field_dict["modality"] = modality
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if rate_snapshot is not UNSET:
            field_dict["rate_snapshot"] = rate_snapshot
        if reported_occurred_at is not UNSET:
            field_dict["reported_occurred_at"] = reported_occurred_at
        if reverses_spend_id is not UNSET:
            field_dict["reverses_spend_id"] = reverses_spend_id
        if settled_at is not UNSET:
            field_dict["settled_at"] = settled_at
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_tags import SpendTags

        d = dict(src_dict)
        billable = d.pop("billable")

        byok = d.pop("byok")

        cost_basis = SpendCostBasis(d.pop("cost_basis"))

        funding = SpendFunding(d.pop("funding"))

        occurred_at = isoparse(d.pop("occurred_at"))

        organization_id = d.pop("organization_id")

        path = SpendPath(d.pop("path"))

        recorded_at = isoparse(d.pop("recorded_at"))

        resolved_tags = SpendTags.from_dict(d.pop("resolved_tags"))

        spend_id = d.pop("spend_id")

        status = SpendStatus(d.pop("status"))

        tags = SpendTags.from_dict(d.pop("tags"))

        activity_type = d.pop("activity_type", UNSET)

        activity_volume = d.pop("activity_volume", UNSET)

        correlation_id = d.pop("correlation_id", UNSET)

        cost_credits = d.pop("cost_credits", UNSET)

        estimated_credits = d.pop("estimated_credits", UNSET)

        external_ref = d.pop("external_ref", UNSET)

        generation_id = d.pop("generation_id", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        license_group_ids = cast(list[str], d.pop("license_group_ids", UNSET))

        license_id = d.pop("license_id", UNSET)

        modality = d.pop("modality", UNSET)

        model_id = d.pop("model_id", UNSET)

        provider = d.pop("provider", UNSET)

        rate_snapshot = d.pop("rate_snapshot", UNSET)

        _reported_occurred_at = d.pop("reported_occurred_at", UNSET)
        reported_occurred_at: Union[Unset, datetime.datetime]
        if isinstance(_reported_occurred_at, Unset):
            reported_occurred_at = UNSET
        else:
            reported_occurred_at = isoparse(_reported_occurred_at)

        reverses_spend_id = d.pop("reverses_spend_id", UNSET)

        _settled_at = d.pop("settled_at", UNSET)
        settled_at: Union[Unset, datetime.datetime]
        if isinstance(_settled_at, Unset):
            settled_at = UNSET
        else:
            settled_at = isoparse(_settled_at)

        usage = d.pop("usage", UNSET)

        spend_detail = cls(
            billable=billable,
            byok=byok,
            cost_basis=cost_basis,
            funding=funding,
            occurred_at=occurred_at,
            organization_id=organization_id,
            path=path,
            recorded_at=recorded_at,
            resolved_tags=resolved_tags,
            spend_id=spend_id,
            status=status,
            tags=tags,
            activity_type=activity_type,
            activity_volume=activity_volume,
            correlation_id=correlation_id,
            cost_credits=cost_credits,
            estimated_credits=estimated_credits,
            external_ref=external_ref,
            generation_id=generation_id,
            idempotency_key=idempotency_key,
            license_group_ids=license_group_ids,
            license_id=license_id,
            modality=modality,
            model_id=model_id,
            provider=provider,
            rate_snapshot=rate_snapshot,
            reported_occurred_at=reported_occurred_at,
            reverses_spend_id=reverses_spend_id,
            settled_at=settled_at,
            usage=usage,
        )

        spend_detail.additional_properties = d
        return spend_detail

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
