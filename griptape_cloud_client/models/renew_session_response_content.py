from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RenewSessionResponseContent")


@_attrs_define
class RenewSessionResponseContent:
    """
    Attributes:
        policy_documents (Any):
        session_token (str):
    """

    policy_documents: Any
    session_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_documents = self.policy_documents

        session_token = self.session_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy_documents": policy_documents,
                "session_token": session_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy_documents = d.pop("policy_documents")

        session_token = d.pop("session_token")

        renew_session_response_content = cls(
            policy_documents=policy_documents,
            session_token=session_token,
        )

        renew_session_response_content.additional_properties = d
        return renew_session_response_content

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
