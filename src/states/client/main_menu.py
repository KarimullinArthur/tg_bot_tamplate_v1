from aiogram.dispatcher.filters.state import StatesGroup, State


class ClientMain(StatesGroup):
    main_menu = State()
