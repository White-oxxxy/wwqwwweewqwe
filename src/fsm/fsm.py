from aiogram.fsm.state import State, StatesGroup


class FSMAddForm(StatesGroup):
    insert_tags = State()
    insert_text = State()


class FSMTagSearchForm(StatesGroup):
    fill_tag = State()
    text_interaction = State()


class FSMTextSearchForm(StatesGroup):
    fill_text = State()
    text_interaction = State()
