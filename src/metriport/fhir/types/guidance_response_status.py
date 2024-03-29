# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GuidanceResponseStatus(str, enum.Enum):
    """
    The status of the response. If the evaluation is completed successfully, the status will indicate success. However, in order to complete the evaluation, the engine may require more information. In this case, the status will be data-required, and the response will contain a description of the additional required information. If the evaluation completed successfully, but the engine determines that a potentially more accurate response could be provided if more data was available, the status will be data-requested, and the response will contain a description of the additional requested information.
    """

    SUCCESS = "success"
    DATA_REQUESTED = "data-requested"
    DATA_REQUIRED = "data-required"
    IN_PROGRESS = "in-progress"
    FAILURE = "failure"
    ENTERED_IN_ERROR = "entered-in-error"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        data_requested: typing.Callable[[], T_Result],
        data_required: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GuidanceResponseStatus.SUCCESS:
            return success()
        if self is GuidanceResponseStatus.DATA_REQUESTED:
            return data_requested()
        if self is GuidanceResponseStatus.DATA_REQUIRED:
            return data_required()
        if self is GuidanceResponseStatus.IN_PROGRESS:
            return in_progress()
        if self is GuidanceResponseStatus.FAILURE:
            return failure()
        if self is GuidanceResponseStatus.ENTERED_IN_ERROR:
            return entered_in_error()
