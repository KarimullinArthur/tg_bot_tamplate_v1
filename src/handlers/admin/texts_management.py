from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs


async def text_management(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.text_management())


def register_text_management(dp: Dispatcher):
    dp.register_message_handler(text_management,
                                Text(keyboards.text_button_texts_management),
                                state=AdditionalFuncs.main_menu)
