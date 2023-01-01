from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
import markup
from states.user.main_menu import UserMain
import texts


async def start(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            start_command = message.text
            ref_link = str(start_command[7:])

            if str(ref_link) in db.get_ref_links():
                db.add_user(message.from_user.id, ref_link,
                            misc.get_datetime())

            else:
                db.add_user(message.from_user.id, '',
                            misc.get_datetime())

        await message.answer(texts.start,
                             reply_markup=markup.main_menu(
                                 message.from_user.id))
        await UserMain.main_menu.set()


def register_client_main_menu(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
