import niquests
from niquests import AsyncSession

from .exceptions import ApiError, RequestError, ResponseError


class PxollyAPI:
    """
    Клиент для взаимодействия с API чат менеджера Pxolly
    """

    API_URL = "https://api.pxolly.ru/method"

    def __init__(self, token: str, version: str = "2.5", session: AsyncSession | None = None) -> None:
        """
        :param token: Токен доступа
        :param version: Версия API
        :param session: Сессия niquests.AsyncSession
        """

        self._token = token
        self._version = version
        self._session = session or AsyncSession(base_url=self.API_URL)
        self._base_params = {"v": self._version, "access_token": self._token}

    async def __aenter__(self) -> "PxollyAPI":
        return self

    async def __aexit__(self, type, value, traceback) -> None:
        await self.close()

    async def method(self, method: str, params: dict | None = None) -> dict:
        """
        Выполнить запрос к API

        :param method: Название метода
        :param params: Параметры запроса
        :return: dict
        """

        method_params = params or {}
        finally_params = {**self._base_params, **method_params}
        response = await self._session.get(method, params=finally_params)

        try:
            data: dict = response.json()
            error = data.get("error")
        except niquests.JSONDecodeError as error:
            raise ResponseError(f"Invalid response: {error}")

        if response.status_code in (niquests.codes.not_found, niquests.codes.forbidden):
            raise RequestError(f"Invalid request: {error}")

        if error:
            raise ApiError(
                error["error_code"], error["error_msg"], error.get("error_text"), error.get("request_params")
            )

        return data

    async def execute(self, code: str) -> dict:
        """
        Выполнить несколько запросов к API
        Документация: https://vk.com/app7273656#/dev/method/execute

        :param code: код запросов
        :return: dict
        """

        params = {"code": code}
        return await self.method("execute", params)

    async def close(self) -> None:
        """Закрыть соединение с API"""
        await self._session.close()
