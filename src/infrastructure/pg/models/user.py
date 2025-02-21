from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey

from src.infrastructure.pg.models.base import BaseORM
from src.infrastructure.pg.models.mixins import TimeMixin


class RoleORM(BaseORM, TimeMixin):
    __tablename__ = "roles" # noqa

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    user: Mapped["UserORM"] = relationship(back_populates="role", uselist=False)


class UserORM(BaseORM, TimeMixin):
    __tablename__ = "users" # noqa

    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    role: Mapped["RoleORM"] = relationship(back_populates="user", uselist=False)
    tag: Mapped[list["TagORM"]] = relationship(back_populates="user")
    text: Mapped[list["TextORM"]] = relationship(back_populates="user")


class TextORM(BaseORM, TimeMixin):
    __tablename__ = "texts" # noqa

    value: Mapped[str] = mapped_column()
    uploader_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))

    user: Mapped[list["UserORM"]] = relationship(back_populates="text")
    texttag: Mapped["TextTagORM"] = relationship(back_populates="text", uselist=False) # noqa


class TagORM(BaseORM, TimeMixin):
    __tablename__ = "tags" # noqa

    name: Mapped[str] = mapped_column()
    uploader_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))

    user: Mapped[list["UserORM"]] = relationship(back_populates="tag")
    textag: Mapped["TextTagORM"] = relationship(back_populates="tag", uselist=False) # noqa


class TextTagORM(BaseORM, TimeMixin):
    __tablename__ = "tagtext" # noqa

    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))
    text_id: Mapped[int] = mapped_column(ForeignKey("texts.id"))

    tag: Mapped["TagORM"] = relationship(back_populates="texttag", uselist=False) # noqa
    text: Mapped["TextORM"] = relationship(back_populates="texttag", uselist=False) # noqa