# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ConsolidatedBundleUpload(pydantic.BaseModel):
    """
    from metriport.resources.medical import ConsolidatedBundleUpload

    ConsolidatedBundleUpload(
        resource_type="Bundle",
        type="collection",
        entry=[
            {
                "resource": {
                    "resourceType": "Observation",
                    "code": {"text": "Cancer"},
                    "valueCodeableConcept": {"text": "NEGATIVE"},
                    "status": "final",
                    "category": [
                        {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                    "code": "laboratory",
                                }
                            ]
                        }
                    ],
                }
            }
        ],
    )
    """

    resource_type: str = pydantic.Field(alias="resourceType", description="The resource needs to be “Bundle”")
    type: str = pydantic.Field(description="The type needs to be “collection”")
    entry: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="The entry needs to be an array of FHIR resources."
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
