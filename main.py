import asyncio

import src.config_data
import src.handlers

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode




async def main() -> None:
    config: src.config_data.Config = src.config_data.load_config()

    bot = Bot(
            token=config.tg_bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp = Dispatcher()

    dp.include_router(src.handlers.admin_handlers.router)
    dp.include_router(src.handlers.user_handlers.router)
    dp.include_router(src.handlers.other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
