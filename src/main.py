import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis
from redis.asyncio import Redis
from src.settings import *
from src.handlers import *


async def main() -> None:
    settings: DevSettings = get_settings()

    redis = Redis(host="localhost")

    storage = RedisStorage(redis=redis)

    bot = Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp = Dispatcher(storage=storage)

    dp.include_router(admin_router)
    dp.include_router(all_users_router)
    dp.include_router(other_router)

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
