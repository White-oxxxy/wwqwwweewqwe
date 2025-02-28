from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.fsm import *
from src.keyboards import *
from src.lexicon import *
from src.filters import *
from src.settings import *


settings: DevSettings = get_settings()

admin_router = Router()


@admin_router.message(
    CommandStart(), IsAdmin(settings.ADMIN_IDS), StateFilter(default_state)
)
async def process_command_start(message: Message):
    await message.answer(AllLexicon.answer_start.value, reply_markup=admin_menu_kb)


@admin_router.message(
    Command(commands="help"), IsAdmin(settings.ADMIN_IDS), StateFilter(default_state)
)
async def process_command_help(message: Message):
    await message.answer(AllLexicon.answer_help.value, reply_markup=admin_menu_kb)


@admin_router.message(
    IsAdmin(settings.ADMIN_IDS), F.text == AllLexicon.button_menu.value
)
async def process_button_menu(message: Message):
    await message.answer(AllLexicon.answer_menu.value, reply_markup=admin_menu_kb)


@admin_router.message(
    IsAdmin(settings.ADMIN_IDS), F.text == AdminLexicon.button_add.value
)
async def process_button_add_text(message: Message):
    await message.answer(
        AllLexicon.answer_insert_tag.value, reply_markup=all_users_back_menu_kb
    )
