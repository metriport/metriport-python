# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StructureMapTargetTransform(str, enum.Enum):
    """
    How the data is copied / created.
    """

    CREATE = "create"
    COPY = "copy"
    TRUNCATE = "truncate"
    ESCAPE = "escape"
    CAST = "cast"
    APPEND = "append"
    TRANSLATE = "translate"
    REFERENCE = "reference"
    DATE_OP = "dateOp"
    UUID = "uuid"
    POINTER = "pointer"
    EVALUATE = "evaluate"
    CC = "cc"
    C = "c"
    QTY = "qty"
    ID = "id"
    CP = "cp"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        copy: typing.Callable[[], T_Result],
        truncate: typing.Callable[[], T_Result],
        escape: typing.Callable[[], T_Result],
        cast: typing.Callable[[], T_Result],
        append: typing.Callable[[], T_Result],
        translate: typing.Callable[[], T_Result],
        reference: typing.Callable[[], T_Result],
        date_op: typing.Callable[[], T_Result],
        uuid: typing.Callable[[], T_Result],
        pointer: typing.Callable[[], T_Result],
        evaluate: typing.Callable[[], T_Result],
        cc: typing.Callable[[], T_Result],
        c: typing.Callable[[], T_Result],
        qty: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        cp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StructureMapTargetTransform.CREATE:
            return create()
        if self is StructureMapTargetTransform.COPY:
            return copy()
        if self is StructureMapTargetTransform.TRUNCATE:
            return truncate()
        if self is StructureMapTargetTransform.ESCAPE:
            return escape()
        if self is StructureMapTargetTransform.CAST:
            return cast()
        if self is StructureMapTargetTransform.APPEND:
            return append()
        if self is StructureMapTargetTransform.TRANSLATE:
            return translate()
        if self is StructureMapTargetTransform.REFERENCE:
            return reference()
        if self is StructureMapTargetTransform.DATE_OP:
            return date_op()
        if self is StructureMapTargetTransform.UUID:
            return uuid()
        if self is StructureMapTargetTransform.POINTER:
            return pointer()
        if self is StructureMapTargetTransform.EVALUATE:
            return evaluate()
        if self is StructureMapTargetTransform.CC:
            return cc()
        if self is StructureMapTargetTransform.C:
            return c()
        if self is StructureMapTargetTransform.QTY:
            return qty()
        if self is StructureMapTargetTransform.ID:
            return id()
        if self is StructureMapTargetTransform.CP:
            return cp()
