from aiogram import F, Router
from aiogram.filters import Command, CommandStart, and_f
from aiogram.types import Message

from src.keyboards import *
from src.lexicon import *
from src.filters import *
from src.settings import *

config: Config = load_config()

admin_router = Router()

@admin_router.message(CommandStart(), IsAdmin(config.tg_bot.admin_ids))
async def process_command_start(message: Message):
    await message.answer(AllLexicon.command_start.value, reply_markup=admin_menu_kb)

@admin_router.message(IsAdmin(config.tg_bot.admin_ids), F.text == AllLexicon.button_menu.value)
async def process_button_menu(message: Message):
    await message.answer(AllLexicon.answer_menu.value, reply_markup=admin_menu_kb)

@admin_router.message(IsAdmin(config.tg_bot.admin_ids), F.text == AdminLexicon.button_add.value)
async def process_button_add_text(message: Message):
    await message.answer(AllLexicon.answer_insert_tag.value, reply_markup=all_users_back_menu_kb)



