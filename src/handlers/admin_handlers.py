from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from infrastructure.pg.models import TagORM, TextORM
from lexicon.roles import Roles
from fsm import *
from keyboards import *
from lexicon import *
from filters import *
from infrastructure.repository.user import (
    UserRepositoryORM,
    TextRepositoryORM,
)
from settings.dev import DevSettings, get_settings
from di.dev import get_container


settings: DevSettings = get_settings()
admin_ids = list(map(int, settings.ADMIN_IDS.split(",")))

admin_router = Router()


@admin_router.message(IsAdmin(admin_ids), CommandStart(), StateFilter(default_state))
async def process_command_start(message: Message) -> None:
    container = get_container()
    async with container() as req_container:
        user_repository = await req_container.get(UserRepositoryORM)

        user = await user_repository.get_by_user_id(message.from_user.id)
        if user:
            await message.answer(
                text=AllLexicon.answer_start.value, reply_markup=admin_menu_kb
            )
        else:
            await user_repository.create(
                user_id=message.from_user.id,
                username=message.from_user.username,
                role_id=Roles.admin.value,
            )
            await user_repository.session.commit()
            await message.answer(
                text=AllLexicon.answer_start.value, reply_markup=admin_menu_kb
            )


@admin_router.message(
    IsAdmin(admin_ids), Command(commands="help"), StateFilter(default_state)
)
async def process_command_help(message: Message) -> None:
    await message.answer(text=AllLexicon.answer_help.value, reply_markup=admin_menu_kb)


@admin_router.message(
    IsAdmin(admin_ids),
    F.text == AllLexicon.button_menu.value,
    StateFilter(default_state),
)
async def process_button_menu(message: Message) -> None:
    await message.answer(text=AllLexicon.answer_menu.value, reply_markup=admin_menu_kb)


@admin_router.message(
    IsAdmin(admin_ids),
    F.text == AllLexicon.button_menu.value,
    ~StateFilter(default_state),
)
async def process_button_menu_while_fsm(message: Message, state: FSMContext) -> None:
    await message.answer(text=AllLexicon.answer_menu.value, reply_markup=admin_menu_kb)
    await state.clear()


@admin_router.message(
    IsAdmin(admin_ids),
    F.text == AdminLexicon.button_add.value,
    StateFilter(default_state),
)
async def process_button_add_text(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMAddForm.insert_tags)
    await message.answer(
        text=AllLexicon.answer_insert_tag.value, reply_markup=all_users_back_menu_kb
    )


@admin_router.message(IsAdmin(admin_ids), StateFilter(FSMAddForm.insert_tags))
async def process_insert_tag(message: Message, state: FSMContext) -> None:
    if message.text[0] == AdminLexicon.prefix.value:
        await state.update_data(tag=message.text)
        await message.answer(
            text=AdminLexicon.answer_insert_text.value,
            reply_markup=all_users_back_menu_kb,
        )
        await state.set_state(FSMAddForm.insert_text)
    else:
        await message.answer(
            text=AllLexicon.answer_if_incorrect_prefix.value,
            reply_markup=all_users_back_menu_kb,
        )


@admin_router.message(IsAdmin(admin_ids), StateFilter(FSMAddForm.insert_text))
async def process_insert_text(message: Message, state: FSMContext) -> None:
    await state.update_data(text=message.text)
    container = get_container()
    async with container() as req_container:
        text_repo: TextRepositoryORM = await req_container.get(TextRepositoryORM)
        data = await state.get_data()

        tag: TagORM | None = await text_repo.get_by_name(name=data.get("tag"))
        if tag is None:
            tag: TagORM = TagORM(name=data.get("tag"), uploader_id=message.from_user.id)

        text: TextORM = await text_repo.create_text(
            value=data.get("text"), uploader_id=message.from_user.id
        )

        await text_repo.create_tag(tag, text.id)
        await text_repo.session.commit()

    await message.answer(
        text=AdminLexicon.answer_success_text_added.value, reply_markup=admin_menu_kb
    )
    await state.clear()
