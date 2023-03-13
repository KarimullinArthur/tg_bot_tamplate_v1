from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

import config
from loader import db
from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.referral_links import ReferralLinks, CreateLink, DeleteLink


async def referral_links(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=keyboards.referral_links())
    await ReferralLinks.main_menu.set()


async def create_link(message: types.Message, state: FSMContext):
    await message.answer("Введи название ссылки\n(A-z, -, _ )",
                         reply_markup=keyboards.cancel())
    await CreateLink.name.set()


async def get_name_for_create_link(message: types.Message, state: FSMContext):
    if len(message.text) > 25:
        await message.answer("Название ссылки не должно привышать 25 символов")

    else:
        db.add_ref_link(message.text)
        await message.answer(f'''Ссылка создана вот она
https://t.me/{config.BOT_NAME}?start={message.text}''',
                             reply_markup=keyboards.referral_links())
        await ReferralLinks.main_menu.set()


async def delete_link(message: types.Message, state: FSMContext):
    if db.get_ref_links() != []:
        await message.answer(message.text,
                             reply_markup=keyboards.referral_links_list())
        await DeleteLink.name.set()
    else:
        await message.answer("Ссылок нет")


async def delete_link_inline(callback: types.callback_query,
                             state: FSMContext):
    await callback.message.reply('Удаляем?',
                                 reply_markup=keyboards.check_yes_no())
    async with state.proxy() as data:
        data['delete_link'] = callback.data
    await DeleteLink.check.set()


async def delete_link_check(message: types.Message, state: FSMContext):
    if message.text == keyboards.text_button_yes:
        async with state.proxy() as data:
            db.remove_ref_link(data['delete_link'])
        await message.reply('Удалил', reply_markup=keyboards.referral_links())

    elif message.text == keyboards.text_button_no:
        await message.reply('Отменил', reply_markup=keyboards.referral_links())

    await ReferralLinks.main_menu.set()


async def my_links(message: types.Message, state: FSMContext):
    if db.get_ref_links() != []:
        await message.answer(message.text,
                             reply_markup=keyboards.referral_links_list())
    else:
        await message.answer("Ссылок нет")


async def my_links_get_data(callback: types.callback_query, state: FSMContext):
    count = db.get_count_user_ref_link(callback.data)
    await callback.message.reply(
            f"#{callback.data}\nПришло по ссылке - {count}\nСсылка - \
https://t.me/{config.BOT_NAME}?start={callback.data}",
            disable_web_page_preview=True)


def register_refferal_links(dp: Dispatcher):
    dp.register_message_handler(referral_links,
                                Text(keyboards.text_button_referral_links),
                                state=AdditionalFuncs, is_admin=True)

    dp.register_message_handler(create_link,
                                Text(keyboards.text_button_create_link),
                                state=ReferralLinks, is_admin=True)

    dp.register_message_handler(get_name_for_create_link,
                                content_types='text', state=CreateLink.name,
                                is_admin=True)

    dp.register_message_handler(delete_link,
                                Text(keyboards.text_button_delete_link),
                                state=ReferralLinks, is_admin=True)

    dp.register_callback_query_handler(delete_link_inline,
                                       text=db.get_ref_links(),
                                       state=DeleteLink.name)

    dp.register_message_handler(delete_link_check,
                                Text((keyboards.text_button_yes,
                                      keyboards.text_button_no)),
                                state=DeleteLink.check)

    dp.register_message_handler(my_links,
                                Text(keyboards.text_button_my_links),
                                state=ReferralLinks.main_menu, is_admin=True)

    dp.register_callback_query_handler(my_links_get_data,
                                       text=db.get_ref_links(), state='*',
                                       is_admin=True)
