import pytest

from pxolly_api import PxollyAPI
from pxolly_api.enums import ChatMemberFilter
from pxolly_api.models.chats import ChatGetMembers, ChatGetMembersById, ChatGetRoles, ChatsGetByID


@pytest.mark.asyncio
async def test_chats_get_by_id(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.chats.get_by_id("eEEAa", "role")
    assert isinstance(result, ChatsGetByID)


@pytest.mark.asyncio
async def test_chats_get_roles(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.chats.get_roles("eEEAa")
    assert isinstance(result, ChatGetRoles)


@pytest.mark.asyncio
async def test_chats_get_members(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.chats.get_members("eEEAa", 100, 0, ChatMemberFilter.ALL)
    assert isinstance(result, ChatGetMembers)


@pytest.mark.asyncio
async def test_chats_get_members_by_id(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.chats.get_members_by_id("eEEAa", "7337723623")
    assert isinstance(result, ChatGetMembersById)
