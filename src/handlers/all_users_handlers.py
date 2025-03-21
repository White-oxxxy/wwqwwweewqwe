from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from lexicon.roles import Roles
from fsm import *
from lexicon import *
from keyboards.user import UserKeyboards
from infrastructure.repository.user import (
    UserRepositoryORM,
    TextRepositoryORM,
    TextTagRepositoryORM,
)
from di.dev import get_container
from utils.utils import to_dict, join_tags


all_users_router = Router()


@all_users_router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message) -> None:
    container = get_container()
    async with container() as req_container:
        await message.answer(
            text=AllLexicon.answer_start.value, reply_markup=UserKeyboards.create_user_menu_kb()
        )
        user_repo = await req_container.get(UserRepositoryORM)
        user = await user_repo.get_by_user_id(message.from_user.id)
        if not user:
            await user_repo.create(
                user_id=message.from_user.id,
                username=message.from_user.username,
                role_id=Roles.user.value,
            )
            await user_repo.session.commit()


@all_users_router.message(Command(commands="help"), StateFilter(default_state))
async def process_help_command(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_help.value, reply_markup=UserKeyboards.create_user_menu_kb()
    )


@all_users_router.message(
    F.text == AllLexicon.button_help.value, StateFilter(default_state)
)
async def process_button_help(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_help.value, reply_markup=UserKeyboards.create_back_menu_kb()
    )


@all_users_router.message(
    F.text == AllLexicon.button_menu.value, StateFilter(default_state)
)
async def process_button_menu(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_menu.value, reply_markup=UserKeyboards.create_user_menu_kb()
    )


@all_users_router.message(
    F.text == AllLexicon.button_search.value, StateFilter(default_state)
)
async def process_search(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_search.value, reply_markup=UserKeyboards.create_search_kb()
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
            text=join_tags(tags), reply_markup=UserKeyboards.create_back_to_search_kb()
        )
    else:
        await message.answer(
            text=AllLexicon.answer_empty_tag_list.value,
            reply_markup=UserKeyboards.create_search_kb(),
        )


@all_users_router.message(
    F.text == AllLexicon.button_back_to_search.value, StateFilter(default_state)
)
async def process_back_to_search(message: Message) -> None:
    await message.answer(
        text=AllLexicon.answer_search.value, reply_markup=UserKeyboards.create_search_kb()
    )


@all_users_router.message(
    F.text == AllLexicon.button_back_to_search.value, ~StateFilter(default_state)
)
async def process_back_to_search_while_fsm(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=AllLexicon.answer_search.value, reply_markup=UserKeyboards.create_search_kb()
    )
    await state.clear()


@all_users_router.message(
    F.text == AllLexicon.button_tag_search.value, StateFilter(default_state)
)
async def process_tag_search(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=AllLexicon.answer_insert_tag.value,
        reply_markup=UserKeyboards.create_back_to_search_kb(),
    )
    await state.set_state(FSMTagSearchForm.fill_tag)


@all_users_router.message(StateFilter(FSMTagSearchForm.fill_tag))
async def process_sent_tag(message: Message, state: FSMContext) -> None:
    if message.text[0] == AdminLexicon.prefix.value:
        container = get_container()
        await state.update_data(tag=message.text)
        await state.set_state(FSMTagSearchForm.text_interaction)
        async with container() as req_container:
            text_tag_repo: TextTagRepositoryORM = await req_container.get(
                TextTagRepositoryORM
            )
            data = await state.get_data()
            texts = await text_tag_repo.get_by_tag(data["tag"])
            if len(texts) > 0:
                await state.update_data(text=to_dict(texts))
                await state.update_data(pages=len(texts))
                await state.update_data(current_page=0)

                data = await state.get_data()

                await message.answer(
                    text=data["text"][str(data["current_page"])]["value"],
                    reply_markup=UserKeyboards.create_text_showing_kb(),
                )
                await message.answer(
                    text=str(data["current_page"] + 1) + "/" + str(data["pages"])
                )
            else:
                await message.answer(
                    text=AllLexicon.answer_result_not_found.value,
                    reply_markup=UserKeyboards.create_search_kb(),
                )
                await state.clear()
    else:
        await message.answer(
            text=AllLexicon.answer_if_incorrect_prefix.value,
            reply_markup=UserKeyboards.create_back_to_search_kb(),
        )


@all_users_router.message(
    F.text == AllLexicon.button_next.value,
    StateFilter(FSMTagSearchForm.text_interaction),
)
async def process_button_next_in_tag_fsm(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if data["current_page"] + 1 <= data["pages"] - 1:
        await state.update_data(current_page=data["current_page"] + 1)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )
    else:
        await state.update_data(current_page=0)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )


@all_users_router.message(
    F.text == AllLexicon.button_back.value,
    StateFilter(FSMTagSearchForm.text_interaction),
)
async def process_button_back_in_tag_fsm(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if data["current_page"] - 1 >= 0:
        await state.update_data(current_page=data["current_page"] - 1)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )
    else:
        await state.update_data(current_page=data["pages"] - 1)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )


@all_users_router.message(
    F.text == AllLexicon.button_text_search.value, StateFilter(default_state)
)
async def process_word_search(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=AllLexicon.answer_insert_word.value,
        reply_markup=UserKeyboards.create_back_to_search_kb(),
    )
    await state.set_state(FSMTextSearchForm.fill_text)


@all_users_router.message(StateFilter(FSMTextSearchForm.fill_text))
async def process_text_sent(message: Message, state: FSMContext) -> None:
    container = get_container()
    await state.update_data(word=message.text)
    await state.set_state(FSMTextSearchForm.text_interaction)
    async with container() as req_container:
        text_tag_repo: TextTagRepositoryORM = await req_container.get(
            TextTagRepositoryORM
        )
        data = await state.get_data()
        texts = await text_tag_repo.get_by_text(data["word"])
        if len(texts) > 0:
            await state.update_data(text=to_dict(texts))
            await state.update_data(pages=len(texts))
            await state.update_data(current_page=0)

            data = await state.get_data()

            await message.answer(
                text=data["text"][str(data["current_page"])]["value"],
                reply_markup=UserKeyboards.create_text_showing_kb(),
            )
            await message.answer(
                text=str(data["current_page"] + 1) + "/" + str(data["pages"])
            )
        else:
            await message.answer(
                text=AllLexicon.answer_result_not_found.value,
                reply_markup=UserKeyboards.create_search_kb(),
            )
            await state.clear()


@all_users_router.message(
    StateFilter(FSMTextSearchForm.text_interaction),
    F.text == AllLexicon.button_next.value,
)
async def process_button_next_in_text_fsm(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if data["current_page"] + 1 <= data["pages"] - 1:
        await state.update_data(current_page=data["current_page"] + 1)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )
    else:
        await state.update_data(current_page=0)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )


@all_users_router.message(
    StateFilter(FSMTextSearchForm.text_interaction),
    F.text == AllLexicon.button_back.value,
)
async def process_button_back_in_text_fsm(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if data["current_page"] - 1 >= 0:
        await state.update_data(current_page=data["current_page"] - 1)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )
    else:
        await state.update_data(current_page=data["pages"] - 1)

        data = await state.get_data()

        await message.answer(
            text=data["text"][str(data["current_page"])]["value"],
            reply_markup=UserKeyboards.create_text_showing_kb(),
        )
        await message.answer(
            text=str(data["current_page"] + 1) + "/" + str(data["pages"])
        )
