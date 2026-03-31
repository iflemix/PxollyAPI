from pydantic import BaseModel

from ..enums import ChatMemberStatus, FormattingEntityType


class ChatBanMember(BaseModel):
    """Бан участника в чате"""

    response: int


class ChatEditTitle(BaseModel):
    """Изменение названия чата"""

    response: int


class Chat(BaseModel):
    """Чат"""

    id: str
    title: str
    photo: str | None
    members_count: int | None
    is_gold: int
    owner_id: int
    admin_ids: list[int] | None
    bot_ids: list[int] | None
    role: int | None
    immune: int | None
    warns: int | None
    max_warns: int | None


class ChatsGetByID(BaseModel):
    """Чаты"""

    response: list[Chat]

    @classmethod
    def from_response(cls, response: dict) -> "ChatsGetByID":
        chats = [
            Chat(
                id=chat["id"],
                title=chat["title"],
                photo=chat.get("photo"),
                members_count=chat.get("members_count"),
                is_gold=chat["is_gold"],
                owner_id=chat["owner_id"],
                admin_ids=chat.get("admin_ids"),
                bot_ids=chat.get("bot_ids"),
                role=chat.get("role"),
                immune=chat.get("immune"),
                warns=chat.get("warns"),
                max_warns=chat.get("max_warns"),
            )
            for chat in response
        ]
        return cls(response=chats)


class ChatMember(BaseModel):
    """Участник чата"""

    id: int
    role: int
    immune: int | None
    status: ChatMemberStatus
    warns: int | None
    messages: int
    ban_expire: int | None
    mute_expire: int | None


class ChatMemberAccount(BaseModel):
    """Аккаунт участника чата"""

    id: int
    name: str
    sex: int
    photo_200: str
    screen_name: str


class ChatGetMembersById(BaseModel):
    """Участники чата"""

    response: list[ChatMember]

    @classmethod
    def from_response(cls, response: list) -> "ChatGetMembersById":
        members = [
            ChatMember(
                id=member["id"],
                role=member["role"],
                immune=member.get("immune"),
                status=member["status"],
                warns=member.get("warns"),
                messages=member["messages"],
                ban_expire=member.get("ban_expire"),
                mute_expire=member.get("mute_expire"),
            )
            for member in response
        ]
        return cls(response=members)


class ChatGetMembers(BaseModel):
    """Участники чата"""

    count: int
    items: list[ChatMember]
    accounts: list[ChatMemberAccount]

    @classmethod
    def from_response(cls, response: dict) -> "ChatGetMembers":
        members = [
            ChatMember(
                id=member["id"],
                role=member["role"],
                immune=member.get("immune"),
                status=member["status"],
                warns=member.get("warns"),
                messages=member["messages"],
                ban_expire=member.get("ban_expire"),
                mute_expire=member.get("mute_expire"),
            )
            for member in response["items"]
        ]
        accounts = [ChatMemberAccount(**account) for account in response["accounts"]]
        return cls(count=response["count"], items=members, accounts=accounts)


class ChatRole(BaseModel):
    """Роль чата"""

    name: str
    role_id: str


class ChatGetRoles(BaseModel):
    """Роли чата"""

    response: list[ChatRole]

    @classmethod
    def from_response(cls, response: dict) -> "ChatGetRoles":
        roles = [ChatRole(**role) for role in response]
        return cls(response=roles)


class ChatFormattingEntity(BaseModel):
    """Формат текста"""

    type: FormattingEntityType
    offset: int
    length: int
    url: str = None


class ChatGetRules(BaseModel):
    """Правила чата"""

    text: str
    entities: list[ChatFormattingEntity]
    owner_id: int

    @classmethod
    def from_response(cls, response: dict) -> "ChatGetRules":
        entities = [ChatFormattingEntity(**entity) for entity in response["entities"]]
        return cls(text=response["text"], entities=entities, owner_id=response["owner_id"])


class ChatSendMessage(BaseModel):
    """Отправка сообщения в чат"""

    response: int


class ChatSetMemberRole(BaseModel):
    """Установка роли участника чата"""

    response: int


class ChatSetSilenceMode(BaseModel):
    """Установка режима тишины чата"""

    response: int
