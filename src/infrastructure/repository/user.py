from sqlalchemy import Result, Select, select
from sqlalchemy.orm import joinedload, selectinload

from infrastructure.pg.models.user import (
    UserORM,
    RoleORM,
    TextORM,
    TagORM,
    TextTagORM,
)
from infrastructure.repository.base import BaseRepositoryORM


class RoleRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> RoleORM | None:
        role: RoleORM | None = await self.session.get(RoleORM, required_id)
        return role

    async def create(self, name: str, uploader_id: int, description: str) -> RoleORM:
        role = RoleORM(name=name, uploader_id=uploader_id, description=description)
        self.session.add(role)

        return role

    async def get_by_name(self, name: str) -> RoleORM | None:
        stmt: Select[tuple[RoleORM]] = (
            select(RoleORM).where(RoleORM.name == name).limit(1)
        )
        role: RoleORM | None = await self.session.scalar(stmt)
        if not role:
            return None

        return role


class UserRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> UserORM | None:
        user: UserORM | None = await self.session.get(UserORM, required_id)

        return user

    async def create(self, user_id: int, username: str, role_id: int) -> UserORM:
        user = UserORM(user_id=user_id, username=username, role_id=role_id)
        self.session.add(user)

        return user

    async def get_by_user_id(self, user_id: int) -> UserORM | None:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.user_id == user_id)
        user: UserORM | None = await self.session.scalar(stmt)
        if not user:
            return None

        return user

    async def get_by_role(self, role_id: int) -> list[UserORM]:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.role_id == role_id)
        result: Result = await self.session.execute(stmt)
        user: list[UserORM] = list(result.scalars().all())

        return user


class TextRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_id)

        return text

    async def create_text(self, value: str, uploader_id: int) -> TextORM:
        text = TextORM(value=value, uploader_id=uploader_id)
        self.session.add(text)
        await self.session.flush()

        return text

    async def create_tag(self, tag: TagORM, text_id: int) -> TextORM:
        stmt: Select[tuple[TextORM]] = select(TextORM).where(TextORM.id == text_id).options(selectinload(TextORM.tags))
        result: Result = await self.session.execute(stmt)
        text: TextORM | None = result.scalars().first()
        if text:
            if tag.id is None:
                self.session.add(tag)
            text.tags.append(tag)
            self.session.add(text)

        return text

    async def get_by_name(self, name: str) -> TagORM | None:
        stmt: Select[tuple[TagORM]] = select(TagORM).where(TagORM.name == name)
        tag: TagORM | None = await self.session.scalar(stmt)
        if not tag:
            return None

        return tag

    async def get_all_tag_names(self) -> list[TagORM.name]:
        stmt: Select[tuple[TagORM.name]] = select(TagORM.name)
        result: Result = await self.session.execute(stmt)
        tags: list[TagORM.name] = list(result.scalars().all())

        return tags


class TextTagRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int): ...

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

    async def get_by_text(self, value: str) -> list[TextORM]:
        stmt = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_id == TextORM.id)
            .filter(TextORM.value.like("%" + value + "%"))
        )
        result = await self.session.execute(stmt)
        text: list[TextORM] = list(result.scalars().all())

        return text
