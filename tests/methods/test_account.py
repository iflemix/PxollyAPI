import pytest

from pxolly_api import PxollyAPI
from pxolly_api.models.account import AccountGetInfo


class TestAccountMethods:
    @pytest.mark.asyncio
    async def test_account_get_info(self, pxolly_api: PxollyAPI) -> None:
        result = await pxolly_api.account.get_info()
        assert isinstance(result, AccountGetInfo)
