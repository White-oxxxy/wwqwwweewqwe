from dataclasses import dataclass

from aiogram.types import Message
from aiogram.filters import BaseFilter

from src.infrastructure.pg.database import database
from src.infrastructure.repository.user import UserRepositoryORM
from src.lexicon.roles import Roles

@dataclass
class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with database.get_session() as session:
            admins = await UserRepositoryORM.get_by_role(session, Roles.admin.value)
        return message.from_user.id in admins


@dataclass
class IsTag(BaseFilter):
    prefix: str = "#"

    async def __call__(self, message: Message) -> bool:
        return message.text[0] == self.prefix
