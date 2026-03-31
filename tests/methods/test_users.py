import pytest

from pxolly_api import PxollyAPI
from pxolly_api.models.users import GetUserRegisteredDate, GetUserStickerPacks


@pytest.mark.asyncio
async def test_users_get_registered_date(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.users.get_registered_date("733772362")
    assert isinstance(result, GetUserRegisteredDate)


@pytest.mark.asyncio
async def test_users_get_sticker_packs(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.users.get_sticker_packs("733772362", max_count=30)
    assert isinstance(result, GetUserStickerPacks)
