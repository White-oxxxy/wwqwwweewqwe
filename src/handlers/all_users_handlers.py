from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from src.lexicon import *
from src.keyboards import *

all_users_router = Router()

@all_users_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=AllLexicon.command_start.value, reply_markup=all_users_menu_kb)

@all_users_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=AllLexicon.command_start.command_help.value, reply_markup=all_users_menu_kb)

@all_users_router.message(F.text == AllLexicon.command_start.button_help.value)
async def process_button_help(message: Message):
    await message.answer(text=AllLexicon.command_start.command_help.value, reply_markup=all_users_back_menu_kb)

@all_users_router.message(F.text == AllLexicon.button_menu.value)
async def process_button_menu(message: Message):
    await message.answer(text=AllLexicon.answer_menu.value, reply_markup=all_users_menu_kb)

@all_users_router.message(F.text == AllLexicon.button_search.value)
async def process_search(message: Message):
    await message.answer(text=AllLexicon.answer_search.value, reply_markup=all_users_search_kb)

@all_users_router.message(F.text == AllLexicon.button_tag_list.value)
async def process_tag_list(message: Message):
    await message.answer(text=AllLexicon.answer_db.value, reply_markup=all_users_back_to_search_kb)

@all_users_router.message(F.text == AllLexicon.button_back_to_search.value)
async def process_back_to_search(message: Message):
    await message.answer(text=AllLexicon.answer_search.value, reply_markup=all_users_search_kb)

@all_users_router.message(F.text == AllLexicon.button_tag_search.value)
async def process_tag_search(message: Message):
    await message.answer(text=AllLexicon.answer_insert_tag.value, reply_markup=all_users_back_to_search_kb)

@all_users_router.message(F.text == AllLexicon.button_text_search.value)
async def process_word_search(message: Message):
    await message.answer(text=AllLexicon.answer_insert_word.value, reply_markup=all_users_back_to_search_kb)