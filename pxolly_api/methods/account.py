from ..models.account import AccountGetInfo
from ._base import BaseCategory


class AccountCategory(BaseCategory):
    """Методы для работы с аккаунтом"""

    async def get_info(self) -> AccountGetInfo:
        """
        Получить информацию о текущем аккаунте
        Документация: https://vk.com/app7273656#/dev/method/account.getInfo
        """
        response = await self.api.method("account.getInfo")
        return AccountGetInfo(**response["response"])
