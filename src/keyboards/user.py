from dataclasses import dataclass

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.admin import AdminKeyboards
from lexicon import *


@dataclass
class UserKeyboards(AdminKeyboards):
    @staticmethod
    def create_user_menu_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_search.value),
            KeyboardButton(text=AllLexicon.button_help.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*buttons, width=2)
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb

    @staticmethod
    def create_search_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_tag_search.value),
            KeyboardButton(text=AllLexicon.button_text_search.value),
            KeyboardButton(text=AllLexicon.button_tag_list.value),
            KeyboardButton(text=AllLexicon.button_menu.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*buttons, width=4)
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb

    @staticmethod
    def create_tag_list_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_back.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*buttons, width=1)
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb

    @staticmethod
    def create_back_menu_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_menu.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*buttons, width=1)
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb

    @staticmethod
    def create_back_to_search_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_back_to_search.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*buttons, width=1)
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb

    @staticmethod
    def create_text_showing_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=AllLexicon.button_back.value),
            KeyboardButton(text=AllLexicon.button_next.value),
            KeyboardButton(text=AllLexicon.button_back_to_search.value),
        ]
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*buttons, width=3)
        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True, resize_keyboard=True
        )
        return kb
