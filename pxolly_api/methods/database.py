from ..enums import DatabaseID
from ..models.database import DatabaseGet
from ._base import BaseCategory


class DatabaseCategory(BaseCategory):
    """Методы для работы с базами данных"""

    async def get(
        self,
        database_id: DatabaseID,
        user_ids: str,
        allow_fakes: bool,
        key: str | None = None,
    ) -> DatabaseGet:
        """
        Получить данные из базы данных
        Документация: https://vk.com/app7273656#/dev/method/database.get

        :param database_id: ID базы данных
        :param user_ids: ID пользователей
        :param allow_fakes: Разрешить использование фейковых данных
        :param key: Ключ для снятия ограничений
        """
        params = {"database_id": database_id, "user_ids": user_ids, "allow_fakes": allow_fakes, "key": key}
        response = await self.api.method("database.get", params)
        return DatabaseGet.from_response(response=response["response"], database_id=database_id)
