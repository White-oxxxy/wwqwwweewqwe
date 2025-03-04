from aiogram.fsm.state import State, StatesGroup


class FSMTagSearchForm(StatesGroup):
    fill_tag = State()

class FSMTextSearchForm(StatesGroup):
    fill_text = State()

