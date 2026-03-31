from pydantic import BaseModel


class UtilsGetServerTimeExtended(BaseModel):
    """Расширенное время сервера Pxolly"""

    seconds: int
    milliseconds: int


class UtilsGetServerTime(BaseModel):
    """Время сервера Pxolly"""

    response: int


class UtilsCheckText(BaseModel):
    """Совпадение текста словарю"""

    response: float
