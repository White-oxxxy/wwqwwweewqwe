from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.lexicon import *


# ---- клавиатура главного меню ----

admin_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_search.value),
    KeyboardButton(text=AdminLexicon.button_add.value),
    KeyboardButton(text=AllLexicon.button_help.value)
]

admin_menu_kb_builder = ReplyKeyboardBuilder()

admin_menu_kb_builder.row(*admin_menu_buttons, width=3)

admin_menu_kb: ReplyKeyboardMarkup = admin_menu_kb_builder.as_markup(
    one_type_keyboard=True, resize_keyboard=True
)


