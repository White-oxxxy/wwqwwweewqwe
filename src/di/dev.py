from functools import lru_cache
from typing import AsyncIterable

from dishka import Provider, AsyncContainer, Scope, make_async_container, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from infrastructure.repository.user import (
    RoleRepositoryORM,
    UserRepositoryORM,
    TextRepositoryORM,
    TextTagRepositoryORM,
)
from settings.base import CommonSettings
from settings.dev import DevSettings


class CommonProvider(Provider):
    @provide(scope=Scope.APP)
    def create_settings(self) -> CommonSettings:
        return DevSettings()


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_async_engine(self, settings: CommonSettings) -> AsyncEngine:
        return create_async_engine(
            url=settings.POSTGRES_URL, isolation_level="READ COMMITTED"
        )

    @provide(scope=Scope.APP)
    async def create_session_maker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, autoflush=True, expire_on_commit=False)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self, create_session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with create_session_maker() as session:
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
    async def provide_text_repository(self, session: AsyncSession) -> TextRepositoryORM:
        repository = TextRepositoryORM(session=session)
        return repository

    @provide(scope=Scope.REQUEST)
    async def provide_text_tag_repository(
        self, session: AsyncSession
    ) -> TextTagRepositoryORM:
        repository = TextTagRepositoryORM(session=session)
        return repository


@lru_cache(1)
def get_container() -> AsyncContainer:
    return make_async_container(
        CommonProvider(), DatabaseProvider(), RepositoryProvider()
    )
