from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from states.admin.main_menu import AdminMain
from states.client.main_menu import ClientMain


async def stat(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await AdminMain.main_menu.set()


def register_stat(dp: Dispatcher):
    dp.register_message_handler(stat,
                                Text(keyboards.text_button_stat),
                                state=AdminMain, is_admin=True)
