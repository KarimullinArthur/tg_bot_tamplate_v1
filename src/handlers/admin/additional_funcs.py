from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs
from utils.export_db import backup_db, export_txt


async def export_db(message: types.Message, state: FSMContext):
    await message.answer('Секундочку')

    backup_db()
    with open('../backups/backup.db', 'rb') as file:
        await message.reply_document(file)

    export_txt()
    with open('../backups/backup.txt') as file:
        await message.reply_document(file)


def register_additional_funcs(dp: Dispatcher):
    dp.register_message_handler(export_db,
                                Text(keyboards.text_button_export_db),
                                state=AdditionalFuncs, is_admin=True)
