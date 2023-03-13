from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from markups import keyboards
from loader import db
from states.admin.main_menu import AdminMain
from states.client.main_menu import ClientMain


async def sing_in_to_admin_panel(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.admin_menu())
    await AdminMain.main_menu.set()


async def stat(message: types.Message, state: FSMContext):
    all = len(db.get_all_tg_id())
    live = len(db.get_all_tg_id(only_live=True))
    dead = all - live
    await message.answer(f'''
#Статистика\n
👥Живых {live}
💀Мёртвых {dead}
📊Всего {all}''')


def register_admin_panel(dp: Dispatcher):
    dp.register_message_handler(sing_in_to_admin_panel,
                                Text(keyboards.text_button_admin_menu),
                                state=ClientMain, is_admin=True)

    dp.register_message_handler(stat,
                                Text(keyboards.text_button_stat),
                                state=AdminMain, is_admin=True)
