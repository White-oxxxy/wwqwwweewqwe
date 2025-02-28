from aiogram.fsm.state import State, StatesGroup


class FSMAddForm(StatesGroup):
    insert_tags = State()
    insert_text = State()
