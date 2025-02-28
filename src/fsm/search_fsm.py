from aiogram.fsm.state import State, StatesGroup


class FSMSearchForm(StatesGroup):
    fill_tag = State()
    fill_words = State()
