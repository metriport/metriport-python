# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AppointmentParticipantRequired(str, enum.Enum):
    """
    Whether this participant is required to be present at the meeting. This covers a use-case where two doctors need to meet to discuss the results for a specific patient, and the patient is not required to be present.
    """

    REQUIRED = "required"
    OPTIONAL = "optional"
    INFORMATION_ONLY = "information-only"

    def visit(
        self,
        required: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
        information_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppointmentParticipantRequired.REQUIRED:
            return required()
        if self is AppointmentParticipantRequired.OPTIONAL:
            return optional()
        if self is AppointmentParticipantRequired.INFORMATION_ONLY:
            return information_only()