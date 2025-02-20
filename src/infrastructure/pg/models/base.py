from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class BaseORM(DeclarativeBase):

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)