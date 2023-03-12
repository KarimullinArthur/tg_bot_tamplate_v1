from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminManagement(StatesGroup):
    main_menu = State()


class AddAdmin(StatesGroup):
    tg_id = State()


class RemoveAdmin(StatesGroup):
    tg_id = State()
    check = State()
