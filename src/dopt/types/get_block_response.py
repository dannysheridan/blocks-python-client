# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .get_block_response_fields_item import GetBlockResponseFieldsItem
from .get_block_response_state import GetBlockResponseState
from .get_block_response_type import GetBlockResponseType


class GetBlockResponse(pydantic.BaseModel):
    kind: typing_extensions.Literal["block"]
    uid: str
    sid: str
    version: float
    state: GetBlockResponseState
    container_uid: typing.Optional[str] = pydantic.Field(alias="containerUid")
    transitioned: typing.Dict[str, bool]
    type: GetBlockResponseType
    fields: typing.List[GetBlockResponseFieldsItem]

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
