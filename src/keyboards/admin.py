from dataclasses import dataclass

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import *

@dataclass
class AdminKeyboards:
    @staticmethod
    def create_admin_menu_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_search.value),
            KeyboardButton(text=AdminLexicon.button_add.value),
            KeyboardButton(text=AllLexicon.button_help.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(
            *buttons, width=3
        )
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb

