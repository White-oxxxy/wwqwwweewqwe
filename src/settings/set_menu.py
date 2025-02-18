from aiogram import Bot
from aiogram.types import BotCommand
from src.lexicon import *

async def set_main_menu(bot: Bot):
    main_menu_commands: list[BotCommand] = [
        BotCommand(command=AllLexicon.command_button_start.value,
                   description=AllLexicon.command_button_start_description.value),
        BotCommand(command=AllLexicon.command_button_help.value,
                   description=AllLexicon.command_button_help_description.value)
    ]

    await bot.set_my_commands(main_menu_commands)