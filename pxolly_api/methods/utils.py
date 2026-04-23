from typing import overload

from ..models.utils import UtilsCheckText, UtilsGetServerTime, UtilsGetServerTimeExtended
from ._base import BaseCategory


class UtilsCategory(BaseCategory):
    """Методы для работы с утилитами"""

    async def check_text(self, text: str, dictionary: str) -> UtilsCheckText:
        """
        Проверить совпадение текста указанному словарю
        Экспериментальный метод, доступ к которому может быть не у всех
        Документация: https://vk.com/app7273656#/dev/method/utils.checkText

        :param text: Текст
        :param dictionary: Название словаря
        """
        params = {"text": text, "dictionary": dictionary}
        response = await self.api.method("utils.checkText", params)
        return UtilsCheckText(response=response["response"])

    @overload
    async def get_server_time(self, extended: bool = False) -> UtilsGetServerTime: ...

    @overload
    async def get_server_time(self, extended: bool = True) -> UtilsGetServerTimeExtended: ...

    async def get_server_time(self, extended: bool = False) -> UtilsGetServerTime | UtilsGetServerTimeExtended:
        """
        Получить время сервера Pxolly
        Документация: https://vk.com/app7273656#/dev/method/utils.getServerTime

        :param extended: Вернуть подробное время
        """
        params = {"extended": extended}
        response = await self.api.method("utils.getServerTime", params)

        if extended:
            return UtilsGetServerTimeExtended(**response["response"])
        else:
            return UtilsGetServerTime(response=response["response"])
