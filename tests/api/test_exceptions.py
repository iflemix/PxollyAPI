import pytest

from pxolly_api import PxollyAPI
from pxolly_api.exceptions import ApiError, RequestError


@pytest.mark.asyncio
async def test_request_error(pxolly_api: PxollyAPI) -> None:
    with pytest.raises(RequestError):
        await pxolly_api.method("invalid_method")


@pytest.mark.asyncio
async def test_api_error(pxolly_api: PxollyAPI) -> None:
    with pytest.raises(ApiError):
        await pxolly_api.method("chats.getMemberById", {"chat_id": "random_chat_id"})
