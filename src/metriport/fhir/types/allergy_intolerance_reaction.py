# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .allergy_intolerance_reaction_severity import AllergyIntoleranceReactionSeverity
from .annotation import Annotation
from .codeable_concept import CodeableConcept
from .date_time import DateTime
from .extension import Extension

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AllergyIntoleranceReaction(pydantic.BaseModel):
    """
    Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.
    """

    id: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
    )
    extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.",
    )
    modifier_extension: typing.Optional[typing.List[Extension]] = pydantic.Field(
        alias="modifierExtension",
        default=None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions. Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    substance: typing.Optional[CodeableConcept] = pydantic.Field(
        default=None,
        description="Identification of the specific substance (or pharmaceutical product) considered to be responsible for the Adverse Reaction event. Note: the substance for a specific reaction may be different from the substance identified as the cause of the risk, but it must be consistent with it. For instance, it may be a more specific substance (e.g. a brand medication) or a composite product that includes the identified substance. It must be clinically safe to only process the 'code' and ignore the 'reaction.substance'. If a receiving system is unable to confirm that AllergyIntolerance.reaction.substance falls within the semantic scope of AllergyIntolerance.code, then the receiving system should ignore AllergyIntolerance.reaction.substance.",
    )
    manifestation: typing.List[CodeableConcept] = pydantic.Field(
        description="Clinical symptoms and/or signs that are observed or associated with the adverse reaction event."
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Text description about the reaction as a whole, including details of the manifestation if required.",
    )
    onset: typing.Optional[DateTime] = pydantic.Field(
        default=None, description="Record of the date and/or time of the onset of the Reaction."
    )
    severity: typing.Optional[AllergyIntoleranceReactionSeverity] = pydantic.Field(
        default=None,
        description="Clinical assessment of the severity of the reaction event as a whole, potentially considering multiple different manifestations.",
    )
    exposure_route: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="exposureRoute",
        default=None,
        description="Identification of the route by which the subject was exposed to the substance.",
    )
    note: typing.Optional[typing.List[Annotation]] = pydantic.Field(
        default=None, description="Additional text about the adverse reaction event not captured in other fields."
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
