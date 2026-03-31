from pydantic import BaseModel


class GetUserRegisterdDate(BaseModel):
    """Дата регистрации пользователя"""

    id: int
    registered: int


class UserStickerPacksCategory(BaseModel):
    """Категория стикерпаков пользователя"""

    count: int
    animated_count: int | None
    pack_titles: list[str] | None


class UserStickerPacksAmount(BaseModel):
    """Цена стикерпаков пользователя"""

    rubles: int
    vk_votes: int


class GetUserStickerPacks(BaseModel):
    """Стикерпаки пользователя"""

    name: str
    total_count: int
    amount: UserStickerPacksAmount
    free: UserStickerPacksCategory
    paid: UserStickerPacksCategory
    collectible: UserStickerPacksCategory

    @classmethod
    def from_response(cls, response: dict) -> "GetUserStickerPacks":
        amount = UserStickerPacksAmount(**response["amount"])
        free = UserStickerPacksCategory(**response["free"])
        paid = UserStickerPacksCategory(**response["paid"])
        collectible = UserStickerPacksCategory(**response["collectible"])

        return cls(
            name=response["name"],
            total_count=response["total_count"],
            amount=amount,
            free=free,
            paid=paid,
            collectible=collectible,
        )
