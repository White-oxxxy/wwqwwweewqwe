from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, as_declarative


@as_declarative()
class BaseORM(DeclarativeBase):

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)