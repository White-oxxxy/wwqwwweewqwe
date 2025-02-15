from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import src.keyboards
import src.lexicon
import src.filters

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['/start'], reply_markup=src.keyboards.user_menu_kb)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['/help'], reply_markup=src.keyboards.user_menu_kb)

@router.message(F.text == src.lexicon.LEXICON_RU['button_help'])
async def process_button_help(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['/help'], reply_markup=src.keyboards.user_back_menu_kb)

@router.message(F.text == src.lexicon.LEXICON_RU['button_menu'])
async def process_button_menu(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['/start'], reply_markup=src.keyboards.user_menu_kb)

@router.message(F.text == src.lexicon.LEXICON_RU['button_search'])
async def process_search(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['answer_search'], reply_markup=src.keyboards.user_search_kb)

@router.message(F.text == src.lexicon.LEXICON_RU['button_tag_list'])
async def process_tag_list(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['answer_db'], reply_markup=src.keyboards.user_back_to_search_kb)

@router.message(F.text == src.lexicon.LEXICON_RU['button_back_to_search'])
async def process_back_to_search(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['answer_search'] ,reply_markup=src.keyboards.user_search_kb)

@router.message(F.text == src.lexicon.LEXICON_RU['button_tag_search'])
async def process_tag_search(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['answer_insert_tag'])

@router.message(F.text == src.lexicon.LEXICON_RU['answer_insert_word'])
async def process_word_search(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['answer_insert_word'])