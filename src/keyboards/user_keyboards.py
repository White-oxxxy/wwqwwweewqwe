from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import src.lexicon

# ---- клавиатура главного меню ----

user_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_search']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_help'])
]

user_menu_kb_builder = ReplyKeyboardBuilder()

user_menu_kb_builder.row(*user_menu_buttons, width=2)

user_menu_kb: ReplyKeyboardMarkup = user_menu_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура поиска ----

user_search_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_tag_search']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_text_search']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_tag_list']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_menu'])
]

user_search_kb_builder = ReplyKeyboardBuilder()

user_search_kb_builder.row(*user_search_buttons, width=4)

user_search_kb: ReplyKeyboardMarkup = user_search_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура списка тэгов ----

user_tag_list_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_back'])
]

user_tag_list_kb_builder = ReplyKeyboardBuilder()

user_tag_list_kb_builder.row(*user_tag_list_buttons, width=1)

user_tag_list_kb: ReplyKeyboardMarkup = user_tag_list_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура возврата в меню ----

user_back_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_menu'])
]

user_back_menu_kb_builder = ReplyKeyboardBuilder()

user_back_menu_kb_builder.row(*user_back_menu_buttons, width=1)

user_back_menu_kb: ReplyKeyboardMarkup = user_back_menu_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура возврата в меню поиска ----

user_back_to_search_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_back_to_search'])
]

user_back_to_search_kb_builder = ReplyKeyboardBuilder()

user_back_to_search_kb_builder.row(*user_back_to_search_buttons, width=1)

user_back_to_search_kb: ReplyKeyboardMarkup = user_back_to_search_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура просмотра текстов ----

user_text_showing_interaction_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_next']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_back']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_menu'])
]

user_text_showing_interaction_kb_builder = ReplyKeyboardBuilder()

user_text_showing_interaction_kb_builder.row(*user_text_showing_interaction_buttons, width=3)

user_text_showing_interaction_kb: ReplyKeyboardMarkup = user_text_showing_interaction_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)