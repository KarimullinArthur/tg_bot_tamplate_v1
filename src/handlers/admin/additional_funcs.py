from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.main_menu import AdminMain
from utils.export_db import backup_db, export_txt


async def additional_funcs(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.additional_func())
    await AdditionalFuncs.main_menu.set()


async def export_db(message: types.Message, state: FSMContext):
    await message.answer('Секундочку')

    backup_db()
    with open('../backups/backup.db', 'rb') as file:
        await message.reply_document(file)

    export_txt()
    with open('../backups/export.txt') as file:
        await message.reply_document(file)


def register_additional_funcs(dp: Dispatcher):
    dp.register_message_handler(additional_funcs,
                                Text(keyboards.text_button_additional_funcs),
                                state=AdminMain, is_admin=True)

    dp.register_message_handler(export_db,
                                Text(keyboards.text_button_export_db),
                                state=AdditionalFuncs, is_admin=True)
