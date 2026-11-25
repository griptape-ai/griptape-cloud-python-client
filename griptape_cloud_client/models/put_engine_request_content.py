from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_document import EngineDocument
    from ..models.session_client import SessionClient
    from ..models.transport import Transport


T = TypeVar("T", bound="PutEngineRequestContent")


@_attrs_define
class PutEngineRequestContent:
    """
    Attributes:
        engine_name (str):
        engine_version (str):
        clients (Union[Unset, list['SessionClient']]):
        current_workflow (Union[Unset, str]):
        deployment_type (Union[Unset, str]):
        document (Union[Unset, EngineDocument]):
        engine_os (Union[Unset, str]):
        has_active_flow (Union[Unset, bool]):
        instance_provider (Union[Unset, str]):
        instance_region (Union[Unset, str]):
        instance_type (Union[Unset, str]):
        is_executing (Union[Unset, bool]):
        is_initializing (Union[Unset, bool]):
        orchestrator_engine_id (Union[Unset, str]):
        session_id (Union[Unset, str]):
        transports (Union[Unset, list['Transport']]):
        workflow_file_path (Union[Unset, str]):
    """

    engine_name: str
    engine_version: str
    clients: Union[Unset, list["SessionClient"]] = UNSET
    current_workflow: Union[Unset, str] = UNSET
    deployment_type: Union[Unset, str] = UNSET
    document: Union[Unset, "EngineDocument"] = UNSET
    engine_os: Union[Unset, str] = UNSET
    has_active_flow: Union[Unset, bool] = UNSET
    instance_provider: Union[Unset, str] = UNSET
    instance_region: Union[Unset, str] = UNSET
    instance_type: Union[Unset, str] = UNSET
    is_executing: Union[Unset, bool] = UNSET
    is_initializing: Union[Unset, bool] = UNSET
    orchestrator_engine_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    transports: Union[Unset, list["Transport"]] = UNSET
    workflow_file_path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engine_name = self.engine_name

        engine_version = self.engine_version

        clients: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        current_workflow = self.current_workflow

        deployment_type = self.deployment_type

        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        engine_os = self.engine_os

        has_active_flow = self.has_active_flow

        instance_provider = self.instance_provider

        instance_region = self.instance_region

        instance_type = self.instance_type

        is_executing = self.is_executing

        is_initializing = self.is_initializing

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
                "engine_name": engine_name,
                "engine_version": engine_version,
            }
        )
        if clients is not UNSET:
            field_dict["clients"] = clients
        if current_workflow is not UNSET:
            field_dict["current_workflow"] = current_workflow
        if deployment_type is not UNSET:
            field_dict["deployment_type"] = deployment_type
        if document is not UNSET:
            field_dict["document"] = document
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
        engine_name = d.pop("engine_name")

        engine_version = d.pop("engine_version")

        clients = []
        _clients = d.pop("clients", UNSET)
        for clients_item_data in _clients or []:
            clients_item = SessionClient.from_dict(clients_item_data)

            clients.append(clients_item)

        current_workflow = d.pop("current_workflow", UNSET)

        deployment_type = d.pop("deployment_type", UNSET)

        _document = d.pop("document", UNSET)
        document: Union[Unset, EngineDocument]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = EngineDocument.from_dict(_document)

        engine_os = d.pop("engine_os", UNSET)

        has_active_flow = d.pop("has_active_flow", UNSET)

        instance_provider = d.pop("instance_provider", UNSET)

        instance_region = d.pop("instance_region", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        is_executing = d.pop("is_executing", UNSET)

        is_initializing = d.pop("is_initializing", UNSET)

        orchestrator_engine_id = d.pop("orchestrator_engine_id", UNSET)

        session_id = d.pop("session_id", UNSET)

        transports = []
        _transports = d.pop("transports", UNSET)
        for transports_item_data in _transports or []:
            transports_item = Transport.from_dict(transports_item_data)

            transports.append(transports_item)

        workflow_file_path = d.pop("workflow_file_path", UNSET)

        put_engine_request_content = cls(
            engine_name=engine_name,
            engine_version=engine_version,
            clients=clients,
            current_workflow=current_workflow,
            deployment_type=deployment_type,
            document=document,
            engine_os=engine_os,
            has_active_flow=has_active_flow,
            instance_provider=instance_provider,
            instance_region=instance_region,
            instance_type=instance_type,
            is_executing=is_executing,
            is_initializing=is_initializing,
            orchestrator_engine_id=orchestrator_engine_id,
            session_id=session_id,
            transports=transports,
            workflow_file_path=workflow_file_path,
        )

        put_engine_request_content.additional_properties = d
        return put_engine_request_content

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
