# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .codeable_concept import CodeableConcept
from .extension import Extension
from .molecular_sequence_reference_seq_orientation import MolecularSequenceReferenceSeqOrientation
from .molecular_sequence_reference_seq_strand import MolecularSequenceReferenceSeqStrand
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MolecularSequenceReferenceSeq(pydantic.BaseModel):
    """
    Raw data describing a biological sequence.
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
    chromosome: typing.Optional[CodeableConcept] = pydantic.Field(
        description="Structural unit composed of a nucleic acid molecule which controls its own replication through the interaction of specific proteins at one or more origins of replication ([SO:0000340](http://www.sequenceontology.org/browser/current_svn/term/SO:0000340))."
    )
    genome_build: typing.Optional[str] = pydantic.Field(
        alias="genomeBuild",
        description="The Genome Build used for reference, following GRCh build versions e.g. 'GRCh 37'. Version number must be included if a versioned release of a primary build was used.",
    )
    orientation: typing.Optional[MolecularSequenceReferenceSeqOrientation] = pydantic.Field(
        description='A relative reference to a DNA strand based on gene orientation. The strand that contains the open reading frame of the gene is the "sense" strand, and the opposite complementary strand is the "antisense" strand.'
    )
    reference_seq_id: typing.Optional[CodeableConcept] = pydantic.Field(
        alias="referenceSeqId",
        description="Reference identifier of reference sequence submitted to NCBI. It must match the type in the MolecularSequence.type field. For example, the prefix, “NG*” identifies reference sequence for genes, “NM*” for messenger RNA transcripts, and “NP\_” for amino acid sequences.",
    )
    reference_seq_pointer: typing.Optional[Reference] = pydantic.Field(
        alias="referenceSeqPointer", description="A pointer to another MolecularSequence entity as reference sequence."
    )
    reference_seq_string: typing.Optional[str] = pydantic.Field(
        alias="referenceSeqString", description='A string like "ACGT".'
    )
    strand: typing.Optional[MolecularSequenceReferenceSeqStrand] = pydantic.Field(
        description="An absolute reference to a strand. The Watson strand is the strand whose 5'-end is on the short arm of the chromosome, and the Crick strand as the one whose 5'-end is on the long arm."
    )
    window_start: typing.Optional[int] = pydantic.Field(
        alias="windowStart",
        description="Start position of the window on the reference sequence. If the coordinate system is either 0-based or 1-based, then start position is inclusive.",
    )
    window_end: typing.Optional[int] = pydantic.Field(
        alias="windowEnd",
        description="End position of the window on the reference sequence. If the coordinate system is 0-based then end is exclusive and does not include the last position. If the coordinate system is 1-base, then end is inclusive and includes the last position.",
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