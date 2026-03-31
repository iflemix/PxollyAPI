import pytest

from pxolly_api import PxollyAPI
from pxolly_api.models.chats import ChatGetByID


@pytest.mark.asyncio
async def test_chats_get_by_id(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.chats.get_by_id("aEacCA", "role")
    assert isinstance(result, ChatGetByID)
