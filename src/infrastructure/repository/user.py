from sqlalchemy import Result, Select, select, BigInteger

from src.infrastructure.pg.models.user import UserORM, RoleORM, TextORM, TagORM, TextTagORM
from src.infrastructure.repository.base import BaseRepositoryORM


class RoleRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> RoleORM | None:
        role: RoleORM | None = await self.session.get(RoleORM, required_id)

        return role

    async def add_role(self, name: str, description: str) -> RoleORM | None:
        role = RoleORM(name=name, description=description)
        self.session.add(role)

        await self.session.commit()
        await self.session.refresh(role)

        return role


class UserRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> UserORM | None:
        user: UserORM | None = await self.session.get(UserORM, required_id)

        return user

    async def add_user(self, user_id: int, username: str, role_id: int) -> UserORM | None:
        role = await self.session.get(RoleORM, role_id)
        if not role:
            raise ValueError("Нет такой роли!")

        user = UserORM(user_id=user_id, username=username, role_id=role_id)
        self.session.add(user)

        await self.session.commit()
        await self.session.refresh(user)

        return user


class TagRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> TagORM | None:
        tag: TagORM | None = await self.session.get(TagORM, required_id)

        return tag

    async def add_tag(self, name: str, uploader_id: int) -> TagORM | None:
        tag = await self.session.get(TagORM, name)
        if tag:
            raise ValueError("Такой тэг уже есть!")

        tag = TagORM(name=name, uploader_id=uploader_id)
        self.session.add(tag)

        await self.session.commit()
        await self.session.refresh(tag)

        return tag


class TextRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_id)

        return text

    async def add_text(self, value: str, uploader_id: int) -> TextORM | None:
        text = await self.session.get(TextORM, value)
        if text:
            raise ValueError("Такой текст уже добавлен")

        text = TextORM(value=value, uploader_id=uploader_id)
        self.session.add(text)

        await self.session.commit()
        await self.session.refresh(text)

        return text


class TextTagRepositoryORM:
    async def get_by_tag(self):
        pass

    async def get_by_text(self):
        pass