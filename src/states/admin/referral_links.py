from aiogram.dispatcher.filters.state import StatesGroup, State


class ReferralLinks(StatesGroup):
    main_menu = State()


class CreateLink(StatesGroup):
    name = State()


class DeleteLink(StatesGroup):
    name = State()
    check = State()
