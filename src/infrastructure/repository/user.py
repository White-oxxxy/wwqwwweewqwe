from sqlalchemy import Result, Select, select, BigInteger
from sqlalchemy.orm import joinedload, subqueryload

from src.infrastructure.pg.models.user import UserORM, RoleORM, TextORM, TagORM, TextTagORM
from src.infrastructure.repository.base import BaseRepositoryORM


class RoleRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> RoleORM | None:
        role: RoleORM | None = await self.session.get(RoleORM, required_id)

        return role

    async def add_role(self, name: str, description: str) -> RoleORM | None:
        stmt: Select[tuple[RoleORM]] = select(RoleORM).where(RoleORM.name == name)
        result: Result = await self.session.execute(stmt)
        role: RoleORM | None = result.scalars().one_or_none()

        if role:
            raise ValueError("Такая роль уже есть!")

        role: RoleORM = RoleORM(name=name, description=description)
        self.session.add(role)

        await self.session.commit()
        await self.session.refresh(role)

        return role

    async def get_by_name(self, name: str) -> RoleORM | None:
        stmt: Select[tuple[RoleORM]] = select(RoleORM).where(RoleORM.name == name)
        result: Result = await self.session.execute(stmt)
        role: RoleORM | None = result.scalars().one_or_none()

        return role


class UserRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> UserORM | None:
        user: UserORM | None = await self.session.get(UserORM, required_id)

        return user

    async def add_user(self, user_id: int, username: str, role_id: int) -> UserORM | None:
        stmt: Select[tuple[RoleORM]] = select(RoleORM).where(RoleORM.id == role_id)
        result: Result = await self.session.execute(stmt)
        role: RoleORM | None = result.scalars().one_or_none()
        if not role:
            raise ValueError("Нет такой роли!")

        user: UserORM = UserORM(user_id=user_id, username=username, role_id=role_id)
        self.session.add(user)

        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def get_by_user_id(self, user_id: int) -> UserORM | None:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.user_id == user_id)
        result: Result = await self.session.execute(stmt)
        user: UserORM | None = result.scalars().one_or_none()

        return user

    async def get_by_username(self, username: str) -> UserORM | None:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.username == username)
        result: Result = await self.session.execute(stmt)
        user: UserORM | None = result.scalars().one_or_none()

        return user


class TagRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> TagORM | None:
        tag: TagORM | None = await self.session.get(TagORM, required_id)

        return tag

    async def add_tag(self, name: str, uploader_id: int) -> TagORM | None:
        stmt: Select[tuple[TagORM]] = select(TagORM).where(TagORM.name == name)
        result: Result = await self.session.execute(stmt)
        tag: TagORM | None = result.scalars().one_or_none()

        if tag:
            raise ValueError("Такой тэг уже есть!")

        tag: TagORM = TagORM(name=name, uploader_id=uploader_id)
        self.session.add(tag)

        await self.session.commit()
        await self.session.refresh(tag)

        return tag

    async def get_by_tag(self, name: str) -> TagORM | None:
        stmt: Select[tuple[TagORM]] = select(TagORM).where(TagORM.name == name)
        result: Result = await self.session.execute(stmt)
        tag: TagORM | None = result.scalars().one_or_none()

        return tag


class TextRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_id)

        return text

    async def add_text(self, value: str, uploader_id: int) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = select(TextORM).where(TextORM.value == value)
        result: Result = await self.session.execute(stmt)
        text: TextORM | None = result.scalars().one_or_none()
        if text:
            raise ValueError("Такой текст уже добавлен")

        text: TextORM = TextORM(value=value, uploader_id=uploader_id)
        self.session.add(text)

        await self.session.commit()
        await self.session.refresh(text)

        return text

    async def get_by_value(self, value: str) -> TextORM | None:
        ...
        # в разработке


class TextTagRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int):
        ...

    async def get_by_tag(self, name: str) -> list[TextORM] | None:
        stmt = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_id == TextORM.id)
            .join(TagORM, TextTagORM.tag_id == TagORM.id)
            .where(TagORM.name == name)
            .options(joinedload(TextORM.tags))
            )
        result = await self.session.execute(stmt)
        text: list[TextORM] = list(result.scalars().all())

        return text

    async def get_by_text(self):
        ...
        # в разработке