# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ImplementationGuideParameterCode(str, enum.Enum):
    """
    apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.
    """

    APPLY = "apply"
    PATH_RESOURCE = "path-resource"
    PATH_PAGES = "path-pages"
    PATH_TX_CACHE = "path-tx-cache"
    EXPANSION_PARAMETER = "expansion-parameter"
    RULE_BROKEN_LINKS = "rule-broken-links"
    GENERATE_XML = "generate-xml"
    GENERATE_JSON = "generate-json"
    GENERATE_TURTLE = "generate-turtle"
    HTML_TEMPLATE = "html-template"

    def visit(
        self,
        apply: typing.Callable[[], T_Result],
        path_resource: typing.Callable[[], T_Result],
        path_pages: typing.Callable[[], T_Result],
        path_tx_cache: typing.Callable[[], T_Result],
        expansion_parameter: typing.Callable[[], T_Result],
        rule_broken_links: typing.Callable[[], T_Result],
        generate_xml: typing.Callable[[], T_Result],
        generate_json: typing.Callable[[], T_Result],
        generate_turtle: typing.Callable[[], T_Result],
        html_template: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImplementationGuideParameterCode.APPLY:
            return apply()
        if self is ImplementationGuideParameterCode.PATH_RESOURCE:
            return path_resource()
        if self is ImplementationGuideParameterCode.PATH_PAGES:
            return path_pages()
        if self is ImplementationGuideParameterCode.PATH_TX_CACHE:
            return path_tx_cache()
        if self is ImplementationGuideParameterCode.EXPANSION_PARAMETER:
            return expansion_parameter()
        if self is ImplementationGuideParameterCode.RULE_BROKEN_LINKS:
            return rule_broken_links()
        if self is ImplementationGuideParameterCode.GENERATE_XML:
            return generate_xml()
        if self is ImplementationGuideParameterCode.GENERATE_JSON:
            return generate_json()
        if self is ImplementationGuideParameterCode.GENERATE_TURTLE:
            return generate_turtle()
        if self is ImplementationGuideParameterCode.HTML_TEMPLATE:
            return html_template()
