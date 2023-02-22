from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from filters.admin import Admin
from states.admin.main_menu import AdminMain, AdditionalFuncs
from states.client.main_menu import ClientMain


async def sing_in_to_admin_panel(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.admin_menu())
    await AdminMain.main_menu.set()


async def additional_funcs(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.additional_func())
    await AdditionalFuncs.main_menu.set()


def register_admin_panel(dp: Dispatcher):
    dp.register_message_handler(sing_in_to_admin_panel,
                                Text(keyboards.text_button_admin_menu),
                                state=ClientMain, is_admin=True)

    dp.register_message_handler(additional_funcs,
                                Text(keyboards.text_button_additional_func),
                                state=AdminMain, is_admin=True)
