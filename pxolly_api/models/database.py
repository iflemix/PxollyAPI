from pydantic import BaseModel

from ..enums import DatabaseID


class DatabaseGetIrisMember(BaseModel):
    """Участник базы данных Iris"""

    user_id: int
    last_banned: int
    spam_count: int | None
    text: str | None
    is_fake: int | None
    comment: str | None


class DatabaseGetIris(BaseModel):
    """База данных Iris"""

    count: int
    items: list[DatabaseGetIrisMember]


class DatabaseGet(BaseModel):
    """База данных"""

    response: DatabaseGetIris

    @classmethod
    def from_response(cls, response: dict, database_id: DatabaseID) -> "DatabaseGet":
        if database_id == DatabaseID.IRIS:
            members = [DatabaseGetIrisMember(**member) for member in response["items"]]
            response_model = DatabaseGetIris(count=response["count"], items=members)

        return cls(response=response_model)
