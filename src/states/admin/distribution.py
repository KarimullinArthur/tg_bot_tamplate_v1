from aiogram.dispatcher.filters.state import StatesGroup, State


class Distribution(StatesGroup):
    message = State()
    keyboard = State()
    button_name = State()
    button_url = State()
    check = State()
