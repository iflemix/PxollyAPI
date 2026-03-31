import pytest

from pxolly_api import PxollyAPI
from pxolly_api.models.account import AccountGetInfo


@pytest.mark.asyncio
async def test_account_get_info(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.account.get_info()
    assert isinstance(result, AccountGetInfo)
