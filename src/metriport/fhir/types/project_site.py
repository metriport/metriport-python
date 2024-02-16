# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProjectSite(pydantic.BaseModel):
    """
    Web application or web site that is associated with the project.
    """

    name: str = pydantic.Field(
        description="Friendly name that will make it easy for you to identify the site in the future."
    )
    domain: typing.List[str] = pydantic.Field(
        description="The list of domain names associated with the site. User authentication will be restricted to the domains you enter here, plus any subdomains. In other words, a registration for example.com also registers subdomain.example.com. A valid domain requires a host and must not include any path, port, query or fragment."
    )
    google_client_id: typing.Optional[str] = pydantic.Field(
        alias="googleClientId",
        description="The publicly visible Google Client ID for the site. This is used to authenticate users with Google. This value is available in the Google Developer Console.",
    )
    google_client_secret: typing.Optional[str] = pydantic.Field(
        alias="googleClientSecret",
        description="The private Google Client Secret for the site. This value is available in the Google Developer Console.",
    )
    recaptcha_site_key: typing.Optional[str] = pydantic.Field(
        alias="recaptchaSiteKey",
        description="The publicly visible reCAPTCHA site key. This value is generated when you create a new reCAPTCHA site in the reCAPTCHA admin console. Use this site key in the HTML code your site serves to users.",
    )
    recaptcha_secret_key: typing.Optional[str] = pydantic.Field(
        alias="recaptchaSecretKey",
        description="The private reCAPTCHA secret key. This value is generated when you create a new reCAPTCHA site in the reCAPTCHA admin console. Use this secret key for communication between your site and reCAPTCHA.",
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}