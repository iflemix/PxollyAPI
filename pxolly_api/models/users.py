from pydantic import BaseModel


class UserRegisteredDate(BaseModel):
    """Дата регистрации пользователя"""

    id: int
    registered: int


class GetUserRegisteredDate(BaseModel):
    """Дата регистрации пользователей"""

    response: list[UserRegisteredDate]

    @classmethod
    def from_response(cls, response: list) -> "GetUserRegisteredDate":
        dates = [UserRegisteredDate(**date) for date in response]
        return cls(response=dates)


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

        free = UserStickerPacksCategory(
            count=response["free"]["count"],
            animated_count=response["free"].get("animated_count"),
            pack_titles=response["free"].get("pack_titles"),
        )

        paid = UserStickerPacksCategory(
            count=response["paid"]["count"],
            animated_count=response["paid"].get("animated_count"),
            pack_titles=response["paid"].get("pack_titles"),
        )

        collectible = UserStickerPacksCategory(
            count=response["collectible"]["count"],
            animated_count=response["collectible"].get("animated_count"),
            pack_titles=response["collectible"].get("pack_titles"),
        )

        return cls(
            name=response["name"],
            total_count=response["total_count"],
            amount=amount,
            free=free,
            paid=paid,
            collectible=collectible,
        )
