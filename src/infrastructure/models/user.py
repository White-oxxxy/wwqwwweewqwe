from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey

from src.infrastructure.models.base import BaseORM
from src.infrastructure.models.mixins import TimeMixin


class RoleORM(BaseORM, TimeMixin):

    role_name: Mapped[str] = mapped_column()
    role_description: Mapped[str] = mapped_column()
    upload_time: Mapped[TimeMixin.create_at] = mapped_column()
    update_time: Mapped[TimeMixin.update_at] = mapped_column()

    user_role: Mapped[list["UserORM"]] = relationship(back_populates="role")

class UserORM(BaseORM, TimeMixin):

    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    role_id: Mapped[int] = mapped_column(ForeignKey("RoleORM.__tablename__.id"))
    register_time: Mapped[TimeMixin.create_at] = mapped_column()

    role: Mapped[list["RoleORM"]] = relationship(back_populates="user_role", uselist=False)
    texts: Mapped[list["TextORM"]] = relationship(back_populates="user")

class TextORM(BaseORM, TimeMixin):

    tag: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
    uploader_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("UserORM.__tablename__.id"))
    upload_time: Mapped[TimeMixin.create_at] = mapped_column()
    update_time: Mapped[TimeMixin.update_at] = mapped_column()

    user: Mapped[list["UserORM"]] = relationship(back_populates="texts")