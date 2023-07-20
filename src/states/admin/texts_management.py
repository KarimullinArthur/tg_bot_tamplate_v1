from aiogram.dispatcher.filters.state import StatesGroup, State


class TextsManagement(StatesGroup):
    main_menu = State()

    welcome = State()
