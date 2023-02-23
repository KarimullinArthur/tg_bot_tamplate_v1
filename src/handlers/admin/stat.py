from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from states.admin.main_menu import AdminMain
from states.client.main_menu import ClientMain


async def stat(message: types.Message, state: FSMContext):
    all = len(db.get_all_tg_id())
    live = len(db.get_all_tg_id(only_live=True))
    dead = all - live
    await message.answer(f'''
#Статистика\n
👥Живых {live}
💀Мёртвых {dead}
📊Всего {all}''')


def register_stat(dp: Dispatcher):
    dp.register_message_handler(stat,
                                Text(keyboards.text_button_stat),
                                state=AdminMain, is_admin=True)
