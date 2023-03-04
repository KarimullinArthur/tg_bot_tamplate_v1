from aiogram.dispatcher.filters.state import StatesGroup, State


class Sponsors(StatesGroup):
    main_menu = State()


class AddSponsor(StatesGroup):
    name = State()
    link = State()
    tg_id = State()


class DeleteSponsor(StatesGroup):
    name = State()
    check = State()
