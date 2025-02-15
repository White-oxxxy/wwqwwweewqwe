from aiogram import Router
from aiogram.types import Message

import src.lexicon

router = Router()

@router.message()
async def send_answer(message: Message):
    await message.answer(text=src.lexicon.LEXICON_RU['answer_to_another_things'])

