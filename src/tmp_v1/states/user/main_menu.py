from aiogram.dispatcher.filters.state import StatesGroup, State


class UserMain(StatesGroup):
    main_menu = State()
