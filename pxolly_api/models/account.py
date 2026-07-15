from pydantic import BaseModel

from ..types import AccountTypeOrStr


class AccountGetInfo(BaseModel):
    """Информация о текущем аккаунте"""

    user_id: int
    account_type: AccountTypeOrStr
    vk_added: int
    balance: int
