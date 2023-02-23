from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import db
from markups import keyboards
from markups import texts
from states.admin.main_menu import AdditionalFuncs


async def referral_links(message: types.Message, state: FSMContext):
    await message.answer(message.text)


def register_refferal_links(dp: Dispatcher):
    dp.register_message_handler(referral_links,
                                Text(keyboards.text_button_referral_links),
                                state=AdditionalFuncs, is_admin=True)
