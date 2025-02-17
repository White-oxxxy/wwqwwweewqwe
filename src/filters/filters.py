from dataclasses import dataclass

from aiogram.types import Message
from aiogram.filters import BaseFilter

@dataclass
class IsAdmin(BaseFilter):
    admins_ids: list[int]

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_ids

@dataclass
class IsTag(BaseFilter):
    prefix: str = '#'

    async def __call__(self, message: Message) -> bool:
        return message.text[0] == self.prefix

