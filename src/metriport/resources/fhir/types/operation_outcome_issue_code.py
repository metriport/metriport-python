# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OperationOutcomeIssueCode(str, enum.Enum):
    """
    Describes the type of the issue. The system that creates an OperationOutcome SHALL choose the most applicable code from the IssueType value set, and may additional provide its own code for the error in the details element.
    """

    INVALID = "invalid"
    STRUCTURE = "structure"
    REQUIRED = "required"
    VALUE = "value"
    INVARIANT = "invariant"
    SECURITY = "security"
    LOGIN = "login"
    UNKNOWN = "unknown"
    EXPIRED = "expired"
    FORBIDDEN = "forbidden"
    SUPPRESSED = "suppressed"
    PROCESSING = "processing"
    NOT_SUPPORTED = "not-supported"
    DUPLICATE = "duplicate"
    MULTIPLE_MATCHES = "multiple-matches"
    NOT_FOUND = "not-found"
    DELETED = "deleted"
    TOO_LONG = "too-long"
    CODE_INVALID = "code-invalid"
    EXTENSION = "extension"
    TOO_COSTLY = "too-costly"
    BUSINESS_RULE = "business-rule"
    CONFLICT = "conflict"
    TRANSIENT = "transient"
    LOCK_ERROR = "lock-error"
    NO_STORE = "no-store"
    EXCEPTION = "exception"
    TIMEOUT = "timeout"
    INCOMPLETE = "incomplete"
    THROTTLED = "throttled"
    INFORMATIONAL = "informational"

    def visit(
        self,
        invalid: typing.Callable[[], T_Result],
        structure: typing.Callable[[], T_Result],
        required: typing.Callable[[], T_Result],
        value: typing.Callable[[], T_Result],
        invariant: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        login: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        suppressed: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        not_supported: typing.Callable[[], T_Result],
        duplicate: typing.Callable[[], T_Result],
        multiple_matches: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        too_long: typing.Callable[[], T_Result],
        code_invalid: typing.Callable[[], T_Result],
        extension: typing.Callable[[], T_Result],
        too_costly: typing.Callable[[], T_Result],
        business_rule: typing.Callable[[], T_Result],
        conflict: typing.Callable[[], T_Result],
        transient: typing.Callable[[], T_Result],
        lock_error: typing.Callable[[], T_Result],
        no_store: typing.Callable[[], T_Result],
        exception: typing.Callable[[], T_Result],
        timeout: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        throttled: typing.Callable[[], T_Result],
        informational: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OperationOutcomeIssueCode.INVALID:
            return invalid()
        if self is OperationOutcomeIssueCode.STRUCTURE:
            return structure()
        if self is OperationOutcomeIssueCode.REQUIRED:
            return required()
        if self is OperationOutcomeIssueCode.VALUE:
            return value()
        if self is OperationOutcomeIssueCode.INVARIANT:
            return invariant()
        if self is OperationOutcomeIssueCode.SECURITY:
            return security()
        if self is OperationOutcomeIssueCode.LOGIN:
            return login()
        if self is OperationOutcomeIssueCode.UNKNOWN:
            return unknown()
        if self is OperationOutcomeIssueCode.EXPIRED:
            return expired()
        if self is OperationOutcomeIssueCode.FORBIDDEN:
            return forbidden()
        if self is OperationOutcomeIssueCode.SUPPRESSED:
            return suppressed()
        if self is OperationOutcomeIssueCode.PROCESSING:
            return processing()
        if self is OperationOutcomeIssueCode.NOT_SUPPORTED:
            return not_supported()
        if self is OperationOutcomeIssueCode.DUPLICATE:
            return duplicate()
        if self is OperationOutcomeIssueCode.MULTIPLE_MATCHES:
            return multiple_matches()
        if self is OperationOutcomeIssueCode.NOT_FOUND:
            return not_found()
        if self is OperationOutcomeIssueCode.DELETED:
            return deleted()
        if self is OperationOutcomeIssueCode.TOO_LONG:
            return too_long()
        if self is OperationOutcomeIssueCode.CODE_INVALID:
            return code_invalid()
        if self is OperationOutcomeIssueCode.EXTENSION:
            return extension()
        if self is OperationOutcomeIssueCode.TOO_COSTLY:
            return too_costly()
        if self is OperationOutcomeIssueCode.BUSINESS_RULE:
            return business_rule()
        if self is OperationOutcomeIssueCode.CONFLICT:
            return conflict()
        if self is OperationOutcomeIssueCode.TRANSIENT:
            return transient()
        if self is OperationOutcomeIssueCode.LOCK_ERROR:
            return lock_error()
        if self is OperationOutcomeIssueCode.NO_STORE:
            return no_store()
        if self is OperationOutcomeIssueCode.EXCEPTION:
            return exception()
        if self is OperationOutcomeIssueCode.TIMEOUT:
            return timeout()
        if self is OperationOutcomeIssueCode.INCOMPLETE:
            return incomplete()
        if self is OperationOutcomeIssueCode.THROTTLED:
            return throttled()
        if self is OperationOutcomeIssueCode.INFORMATIONAL:
            return informational()
