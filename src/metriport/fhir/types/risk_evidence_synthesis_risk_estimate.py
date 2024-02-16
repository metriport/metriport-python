# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .decimal import Decimal
from .extension import Extension
from .risk_evidence_synthesis_precision_estimate import RiskEvidenceSynthesisPrecisionEstimate

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RiskEvidenceSynthesisRiskEstimate(pydantic.BaseModel):
    """
    The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
    """

    id: typing.Optional[str] = pydantic.Field(
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    description: typing.Optional[str] = pydantic.Field(description="Human-readable summary of risk estimate.")
    type: typing.Optional[CodeableConcept] = pydantic.Field(description="Examples include proportion and mean.")
    value: typing.Optional[Decimal] = pydantic.Field(description="The point estimate of the risk estimate.")
    unit_of_measure: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="unitOfMeasure", description="Specifies the UCUM unit for the outcome."
    )
    denominator_count: typing.Optional[int] = pydantic.Field(
        alias="denominatorCount", description="The sample size for the group that was measured for this risk estimate."
    )
    numerator_count: typing.Optional[int] = pydantic.Field(
        alias="numeratorCount", description="The number of group members with the outcome of interest."
    )
    precision_estimate: typing.Optional[typing.List[RiskEvidenceSynthesisPrecisionEstimate]] = pydantic.Field(
        alias="precisionEstimate", description="A description of the precision of the estimate for the effect."
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