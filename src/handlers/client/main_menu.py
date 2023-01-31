from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from states.client.main_menu import ClientMain
from utils.datetime import get_datetime


async def start(message: types.Message, state: FSMContext):
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        ref_link = str(start_command[7:])

        if str(ref_link) in db.get_ref_links():
            db.add_user(message.from_user.id, ref_link,
                        get_datetime())

        else:
            db.add_user(message.from_user.id, '',
                        get_datetime())

    await message.answer(texts.start,
                         reply_markup=keyboards.main_menu(
                             message.from_user.id))
    await ClientMain.main_menu.set()


def register_client_main_menu(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*',
                                chat_type='private')
