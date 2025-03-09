from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from lexicon.roles import Roles
from fsm import *
from lexicon import *
from keyboards import *
from infrastructure.repository.user import (
    UserRepositoryORM,
    TextRepositoryORM,
    TextTagRepositoryORM
)
from di.dev import get_container



all_users_router = Router()


@all_users_router.message(
    CommandStart(), StateFilter(default_state)
)
async def process_start_command(message: Message) -> None:
    container = get_container()
    async with container() as req_container:
        user_repo = await req_container.get(UserRepositoryORM)
        user = await user_repo.get_by_user_id(message.from_user.id)
        if user:
            await message.answer(
                text=AllLexicon.answer_start.value, reply_markup=all_users_menu_kb
            )
        else:
            await user_repo.add_user(
                user_id=message.from_user.id, username=message.from_user.username,role_id=Roles.user.value
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
    container = get_container()
    async with container() as req_container:
        tag_repo = await req_container.get(TextRepositoryORM)

        tags = await tag_repo.get_all_tag_names()

    if tags:
        await message.answer(
            text=", ".join(map(str, tags)), reply_markup=all_users_back_to_search_kb
        )
    else:
        await message.answer(
            text=AllLexicon.answer_empty_tag_list.value, reply_markup=all_users_search_kb
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
async def process_back_to_search_while_fsm(message: Message, state: FSMContext) -> None:
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
    StateFilter(FSMTagSearchForm.fill_tag)
)
async def process_sent_tag(message: Message, state: FSMContext) -> None:
    if message.text[0] == AdminLexicon.prefix.value:
        await state.update_data(
            tag=message.text
        )
        container = get_container()
        async with container() as req_container:
            repo = await req_container.get(TextTagRepositoryORM)


        await message.answer(
            text=AllLexicon.answer_result.value, reply_markup=all_users_text_showing_interaction_kb
        )
        await state.clear()
    else:
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
    StateFilter(FSMTextSearchForm.fill_text)
)
async def process_text_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(
        text=message.text
    )
    await state.clear()
    await message.answer(
        text=AllLexicon.answer_result.value, reply_markup=all_users_text_showing_interaction_kb
    )

