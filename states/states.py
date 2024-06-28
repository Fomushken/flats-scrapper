from aiogram.fsm.state import State, StatesGroup

class FSMBairesScrap(StatesGroup):
    on_main = State()
    on_baires = State()
    subscribed = State()