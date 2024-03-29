# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ElementDefinitionRepresentationItem(str, enum.Enum):
    XML_ATTR = "xmlAttr"
    XML_TEXT = "xmlText"
    TYPE_ATTR = "typeAttr"
    CDA_TEXT = "cdaText"
    XHTML = "xhtml"

    def visit(
        self,
        xml_attr: typing.Callable[[], T_Result],
        xml_text: typing.Callable[[], T_Result],
        type_attr: typing.Callable[[], T_Result],
        cda_text: typing.Callable[[], T_Result],
        xhtml: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ElementDefinitionRepresentationItem.XML_ATTR:
            return xml_attr()
        if self is ElementDefinitionRepresentationItem.XML_TEXT:
            return xml_text()
        if self is ElementDefinitionRepresentationItem.TYPE_ATTR:
            return type_attr()
        if self is ElementDefinitionRepresentationItem.CDA_TEXT:
            return cda_text()
        if self is ElementDefinitionRepresentationItem.XHTML:
            return xhtml()
