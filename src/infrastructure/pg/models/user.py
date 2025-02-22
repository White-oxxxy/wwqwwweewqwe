from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey

from src.infrastructure.pg.models.base import BaseORM
from src.infrastructure.pg.models.mixins import TimeMixin, IdPkMixin


class RoleORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "roles" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    users: Mapped[list["UserORM"]] = relationship(back_populates="role")


class UserORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "users" # noqa

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    role: Mapped["RoleORM"] = relationship(back_populates="users")
    tags: Mapped[list["TagORM"]] = relationship(back_populates="user")
    texts: Mapped[list["TextORM"]] = relationship(back_populates="user")


class TextORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "texts" # noqa

    value: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)

    user: Mapped["UserORM"] = relationship(back_populates="text")
    tags: Mapped[list["TagORM"]] = relationship(secondary="tag_text", back_populates="texts")


class TagORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "tags" # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)

    user: Mapped["UserORM"] = relationship(back_populates="tag", uselist=False, secondary="tag_text")
    texts: Mapped[list["TextORM"]] = relationship(secondary="tag_text", back_populates="tags")


class TextTagORM(BaseORM, TimeMixin):
    __tablename__ = "tag_text" # noqa

    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), nullable=False)
    text_id: Mapped[int] = mapped_column(ForeignKey("texts.id"), nullable=False)

    tag: Mapped["TagORM"] = relationship(back_populates="texts")
    text: Mapped["TextORM"] = relationship(back_populates="tags")