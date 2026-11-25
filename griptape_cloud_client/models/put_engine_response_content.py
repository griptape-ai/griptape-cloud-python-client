import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.engine_presence_status import EnginePresenceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_document import EngineDocument
    from ..models.session_client import SessionClient
    from ..models.transport import Transport


T = TypeVar("T", bound="PutEngineResponseContent")


@_attrs_define
class PutEngineResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        document (EngineDocument):
        engine_id (str):
        engine_name (str):
        engine_version (str):
        expires_at (datetime.datetime):
        last_seen (datetime.datetime):
        organization_id (str):
        status (EnginePresenceStatus):
        updated_at (datetime.datetime):
        clients (Union[Unset, list['SessionClient']]):
        current_workflow (Union[Unset, str]):
        deployment_type (Union[Unset, str]):
        engine_os (Union[Unset, str]):
        has_active_flow (Union[Unset, bool]):
        instance_provider (Union[Unset, str]):
        instance_region (Union[Unset, str]):
        instance_type (Union[Unset, str]):
        is_executing (Union[Unset, bool]):
        is_initializing (Union[Unset, bool]):
        license_id (Union[Unset, str]):
        license_session_id (Union[Unset, str]):
        manifest_generated_at (Union[Unset, datetime.datetime]):
        manifest_hash (Union[Unset, str]):
        orchestrator_engine_id (Union[Unset, str]):
        session_id (Union[Unset, str]):
        transports (Union[Unset, list['Transport']]):
        workflow_file_path (Union[Unset, str]):
    """

    created_at: datetime.datetime
    document: "EngineDocument"
    engine_id: str
    engine_name: str
    engine_version: str
    expires_at: datetime.datetime
    last_seen: datetime.datetime
    organization_id: str
    status: EnginePresenceStatus
    updated_at: datetime.datetime
    clients: Union[Unset, list["SessionClient"]] = UNSET
    current_workflow: Union[Unset, str] = UNSET
    deployment_type: Union[Unset, str] = UNSET
    engine_os: Union[Unset, str] = UNSET
    has_active_flow: Union[Unset, bool] = UNSET
    instance_provider: Union[Unset, str] = UNSET
    instance_region: Union[Unset, str] = UNSET
    instance_type: Union[Unset, str] = UNSET
    is_executing: Union[Unset, bool] = UNSET
    is_initializing: Union[Unset, bool] = UNSET
    license_id: Union[Unset, str] = UNSET
    license_session_id: Union[Unset, str] = UNSET
    manifest_generated_at: Union[Unset, datetime.datetime] = UNSET
    manifest_hash: Union[Unset, str] = UNSET
    orchestrator_engine_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    transports: Union[Unset, list["Transport"]] = UNSET
    workflow_file_path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        document = self.document.to_dict()

        engine_id = self.engine_id

        engine_name = self.engine_name

        engine_version = self.engine_version

        expires_at = self.expires_at.isoformat()

        last_seen = self.last_seen.isoformat()

        organization_id = self.organization_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        clients: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        current_workflow = self.current_workflow

        deployment_type = self.deployment_type

        engine_os = self.engine_os

        has_active_flow = self.has_active_flow

        instance_provider = self.instance_provider

        instance_region = self.instance_region

        instance_type = self.instance_type

        is_executing = self.is_executing

        is_initializing = self.is_initializing

        license_id = self.license_id

        license_session_id = self.license_session_id

        manifest_generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.manifest_generated_at, Unset):
            manifest_generated_at = self.manifest_generated_at.isoformat()

        manifest_hash = self.manifest_hash

        orchestrator_engine_id = self.orchestrator_engine_id

        session_id = self.session_id

        transports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transports, Unset):
            transports = []
            for transports_item_data in self.transports:
                transports_item = transports_item_data.to_dict()
                transports.append(transports_item)

        workflow_file_path = self.workflow_file_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "document": document,
                "engine_id": engine_id,
                "engine_name": engine_name,
                "engine_version": engine_version,
                "expires_at": expires_at,
                "last_seen": last_seen,
                "organization_id": organization_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if clients is not UNSET:
            field_dict["clients"] = clients
        if current_workflow is not UNSET:
            field_dict["current_workflow"] = current_workflow
        if deployment_type is not UNSET:
            field_dict["deployment_type"] = deployment_type
        if engine_os is not UNSET:
            field_dict["engine_os"] = engine_os
        if has_active_flow is not UNSET:
            field_dict["has_active_flow"] = has_active_flow
        if instance_provider is not UNSET:
            field_dict["instance_provider"] = instance_provider
        if instance_region is not UNSET:
            field_dict["instance_region"] = instance_region
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if is_executing is not UNSET:
            field_dict["is_executing"] = is_executing
        if is_initializing is not UNSET:
            field_dict["is_initializing"] = is_initializing
        if license_id is not UNSET:
            field_dict["license_id"] = license_id
        if license_session_id is not UNSET:
            field_dict["license_session_id"] = license_session_id
        if manifest_generated_at is not UNSET:
            field_dict["manifest_generated_at"] = manifest_generated_at
        if manifest_hash is not UNSET:
            field_dict["manifest_hash"] = manifest_hash
        if orchestrator_engine_id is not UNSET:
            field_dict["orchestrator_engine_id"] = orchestrator_engine_id
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if transports is not UNSET:
            field_dict["transports"] = transports
        if workflow_file_path is not UNSET:
            field_dict["workflow_file_path"] = workflow_file_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engine_document import EngineDocument
        from ..models.session_client import SessionClient
        from ..models.transport import Transport

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        document = EngineDocument.from_dict(d.pop("document"))

        engine_id = d.pop("engine_id")

        engine_name = d.pop("engine_name")

        engine_version = d.pop("engine_version")

        expires_at = isoparse(d.pop("expires_at"))

        last_seen = isoparse(d.pop("last_seen"))

        organization_id = d.pop("organization_id")

        status = EnginePresenceStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        clients = []
        _clients = d.pop("clients", UNSET)
        for clients_item_data in _clients or []:
            clients_item = SessionClient.from_dict(clients_item_data)

            clients.append(clients_item)

        current_workflow = d.pop("current_workflow", UNSET)

        deployment_type = d.pop("deployment_type", UNSET)

        engine_os = d.pop("engine_os", UNSET)

        has_active_flow = d.pop("has_active_flow", UNSET)

        instance_provider = d.pop("instance_provider", UNSET)

        instance_region = d.pop("instance_region", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        is_executing = d.pop("is_executing", UNSET)

        is_initializing = d.pop("is_initializing", UNSET)

        license_id = d.pop("license_id", UNSET)

        license_session_id = d.pop("license_session_id", UNSET)

        _manifest_generated_at = d.pop("manifest_generated_at", UNSET)
        manifest_generated_at: Union[Unset, datetime.datetime]
        if isinstance(_manifest_generated_at, Unset):
            manifest_generated_at = UNSET
        else:
            manifest_generated_at = isoparse(_manifest_generated_at)

        manifest_hash = d.pop("manifest_hash", UNSET)

        orchestrator_engine_id = d.pop("orchestrator_engine_id", UNSET)

        session_id = d.pop("session_id", UNSET)

        transports = []
        _transports = d.pop("transports", UNSET)
        for transports_item_data in _transports or []:
            transports_item = Transport.from_dict(transports_item_data)

            transports.append(transports_item)

        workflow_file_path = d.pop("workflow_file_path", UNSET)

        put_engine_response_content = cls(
            created_at=created_at,
            document=document,
            engine_id=engine_id,
            engine_name=engine_name,
            engine_version=engine_version,
            expires_at=expires_at,
            last_seen=last_seen,
            organization_id=organization_id,
            status=status,
            updated_at=updated_at,
            clients=clients,
            current_workflow=current_workflow,
            deployment_type=deployment_type,
            engine_os=engine_os,
            has_active_flow=has_active_flow,
            instance_provider=instance_provider,
            instance_region=instance_region,
            instance_type=instance_type,
            is_executing=is_executing,
            is_initializing=is_initializing,
            license_id=license_id,
            license_session_id=license_session_id,
            manifest_generated_at=manifest_generated_at,
            manifest_hash=manifest_hash,
            orchestrator_engine_id=orchestrator_engine_id,
            session_id=session_id,
            transports=transports,
            workflow_file_path=workflow_file_path,
        )

        put_engine_response_content.additional_properties = d
        return put_engine_response_content

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
