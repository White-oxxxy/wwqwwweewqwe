from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.infrastructure.pg.database import database
from src.filters import IsTag
from src.fsm import *
from src.lexicon import *
from src.keyboards import *
from src.infrastructure.repository.user import (
    UserRepositoryORM,
    RoleRepositoryORM,
    TagRepositoryORM,
    TextRepositoryORM,
    TextTagRepositoryORM
)



all_users_router = Router()


@all_users_router.message(
    CommandStart(), StateFilter(default_state)
)
async def process_start_command(message: Message) -> None:
    async with database.get_session() as session:
        user = await UserRepositoryORM.get_by_user_id(
            session, message.from_user.id
        )
        if user:
            await message.answer(
                text=AllLexicon.answer_start.value, reply_markup=all_users_menu_kb
            )
        else:
            await UserRepositoryORM.add_user(
                session, user_id=message.from_user.id, username=message.from_user.username,role_id=1
            )
            await message.answer(
                text=AllLexicon.answer_start.value, reply_markup=all_users_menu_kb
            )


@all_users_router.message(
    Command(commands="help"), StateFilter(default_state)
)
async def process_help_command(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_help.value, reply_markup=all_users_menu_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_help.value, StateFilter(default_state)
)
async def process_button_help(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_help.value, reply_markup=all_users_back_menu_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_menu.value, StateFilter(default_state)
)
async def process_button_menu(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_menu.value, reply_markup=all_users_menu_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_search.value, StateFilter(default_state)
)
async def process_search(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_search.value, reply_markup=all_users_search_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_tag_list.value, StateFilter(default_state)
)
async def process_tag_list(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_db.value, reply_markup=all_users_back_to_search_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_back_to_search.value, StateFilter(default_state)
)
async def process_back_to_search(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_search.value, reply_markup=all_users_search_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_back_to_search.value, ~StateFilter(default_state)
)
async def process_back_to_search(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=AllLexicon.answer_search.value, reply_markup=all_users_search_kb
    )
    await state.clear()


@all_users_router.message(
    F.text == AllLexicon.button_tag_search.value, StateFilter(default_state)
)
async def process_tag_search(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=AllLexicon.answer_insert_tag.value, reply_markup=all_users_back_to_search_kb,
    )
    await state.set_state(FSMTagSearchForm.fill_tag)


@all_users_router.message(
    StateFilter(FSMTagSearchForm.fill_tag), IsTag(F.text)
)
async def process_sent_tag(message: Message, state: FSMContext) -> None:
    await state.update_data(
        tag=message.text
    )
    await state.clear()
    await message.answer(
        text=AllLexicon.answer_result.value, reply_markup=all_users_text_showing_interaction_kb
    )


@all_users_router.message(
    StateFilter(FSMTagSearchForm.fill_tag)
)
async def warning_incorrect_tag(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_if_incorrect_prefix.value, reply_markup=all_users_back_to_search_kb
    )


@all_users_router.message(
    F.text == AllLexicon.button_text_search.value, StateFilter(default_state)
)
async def process_word_search(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=AllLexicon.answer_insert_word.value, reply_markup=all_users_back_to_search_kb,
    )
    await state.set_state(FSMTextSearchForm.fill_text)


@all_users_router.message(
    StateFilter(FSMTextSearchForm.fill_text), F.text.isalpha()
)
async def process_text_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(
        text=message.text
    )
    await state.clear()
    await message.answer(
        text=AllLexicon.answer_result.value, reply_markup=all_users_text_showing_interaction_kb
    )

