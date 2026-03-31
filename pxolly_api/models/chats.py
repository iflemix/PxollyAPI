from pydantic import BaseModel

from ..enums import ChatMemberStatus, FormattingEntityType


class ChatBanMember(BaseModel):
    response: int


class ChatEditTitle(BaseModel):
    response: int


class ChatGetByID(BaseModel):
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
    max_warns: int


class ChatMember(BaseModel):
    id: int
    role: int
    immune: int | None
    status: ChatMemberStatus
    warns: int | None
    messages: int
    ban_expire: int | None
    mute_expire: int | None


class ChatGetMembers(BaseModel):
    response: list[ChatMember]

    @classmethod
    def from_response(cls, response: dict) -> "ChatGetMembers":
        members = [ChatMember(**member) for member in response]
        return cls(response=members)


class ChatRole(BaseModel):
    name: str
    role_id: str


class ChatGetRoles(BaseModel):
    response: list[ChatRole]

    @classmethod
    def from_response(cls, response: dict) -> "ChatGetRoles":
        roles = [ChatRole(**role) for role in response]
        return cls(response=roles)


class ChatFormattingEntity(BaseModel):
    type: FormattingEntityType
    offset: int
    length: int
    url: str = None


class ChatGetRules(BaseModel):
    text: str
    entities: list[ChatFormattingEntity]
    owner_id: int

    @classmethod
    def from_response(cls, response: dict) -> "ChatGetRules":
        entities = [ChatFormattingEntity(**entity) for entity in response["entities"]]
        return cls(text=response["text"], entities=entities, owner_id=response["owner_id"])


class ChatSendMessage(BaseModel):
    response: int


class ChatSetMemberRole(BaseModel):
    response: int


class ChatSetSilenceMode(BaseModel):
    response: int
