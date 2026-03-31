import pytest

from pxolly_api import PxollyAPI
from pxolly_api.models.callback import CallbackGetConfirmationCode, CallbackGetSettings, CallbackSetBotPrefix


@pytest.mark.asyncio
async def test_callback_get_settings(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.callback.get_settings()
    assert isinstance(result, CallbackGetSettings)


@pytest.mark.asyncio
async def test_callback_get_confirmation_code(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.callback.get_confirmation_code()
    assert isinstance(result, CallbackGetConfirmationCode)


@pytest.mark.asyncio
async def test_callback_set_bot_prefix(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.callback.set_bot_prefix("!")
    assert isinstance(result, CallbackSetBotPrefix)
