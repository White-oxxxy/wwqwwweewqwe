from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import src.lexicon

# ---- клавиатура главного меню ----

admin_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_search']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_add']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_help'])
]

admin_menu_kb_builder = ReplyKeyboardBuilder()

admin_menu_kb_builder.row(*admin_menu_buttons, width=3)

admin_menu_kb: ReplyKeyboardMarkup = admin_menu_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура поиска ----

admin_search_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_tag_search']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_text_search']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_tag_list']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_menu'])
]

admin_search_kb_builder = ReplyKeyboardBuilder()

admin_search_kb_builder.row(*admin_search_buttons, width=4)

admin_search_kb: ReplyKeyboardMarkup = admin_search_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура списка тэгов ----

admin_tag_list_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_back'])
]

admin_tag_list_kb_builder = ReplyKeyboardBuilder()

admin_tag_list_kb_builder.row(*admin_tag_list_buttons, width=1)

admin_tag_list_kb: ReplyKeyboardMarkup = admin_tag_list_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура просмотра текстов ----

admin_text_showing_interaction_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_next']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_back']),
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_menu'])
]

admin_text_showing_interaction_kb_builder = ReplyKeyboardBuilder()

admin_text_showing_interaction_kb_builder.row(*admin_text_showing_interaction_buttons, width=3)

admin_text_showing_interaction_kb: ReplyKeyboardMarkup = admin_text_showing_interaction_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура возврата в меню ----

admin_back_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_menu'])
]

admin_back_menu_kb_builder = ReplyKeyboardBuilder()

admin_back_menu_kb_builder.row(*admin_back_menu_buttons, width=1)

admin_back_menu_kb: ReplyKeyboardMarkup = admin_back_menu_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)

# ---- клавиатура возврата в меню поиска ----

admin_back_to_search_buttons: list[KeyboardButton] = [
    KeyboardButton(text=src.lexicon.LEXICON_RU['button_back_to_search'])
]

admin_back_to_search_kb_builder = ReplyKeyboardBuilder()

admin_back_to_search_kb_builder.row(*admin_back_to_search_buttons, width=1)

admin_back_to_search_kb: ReplyKeyboardMarkup = admin_back_to_search_kb_builder.as_markup(
    one_type_keyboard=True,
    resize_keyboard=True
)
