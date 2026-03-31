from ..enums import ChatMemberFilter
from ..models.chats import (
    ChatBanMember,
    ChatEditTitle,
    ChatGetMembers,
    ChatGetRoles,
    ChatGetRules,
    ChatSendMessage,
    ChatSetMemberRole,
    ChatSetSilenceMode,
    ChatsGetByID,
)
from ._base import BaseCategory


class ChatsCategory(BaseCategory):
    """Методы для работы с чатами"""

    async def ban_member(self, chat_id: str, member_id: int, date: int, reason: str) -> ChatBanMember:
        """
        Выдать бан участнику в чате
        Документация: https://vk.com/app7273656#/dev/method/chats.banMember

        :param chat_id: ID чата
        :param member_id: ID участника
        :param date: Время бана в unixtime
        :param reason: Причина
        """
        params = {"chat_id": chat_id, "member_id": member_id, "date": date, "reason": reason}
        response = await self.api.method("chats.banMember", params)
        return ChatBanMember(response=response["response"])

    async def edit_title(self, chat_id: str, title: str) -> ChatEditTitle:
        """
        Изменить название чата
        Документация: https://vk.com/app7273656#/dev/method/chats.editTitle

        :param chat_id: ID чата
        :param title: Новое название
        """
        params = {"chat_id": chat_id, "title": title}
        response = await self.api.method("chats.editTitle", params)
        return ChatEditTitle(response=response["response"])

    async def get_by_id(self, chat_ids: str, fields: str) -> ChatsGetByID:
        """
        Получить информацию о чатах и участниках
        Документация: https://vk.com/app7273656#/dev/method/chats.getById

        :param chat_ids: ID чатов
        :param fields: Дополнительные поля с информацией
        """
        params = {"chat_ids": chat_ids, "fields": fields}
        response = await self.api.method("chats.getById", params)
        return ChatsGetByID.from_response(response["response"])

    async def get_members(self, chat_id: str, count: int, offset: int, filter: ChatMemberFilter) -> ChatGetMembers:
        """
        Получить участников чата
        Документация: https://vk.com/app7273656#/dev/method/chats.getMembers

        :param chat_id: ID чата
        :param count: Количество участников
        :param offset: Смещение
        :param filter: Фильтр участников
        """
        params = {"chat_id": chat_id, "count": count, "offset": offset, "filter": filter}
        response = await self.api.method("chats.getMembers", params)
        return ChatGetMembers.from_response(response=response["response"])

    async def get_members_by_id(self, chat_id: str, user_ids: str) -> ChatGetMembers:
        """
        Получить участников чата по их ID
        Документация: https://vk.com/app7273656#/dev/method/chats.getMembersById

        :param chat_id: ID чата
        :param user_ids: ID участников
        """
        params = {"chat_id": chat_id, "user_ids": user_ids}
        response = await self.api.method("chats.getMembersById", params)
        return ChatGetMembers.from_response(response=response["response"])

    async def get_roles(self, chat_id: str) -> ChatGetRoles:
        """
        Получить список ролей чата с их приоритетами
        Документация: https://vk.com/app7273656#/dev/method/chats.getRoles

        :param chat_id: ID чата
        """
        params = {"chat_id": chat_id}
        response = await self.api.method("chats.getRoles", params)
        return ChatGetRoles.from_response(response["response"])

    async def get_rules(self, chat_id: str) -> ChatGetRules:
        """
        Получить правила чата
        Документация: https://vk.com/app7273656#/dev/method/chats.getRules

        :param chat_id: ID чата
        """
        params = {"chat_id": chat_id}
        response = await self.api.method("chats.getRules", params)
        return ChatGetRules.from_response(response["response"])

    async def send_message(self, chat_id: str, text: str, random_id: int) -> ChatSendMessage:
        """
        Отправить сообщение в чат
        Документация: https://vk.com/app7273656#/dev/method/chats.sendMessage

        :param chat_id: ID чата
        :param text: Текст сообщения
        :param random_id: уникальный идентификатор сообщения
        """
        params = {"chat_id": chat_id, "text": text, "random_id": random_id}
        response = await self.api.method("chats.sendMessage", params)
        return ChatSendMessage(response=response["response"])

    async def set_member_role(self, chat_id: str, member_id: int, role_id: int) -> ChatSetMemberRole:
        """
        Изменить роль участника в чате
        Документация: https://vk.com/app7273656#/dev/method/chats.setMemberRole

        :param chat_id: ID чата
        :param member_id: ID участника
        :param role_id: приоритет роли
        """
        params = {"chat_id": chat_id, "member_id": member_id, "role_id": role_id}
        response = await self.api.method("chats.setMemberRole", params)
        return ChatSetMemberRole(response=response["response"])

    async def set_silence_mode(self, chat_id: str, time: int) -> ChatSetSilenceMode:
        """
        Установить режим тишины в чате
        Документация: https://vk.com/app7273656#/dev/method/chats.setSilenceMode

        :param chat_id: ID чата
        :param time: Время (-1 включить сообщения, 0 - отключить сообщения, >60 - отключить временно)
        """
        params = {"chat_id": chat_id, "time": time}
        response = await self.api.method("chats.setSilenceMode", params)
        return ChatSetSilenceMode(response=response["response"])
