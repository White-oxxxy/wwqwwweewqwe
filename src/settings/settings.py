from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class DataBase:
    postgres_db: str
    postgres_user: str
    postgres_password: str
    host_db: str
    port_db: str

@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase

def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DataBase(
            postgres_db=env("POSTGRES_DB"),
            postgres_user=env("POSTGRES_USER"),
            postgres_password=env("POSTGRES_PASSWORD"),
            host_db=env("HOST_DB"),
            port_db=env("PORT_DB")
        )
    )