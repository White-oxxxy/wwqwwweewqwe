from typing import AsyncIterable

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from settings import *

settings: DevSettings = get_settings()


class Database:
    def __init__(self, url: str, ro_url: str) -> None:
        self.async_engine: AsyncEngine = create_async_engine(
            url=url, echo=False, isolation_level="READ COMMITTED"
        )

        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.async_engine, autoflush=False, expire_on_commit=False
        )

        self.read_only_async_engine: AsyncEngine = create_async_engine(
            url=ro_url, echo=False, isolation_level="AUTOCOMMIT"
        )

        self.read_only_session_maker: async_sessionmaker[AsyncSession] = (
            async_sessionmaker(bind=self.read_only_async_engine, expire_on_commit=False)
        )

    async def get_session(self) -> AsyncIterable[AsyncSession]:
        async with self.session_maker() as session:
            try:
                yield session
            except SQLAlchemyError:
                await session.rollback()

    async def read_only_get_session(self) -> AsyncIterable[AsyncSession]:
        async with self.read_only_session_maker() as session:
            try:
                yield session
            except SQLAlchemyError:
                await session.rollback()
                raise
            finally:
                await session.close()
