# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .access_policy_ip_access_rule_action import AccessPolicyIpAccessRuleAction

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AccessPolicyIpAccessRule(pydantic.BaseModel):
    """
    Use IP Access Rules to allowlist, block, and challenge traffic based on the visitor IP address.
    """

    name: typing.Optional[str] = pydantic.Field(
        description="Friendly name that will make it easy for you to identify the IP Access Rule in the future."
    )
    value: str = pydantic.Field(
        description="An IP Access rule will apply a certain action to incoming traffic based on the visitor IP address or IP range."
    )
    action: AccessPolicyIpAccessRuleAction = pydantic.Field(
        description=('Access rule can perform one of the following actions: "allow" \n' ' "block".\n')
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
