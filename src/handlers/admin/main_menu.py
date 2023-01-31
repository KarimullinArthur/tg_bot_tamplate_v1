from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from states.admin.main_menu import AdminMain
from states.client.main_menu import ClientMain
from utils.datetime import get_datetime


async def sing_in_to_admin_panel(message: types.Message, state: FSMContext):
    await message.answer(texts.start,
                         reply_markup=keyboards.admin_menu())
    await AdminMain.main_menu.set()


def register_admin_panel(dp: Dispatcher):
    dp.register_message_handler(sing_in_to_admin_panel,
                                Text(keyboards.text_button_admin_menu),
                                state=ClientMain)
