from aiogram import Router
from aiogram.types import Message
from src.lexicon import *


other_router = Router()


@other_router.message()
async def send_answer(message: Message):
    await message.answer(text=AllLexicon.answer_to_another_things.value)
