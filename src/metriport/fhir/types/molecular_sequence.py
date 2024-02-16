# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .base_resource import BaseResource
from .identifier import Identifier
from .molecular_sequence_quality import MolecularSequenceQuality
from .molecular_sequence_reference_seq import MolecularSequenceReferenceSeq
from .molecular_sequence_repository import MolecularSequenceRepository
from .molecular_sequence_structure_variant import MolecularSequenceStructureVariant
from .molecular_sequence_type import MolecularSequenceType
from .molecular_sequence_variant import MolecularSequenceVariant
from .quantity import Quantity
from .reference import Reference

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MolecularSequence(BaseResource):
    """
    Raw data describing a biological sequence.
    """

    resource_type: typing_extensions.Literal["MolecularSequence"] = pydantic.Field(alias="resourceType")
    identifier: typing.Optional[typing.List[Identifier]] = pydantic.Field(
        description="A unique identifier for this particular sequence instance. This is a FHIR-defined id."
    )
    type: typing.Optional[MolecularSequenceType] = pydantic.Field(
        description="Amino Acid Sequence/ DNA Sequence / RNA Sequence."
    )
    coordinate_system: typing.Optional[int] = pydantic.Field(
        alias="coordinateSystem",
        description="Whether the sequence is numbered starting at 0 (0-based numbering or coordinates, inclusive start, exclusive end) or starting at 1 (1-based numbering, inclusive start and inclusive end).",
    )
    patient: typing.Optional[Reference] = pydantic.Field(
        description="The patient whose sequencing results are described by this resource."
    )
    specimen: typing.Optional[Reference] = pydantic.Field(description="Specimen used for sequencing.")
    device: typing.Optional[Reference] = pydantic.Field(
        description="The method for sequencing, for example, chip information."
    )
    performer: typing.Optional[Reference] = pydantic.Field(
        description="The organization or lab that should be responsible for this result."
    )
    quantity: typing.Optional[Quantity] = pydantic.Field(
        description="The number of copies of the sequence of interest. (RNASeq)."
    )
    reference_seq: typing.Optional[MolecularSequenceReferenceSeq] = pydantic.Field(
        alias="referenceSeq",
        description="A sequence that is used as a reference to describe variants that are present in a sequence analyzed.",
    )
    variant: typing.Optional[typing.List[MolecularSequenceVariant]] = pydantic.Field(
        description="The definition of variant here originates from Sequence ontology ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This element can represent amino acid or nucleic sequence change(including insertion,deletion,SNP,etc.) It can represent some complex mutation or segment variation with the assist of CIGAR string."
    )
    observed_seq: typing.Optional[str] = pydantic.Field(
        alias="observedSeq",
        description="Sequence that was observed. It is the result marked by referenceSeq along with variant records on referenceSeq. This shall start from referenceSeq.windowStart and end by referenceSeq.windowEnd.",
    )
    quality: typing.Optional[typing.List[MolecularSequenceQuality]] = pydantic.Field(
        description="An experimental feature attribute that defines the quality of the feature in a quantitative way, such as a phred quality score ([SO:0001686](http://www.sequenceontology.org/browser/current_svn/term/SO:0001686))."
    )
    read_coverage: typing.Optional[int] = pydantic.Field(
        alias="readCoverage",
        description="Coverage (read depth or depth) is the average number of reads representing a given nucleotide in the reconstructed sequence.",
    )
    repository: typing.Optional[typing.List[MolecularSequenceRepository]] = pydantic.Field(
        description="Configurations of the external repository. The repository shall store target's observedSeq or records related with target's observedSeq."
    )
    pointer: typing.Optional[typing.List[Reference]] = pydantic.Field(
        description="Pointer to next atomic sequence which at most contains one variant."
    )
    structure_variant: typing.Optional[typing.List[MolecularSequenceStructureVariant]] = pydantic.Field(
        alias="structureVariant", description="Information about chromosome structure variation."
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