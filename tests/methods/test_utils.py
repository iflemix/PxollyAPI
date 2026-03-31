import pytest

from pxolly_api import PxollyAPI
from pxolly_api.models.utils import UtilsGetServerTime, UtilsGetServerTimeExtended


@pytest.mark.asyncio
async def test_utils_get_server_time(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.utils.get_server_time()
    assert isinstance(result, UtilsGetServerTime)


@pytest.mark.asyncio
async def test_utils_get_server_time_extended(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.utils.get_server_time(extended=True)
    assert isinstance(result, UtilsGetServerTimeExtended)
