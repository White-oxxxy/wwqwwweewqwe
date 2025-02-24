from functools import lru_cache
from typing import AsyncIterable

from dishka import Provider, AsyncContainer, Scope, make_async_container, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker

from src.infrastructure.repository.user import (
    RoleRepositoryORM,
    UserRepositoryORM,
    TagRepositoryORM,
    TextRepositoryORM,
    TextTagRepositoryORM
)
from src.settings.base import CommonSettings
from src.settings.dev import DevSettings


class CommonProvider(Provider):
    @provide(scope=Scope.APP)
    def create_settings(self) -> CommonSettings:
        return DevSettings()


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_engine(self, settings: CommonSettings) -> AsyncEngine:
        return create_async_engine(url=settings.POSTGRES_URL)

    @provide(scope=Scope.APP)
    async def create_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, autoflush=True)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(self, sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def provide_role_repository(self, session: AsyncSession) -> RoleRepositoryORM:
        repository = RoleRepositoryORM(session=session)
        return repository

    @provide(scope=Scope.REQUEST)
    async def provide_user_repository(self, session: AsyncSession) -> UserRepositoryORM:
        repository = UserRepositoryORM(session=session)
        return repository

    @provide(scope=Scope.REQUEST)
    async def provide_tag_repository(self, session: AsyncSession) -> TagRepositoryORM:
        repository = TagRepositoryORM(session=session)
        return repository

    @provide(scope=Scope.REQUEST)
    async def provide_text_repository(self, session: AsyncSession) -> TextRepositoryORM:
        repository = TextRepositoryORM(session=session)
        return repository

    @provide(scope=Scope.REQUEST)
    async def provide_text_tag_repository(self, session: AsyncSession) -> TextTagRepositoryORM:
        repository = TextTagRepositoryORM(session=session)
        return repository


@lru_cache(1)
def create_container() -> AsyncContainer:
    return make_async_container(
        CommonProvider(), DatabaseProvider(), RepositoryProvider()
    )