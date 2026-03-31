from ..models.users import GetUserRegisterdDate, GetUserStickerPacks
from ._base import BaseCategory


class UsersCategory(BaseCategory):
    """Методы для работы с пользователями"""

    async def get_registered_date(self, user_ids: str) -> GetUserRegisterdDate:
        """
        Получить дату регистрации пользователей
        Документация: https://vk.com/app7273656#/dev/method/users.getRegisteredDate

        :param user_ids: ID пользователей
        """
        params = {"user_ids": user_ids}
        response = await self.api.method("users.getRegisteredDate", params)
        return GetUserRegisterdDate(**response["response"])

    async def get_sticker_packs(self, user_id: int, max_count: int, need_titles: bool = False) -> GetUserStickerPacks:
        """
        Получить список стикер паков пользователя
        Документация: https://vk.com/app7273656#/dev/method/users.getStickerPacks

        :param user_id: ID пользователя
        :param max_count: Максимальное количество паков
        :param need_titles: Получить названия пакетов
        """
        params = {"user_id": user_id, "max_count": max_count, "need_titles": need_titles}
        response = await self.api.method("users.getStickerPacks", params)
        return GetUserStickerPacks.from_response(response=response["response"])
