from typing import AsyncIterable
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker


class Database:
    def __init__(self, url: str) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=False,
            pool_size=10,
            max_overflow=5,
            pool_timeout=30,
            pool_recycle=1800
        )
        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=True,
            expire_on_commit=True
        )

    async def get_session(self) -> AsyncIterable[AsyncSession]:
        async with self.session_maker() as session:
            yield session
