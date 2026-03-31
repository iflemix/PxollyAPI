from ..models.callback import (
    CallbackEditSettings,
    CallbackGetConfirmationCode,
    CallbackGetSettings,
    CallbackSetBotPrefix,
)
from ._base import BaseCategory


class CallbackCategory(BaseCategory):
    """Методы для работы с Callback API сервером"""

    async def get_settings(self) -> CallbackGetSettings:
        """
        Получить настройки Callback API текущего аккаунта
        Документация: https://vk.com/app7273656#/dev/method/callback.getSettings
        """
        response = await self.api.method("callback.getSettings")
        return CallbackGetSettings(**response["response"])

    async def get_confirmation_code(self) -> CallbackGetConfirmationCode:
        """
        Получить код для подтверждения Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.getConfirmationCode
        """
        response = await self.api.method("callback.getConfirmationCode")
        return CallbackGetConfirmationCode(**response["response"])

    async def edit_settings(self, url: str, secret_key: str, is_hidden: bool) -> CallbackEditSettings:
        """
        Изменить настройки Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.editSettings

        :param url: Ссылка на Callback API
        :param secret_key: Секретный ключ
        :param is_hidden: Скрыть адрес сервера Callback API
        """
        params = {"url": url, "secret_key": secret_key, "is_hidden": is_hidden}
        response = await self.api.method("callback.editSettings", params)
        return CallbackEditSettings(response=response["response"])

    async def set_bot_prefix(self, prefix: str) -> CallbackSetBotPrefix:
        """
        Установить префикс бота для Callback API
        Документация: https://vk.com/app7273656#/dev/method/callback.setBotPrefix

        :param prefix: Префикс
        """
        params = {"prefix": prefix}
        response = await self.api.method("callback.setBotPrefix", params)
        return CallbackSetBotPrefix(response=response["response"])
