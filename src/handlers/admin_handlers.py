from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.infrastructure.pg.database import database
from src.fsm import *
from src.keyboards import *
from src.lexicon import *
from src.filters import *


admin_router = Router()


@admin_router.message(
    CommandStart(), IsAdmin, StateFilter(default_state)
)
async def process_command_start(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_start.value, reply_markup=admin_menu_kb
    )


@admin_router.message(
    Command(commands="help"), IsAdmin, StateFilter(default_state)
)
async def process_command_help(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_help.value, reply_markup=admin_menu_kb
    )


@admin_router.message(
    IsAdmin, F.text == AllLexicon.button_menu.value, StateFilter(default_state)
)
async def process_button_menu(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_menu.value, reply_markup=admin_menu_kb
    )


@admin_router.message(
    IsAdmin, F.text == AdminLexicon.button_add.value, StateFilter(default_state)
)
async def process_button_add_text(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMAddForm.insert_tags)
    await message.answer(
        text=AllLexicon.answer_insert_tag.value, reply_markup=all_users_back_menu_kb
    )


@admin_router.message(
    IsAdmin, IsTag(F.text), StateFilter(FSMAddForm.insert_tags)
)
async def process_insert_tag(message: Message, state: FSMContext) -> None:
    await state.update_data(tag=message.text)
    await message.answer(
        text=AllLexicon.answer_insert_word.value, reply_markup=all_users_back_menu_kb
    )
    await state.set_state(FSMAddForm.insert_text)


@admin_router.message(
    IsAdmin, StateFilter(FSMAddForm.insert_tags)
)
async def warning_incorrect_tag(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_if_incorrect_prefix.value, reply_markup=all_users_back_menu_kb
    )


@admin_router.message(
    IsAdmin, StateFilter(FSMAddForm.insert_text), F.text.isalpha()
)
async def process_insert_text(message: Message, state: FSMContext) -> None:
    await state.update_data(text=message.text)
    await message.answer(
        text=AllLexicon.answer_result.value, reply_markup=admin_menu_kb
    )
    await state.clear()