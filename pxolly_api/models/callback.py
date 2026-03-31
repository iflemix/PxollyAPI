from pydantic import BaseModel


class CallbackGetSettings(BaseModel):
    """Настройки Callback API текущего аккаунта"""

    enabled: int
    url: str
    secret_key: str
    confirm_code: str


class CallbackGetConfirmationCode(BaseModel):
    """Код подтверждения Callback API"""

    code: str


class CallbackEditSettings(BaseModel):
    """Изменение настроек Callback API"""

    response: dict


class CallbackSetBotPrefix(BaseModel):
    """Установка префикса бота Callback API"""

    response: int
