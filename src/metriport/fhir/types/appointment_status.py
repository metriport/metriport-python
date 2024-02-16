# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AppointmentStatus(str, enum.Enum):
    """
    The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status.
    """

    PROPOSED = "proposed"
    PENDING = "pending"
    BOOKED = "booked"
    ARRIVED = "arrived"
    FULFILLED = "fulfilled"
    CANCELLED = "cancelled"
    NOSHOW = "noshow"
    ENTERED_IN_ERROR = "entered-in-error"
    CHECKED_IN = "checked-in"
    WAITLIST = "waitlist"

    def visit(
        self,
        proposed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        booked: typing.Callable[[], T_Result],
        arrived: typing.Callable[[], T_Result],
        fulfilled: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        noshow: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
        checked_in: typing.Callable[[], T_Result],
        waitlist: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppointmentStatus.PROPOSED:
            return proposed()
        if self is AppointmentStatus.PENDING:
            return pending()
        if self is AppointmentStatus.BOOKED:
            return booked()
        if self is AppointmentStatus.ARRIVED:
            return arrived()
        if self is AppointmentStatus.FULFILLED:
            return fulfilled()
        if self is AppointmentStatus.CANCELLED:
            return cancelled()
        if self is AppointmentStatus.NOSHOW:
            return noshow()
        if self is AppointmentStatus.ENTERED_IN_ERROR:
            return entered_in_error()
        if self is AppointmentStatus.CHECKED_IN:
            return checked_in()
        if self is AppointmentStatus.WAITLIST:
            return waitlist()