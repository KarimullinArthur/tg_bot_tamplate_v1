from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.texts_management import TextsManagement


async def text_management(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.text_management())
    await TextsManagement.main_menu.set()


async def welcome(message: types.Message, state: FSMContext):
    await message.answer("test", reply_markup=keyboards.cancel())
    await TextsManagement.welcome.set()


async def get_value(message: types.Message, state: FSMContext):
    data = str(await state.get_state()).split(':')[1]
    db.edit_text(data, message.message_id, message.chat.id)
    await message.answer('Готово',
                         reply_markup=keyboards.text_management())
    await TextsManagement.main_menu.set()


def register_text_management(dp: Dispatcher):
    dp.register_message_handler(text_management,
                                Text(keyboards.text_button_texts_management),
                                state=AdditionalFuncs.main_menu)

    dp.register_message_handler(welcome,
                                Text(keyboards.text_button_text_management_welcome),
                                state=TextsManagement.main_menu)

    dp.register_message_handler(get_value,
                                content_types=('text', 'photo', 'video', 'gif',
                                               'animation'),
                                state=(TextsManagement.welcome, ))
