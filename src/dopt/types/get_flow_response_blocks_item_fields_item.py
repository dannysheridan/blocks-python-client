# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .get_flow_response_blocks_item_fields_item_boolean import GetFlowResponseBlocksItemFieldsItemBoolean
from .get_flow_response_blocks_item_fields_item_number import GetFlowResponseBlocksItemFieldsItemNumber
from .get_flow_response_blocks_item_fields_item_rich_text import GetFlowResponseBlocksItemFieldsItemRichText
from .get_flow_response_blocks_item_fields_item_string import GetFlowResponseBlocksItemFieldsItemString


class GetFlowResponseBlocksItemFieldsItem_String(GetFlowResponseBlocksItemFieldsItemString):
    type: typing_extensions.Literal["string"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetFlowResponseBlocksItemFieldsItem_Number(GetFlowResponseBlocksItemFieldsItemNumber):
    type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetFlowResponseBlocksItemFieldsItem_Boolean(GetFlowResponseBlocksItemFieldsItemBoolean):
    type: typing_extensions.Literal["boolean"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetFlowResponseBlocksItemFieldsItem_RichText(GetFlowResponseBlocksItemFieldsItemRichText):
    type: typing_extensions.Literal["richText"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


GetFlowResponseBlocksItemFieldsItem = typing.Union[
    GetFlowResponseBlocksItemFieldsItem_String,
    GetFlowResponseBlocksItemFieldsItem_Number,
    GetFlowResponseBlocksItemFieldsItem_Boolean,
    GetFlowResponseBlocksItemFieldsItem_RichText,
]
