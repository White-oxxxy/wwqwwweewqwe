from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import *


# ---- клавиатура главного меню ----

all_users_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_search.value),
    KeyboardButton(text=AllLexicon.button_help.value),
]

all_users_menu_kb_builder = ReplyKeyboardBuilder()

all_users_menu_kb_builder.row(*all_users_menu_buttons, width=2)

all_users_menu_kb: ReplyKeyboardMarkup = all_users_menu_kb_builder.as_markup(
    one_type_keyboard=True, resize_keyboard=True
)

# ---- клавиатура поиска ----

all_users_search_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_tag_search.value),
    KeyboardButton(text=AllLexicon.button_text_search.value),
    KeyboardButton(text=AllLexicon.button_tag_list.value),
    KeyboardButton(text=AllLexicon.button_menu.value),
]

all_users_search_kb_builder = ReplyKeyboardBuilder()

all_users_search_kb_builder.row(*all_users_search_buttons, width=4)

all_users_search_kb: ReplyKeyboardMarkup = all_users_search_kb_builder.as_markup(
    one_type_keyboard=True, resize_keyboard=True
)

# ---- клавиатура списка тэгов ----

all_users_tag_list_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_back.value)
]

all_users_tag_list_kb_builder = ReplyKeyboardBuilder()

all_users_tag_list_kb_builder.row(*all_users_tag_list_buttons, width=1)

all_users_tag_list_kb: ReplyKeyboardMarkup = all_users_tag_list_kb_builder.as_markup(
    one_type_keyboard=True, resize_keyboard=True
)

# ---- клавиатура возврата в меню ----

all_users_back_menu_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_menu.value)
]

all_users_back_menu_kb_builder = ReplyKeyboardBuilder()

all_users_back_menu_kb_builder.row(*all_users_back_menu_buttons, width=1)

all_users_back_menu_kb: ReplyKeyboardMarkup = all_users_back_menu_kb_builder.as_markup(
    one_type_keyboard=True, resize_keyboard=True
)

# ---- клавиатура возврата в меню поиска ----

all_users_back_to_search_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_back_to_search.value)
]

all_users_back_to_search_kb_builder = ReplyKeyboardBuilder()

all_users_back_to_search_kb_builder.row(*all_users_back_to_search_buttons, width=1)

all_users_back_to_search_kb: ReplyKeyboardMarkup = (
    all_users_back_to_search_kb_builder.as_markup(
        one_type_keyboard=True, resize_keyboard=True
    )
)

# ---- клавиатура просмотра текстов ----

all_users_text_showing_interaction_buttons: list[KeyboardButton] = [
    KeyboardButton(text=AllLexicon.button_next.value),
    KeyboardButton(text=AllLexicon.button_back.value),
    KeyboardButton(text=AllLexicon.button_back_to_search.value),
]

all_users_text_showing_interaction_kb_builder = ReplyKeyboardBuilder()

all_users_text_showing_interaction_kb_builder.row(
    *all_users_text_showing_interaction_buttons, width=3
)

all_users_text_showing_interaction_kb: ReplyKeyboardMarkup = (
    all_users_text_showing_interaction_kb_builder.as_markup(
        one_type_keyboard=True, resize_keyboard=True
    )
)
