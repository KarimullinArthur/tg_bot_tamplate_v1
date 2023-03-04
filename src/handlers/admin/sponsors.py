from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.sponsors import Sponsors, AddSponsor, DeleteSponsor


async def sponsers(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=keyboards.sponsors())
    await Sponsors.main_menu.set()


async def add_sponsor(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await AddSponsor.name.set()


async def delete_sponsor(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await DeleteSponsor.name.set()


async def sponsors_list(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=keyboards.sponsors_list())


def register_sponsors(dp: Dispatcher):
    dp.register_message_handler(sponsers,
                                Text(keyboards.text_button_sponsors),
                                state=AdditionalFuncs, is_admin=True)

    dp.register_message_handler(add_sponsor,
                                Text(keyboards.text_button_add_sponsor),
                                state=Sponsors.main_menu, is_admin=True)

    dp.register_message_handler(delete_sponsor,
                                Text(keyboards.text_button_delete_sponsor),
                                state=Sponsors.main_menu, is_admin=True)

    dp.register_message_handler(sponsors_list,
                                Text(keyboards.text_button_sponsors_list),
                                state=Sponsors.main_menu, is_admin=True)
