from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from filters.admin import Admin
from states.admin.main_menu import AdminMain
from states.admin.additional_funcs import AdditionalFuncs


async def admins_management(message: types.Message, state: FSMContext):
    await message.answer(message.text)


def register_admins_management(dp: Dispatcher):
    dp.register_message_handler(admins_management,
                                Text(keyboards.text_button_admins),
                                state=AdditionalFuncs, is_admin=True)
