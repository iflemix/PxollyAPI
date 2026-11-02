from typing import Any, NotRequired, TypedDict


class ErrorDict(TypedDict):
    error_code: int
    error_msg: str
    error_text: NotRequired[str]
    request_params: NotRequired[list[dict[str, str]]]
    error_subcode: NotRequired[int]
    confirmation_text: NotRequired[str]


class ResponseDict(TypedDict):
    response: dict[str, Any]
    error: NotRequired[ErrorDict]
