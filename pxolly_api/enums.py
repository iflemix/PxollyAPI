from enum import StrEnum


class AccountType(StrEnum):
    """Типы аккаунтов пользователей"""

    BOT = "bot"
    RAIDBOT = "raidbot"
    FLOODER = "flooder"
    SPAMMER = "spammer"
    DEFAULT = "default"
    UNKNOWN = "unknown"


class DatabaseID(StrEnum):
    """Идентификаторы баз данных"""

    IRIS = "iris"


class ChatMemberStatus(StrEnum):
    """Статус участника чата"""

    KICKED = "kicked"
    BANNED = "banned"
    LEFT = "left"
    IN = "in"


class ChatMemberFilter(StrEnum):
    """Фильтр участников чата"""

    ALL = "all"
    BANNED = "banned"
    MUTED = "muted"


class FormattingEntityType(StrEnum):
    """Типы форматирования текста"""

    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    URL = "url"
