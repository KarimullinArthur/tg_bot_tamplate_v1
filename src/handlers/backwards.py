from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from markups import keyboards
from loader import bot
from states.admin.main_menu import AdminMain
from states.client.main_menu import ClientMain
from states.admin.distribution import Distribution
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.referral_links import ReferralLinks
from states.admin.sponsors import Sponsors


async def back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == 'AdminMain:main_menu':
        await message.answer(message.text,
                             reply_markup=keyboards.main_menu(
                                message.from_user.id))
        await ClientMain.main_menu.set()

    if current_state in ('AdditionalFuncs:main_menu', 'Distribution:message'):
        await message.answer(message.text,
                             reply_markup=keyboards.admin_menu())
        await AdminMain.main_menu.set()

    if current_state in ('Distribution:button_name',
                         'Distribution:button_url'):
        async with state.proxy() as data:
            await bot.copy_message(message.from_user.id, message.chat.id,
                                   data['message_id'])
            await bot.send_message(message.from_user.id, "Отправляем?",
                                   reply_to_message_id=data['message_id'],
                                   reply_markup=keyboards.check_yes_no())
            data['button_text'] = ''
            data['button_url'] = ''
        await Distribution.check.set()

    if current_state in ('ReferralLinks:main_menu', 'Sponsors:main_menu'):
        await message.answer(message.text,
                             reply_markup=keyboards.additional_func())
        await AdditionalFuncs.main_menu.set()

    if current_state == 'CreateLink:name':
        await message.answer(message.text,
                             reply_markup=keyboards.referral_links())
        await ReferralLinks.main_menu.set()

    if current_state in ('AddSponsor:tg_id', 'AddSponsor:link',
                         'AddSponsor:name', 'DeleteSponsor:name'):
        await message.answer(message.text, reply_markup=keyboards.sponsors())
        await Sponsors.main_menu.set()


def register_back(dp: Dispatcher):
    dp.register_message_handler(back, Text((keyboards.text_button_back,
                                            keyboards.text_button_cancel)),
                                state='*')
