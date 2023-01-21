from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from states.user.main_menu import UserMain
from utils.datetime import get_datetime


async def start(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
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
        await UserMain.main_menu.set()


def register_client_main_menu(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
