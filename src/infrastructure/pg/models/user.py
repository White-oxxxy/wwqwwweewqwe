from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey

from .base import BaseORM
from .mixins import TimeMixin, IdPkMixin


class RoleORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "roles"  # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    user: Mapped[list["UserORM"]] = relationship(
        back_populates="role", lazy="raise_on_sql"
    )


class UserORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "users"  # noqa

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    role: Mapped["RoleORM"] = relationship(back_populates="user", lazy="raise_on_sql")


class TextORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "texts"  # noqa

    value: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    tags: Mapped[list["TagORM"]] = relationship(
        secondary="tag_text", back_populates="texts", lazy="selectin"
    )


class TagORM(BaseORM, TimeMixin, IdPkMixin):
    __tablename__ = "tags"  # noqa

    name: Mapped[str] = mapped_column(nullable=False)
    uploader_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    texts: Mapped[list["TextORM"]] = relationship(
        secondary="tag_text", back_populates="tags", lazy="selectin"
    )


class TextTagORM(BaseORM, TimeMixin):
    __tablename__ = "tag_text"  # noqa

    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id"), nullable=False, primary_key=True
    )
    text_id: Mapped[int] = mapped_column(
        ForeignKey("texts.id"), nullable=False, primary_key=True
    )
