from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class BaseORM(DeclarativeBase):

    id: Mapped[int] = mapped_column(autoincrement=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

