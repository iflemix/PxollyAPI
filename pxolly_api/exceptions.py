class PxollyException(Exception):
    """Общий класс всех исключений"""


class ResponseError(PxollyException):
    """Ошибка при обработке ответа от API"""


class RequestError(PxollyException):
    """Ошибка при неправильном запросе к API"""


class ApiError(PxollyException):
    """Ошибка API при выполнении запроса"""

    def __init__(
        self,
        error_code: int,
        error_msg: str,
        error_text: str | None = None,
        request_params: dict | None = None,
    ) -> None:
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_text = error_text
        self.request_params = request_params

    def __str__(self) -> str:
        return f"{self.error_code} ({self.error_msg})"
