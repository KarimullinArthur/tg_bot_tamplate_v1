from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

import markup
from states.user.main_menu import UserMain
import texts


async def start(message: types.Message, state: FSMContext):
    await message.reply(texts.start, reply_markup=markup.main_menu())
    await UserMain.main_menu.set()


def register_client_main_menu(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
