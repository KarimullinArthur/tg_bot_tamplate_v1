from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from filters.sponsors import Sponsor
from states.client.main_menu import ClientMain
from utils.datetime import get_datetime
from middleware.check_subs import check_subs as check_subss


async def start(message: types.Message, state: FSMContext):
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        ref_link = str(start_command[7:])

        if ref_link in db.get_ref_links():
            db.add_user(message.from_user.id, ref_link,
                        get_datetime())

        else:
            db.add_user(message.from_user.id, '',
                        get_datetime())
    else:
        db.set_user_activity(message.from_user.id, True)

    await message.answer(texts.start,
                         reply_markup=keyboards.main_menu(
                             message.from_user.id))
    await ClientMain.main_menu.set()


async def check_subs(callback: types.callback_query, state: FSMContext):
    if await check_subss(callback.message):
        await callback.message.answer(texts.start,
                                      reply_markup=keyboards.main_menu(
                                       callback.message.chat.id))
        await ClientMain.main_menu.set()


def register_client_main_menu(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*',
                                chat_type='private', check_sponsor=True)

    dp.register_callback_query_handler(check_subs, text='check_subs',
                                       state='*', chat_type='private')
