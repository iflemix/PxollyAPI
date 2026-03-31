from pydantic import BaseModel

from ..enums import AccountType


class AccountGetInfo(BaseModel):
    user_id: int
    account_type: AccountType
    vk_added: int
    balance: int
