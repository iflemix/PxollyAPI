import typing

if typing.TYPE_CHECKING:
    from ..api import PxollyAPI


class BaseCategory:
    """Базовая категория методов API"""

    def __init__(self, api: "PxollyAPI") -> None:
        self.api = api
