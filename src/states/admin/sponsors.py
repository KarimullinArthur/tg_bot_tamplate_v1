from aiogram.dispatcher.filters.state import StatesGroup, State


class Sponsors(StatesGroup):
    main_menu = State()


class AddSponsor(StatesGroup):
    tg_id = State()
    link = State()
    name = State()


class DeleteSponsor(StatesGroup):
    name = State()
    check = State()
