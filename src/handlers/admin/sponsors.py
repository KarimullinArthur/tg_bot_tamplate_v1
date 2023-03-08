import re

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text, ForwardedMessageFilter, Regexp

from loader import db
from markups import keyboards
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.sponsors import Sponsors, AddSponsor, DeleteSponsor


async def sponsers(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=keyboards.sponsors())
    await Sponsors.main_menu.set()


async def add_sponsor(message: types.Message, state: FSMContext):
    await message.answer('''Введите телеграм ID, или просто перешли
сообщение из канала''', reply_markup=keyboards.cancel())
    await AddSponsor.next()


async def get_tg_id_for_add_sponsor(message: types.Message, state: FSMContext):
    if re.match('-\d{0,9}$', message.text):
        async with state.proxy() as data:
            data['tg_id'] = message.text
        await message.answer("Введите ссылку на канал",
                             reply_markup=keyboards.cancel())
        await AddSponsor.next()
    else:
        await message.reply("Это не ID",
                            reply_markup=keyboards.cancel())


async def get_tg_id_for_add_sponsor_forward(message: types.Message,
                                            state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.forward_from_chat.id
    await message.answer("Введите ссылку на канал",
                         reply_markup=keyboards.cancel())
    await AddSponsor.next()


async def get_link_for_add_sponsor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
    await message.answer("Введите название канала",
                         reply_markup=keyboards.cancel())
    await AddSponsor.next()


async def get_name_for_add_sponsor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.add_sponsor(data['tg_id'], data['link'], message.text)
    await message.answer('''Готово, не забудь добавить бота на канал,
и дать ему права администатора''', reply_markup=keyboards.sponsors())
    await Sponsors.main_menu.set()


async def delete_sponsor(message: types.Message, state: FSMContext):
    if db.get_sponsors() == []:
        await message.answer("Нет ни одного канала")
    else:
        await message.answer(message.text, reply_markup=keyboards.cancel())
        await message.answer("Выберите",
                             reply_markup=keyboards.sponsors_list())
        await DeleteSponsor.name.set()


async def delete_sponsor_inline(callback: types.callback_query,
                                state: FSMContext):
    async with state.proxy() as data:
        data['delete_channel_name'] = callback.data
    await callback.message.reply('Удаляем?',
                                 reply_markup=keyboards.check_yes_no())
    await DeleteSponsor.next()


async def delete_sponsor_check(message: types.Message, state: FSMContext):
    if message.text == keyboards.text_button_yes:
        async with state.proxy() as data:
            db.delete_sponsor(data['delete_channel_name'])
            await message.answer("Готово", reply_markup=keyboards.sponsors())
    else:
        await message.answer("Cancel", reply_markup=keyboards.sponsors())
    await Sponsors.main_menu.set()


async def sponsors_list(message: types.Message, state: FSMContext):
    if db.get_sponsors() == []:
        await message.answer("Нет ни одного канала")
    else:
        await message.answer(message.text,
                             reply_markup=keyboards.sponsors_list())


def register_sponsors(dp: Dispatcher):
    dp.register_message_handler(sponsers,
                                Text(keyboards.text_button_sponsors),
                                state=AdditionalFuncs, is_admin=True)

    dp.register_message_handler(add_sponsor,
                                Text(keyboards.text_button_add_sponsor),
                                state=Sponsors.main_menu, is_admin=True)

    dp.register_message_handler(get_tg_id_for_add_sponsor,
                                content_types='text', state=AddSponsor.tg_id,
                                is_admin=True)

    dp.register_message_handler(get_tg_id_for_add_sponsor_forward,
                                content_types='text', state=AddSponsor.tg_id,
                                is_forwarded=True, is_admin=True)

    dp.register_message_handler(get_link_for_add_sponsor,
                                content_types='text', state=AddSponsor.link,
                                is_admin=True)

    dp.register_message_handler(get_name_for_add_sponsor,
                                content_types='text', state=AddSponsor.name,
                                is_admin=True)

    dp.register_message_handler(delete_sponsor,
                                Text(keyboards.text_button_delete_sponsor),
                                state=Sponsors.main_menu, is_admin=True)

    dp.register_callback_query_handler(delete_sponsor_inline,
                                       text=tuple(map(lambda x: x['name'],
                                                  db.get_sponsors())),
                                       state='*', is_admin=True)

    dp.register_message_handler(delete_sponsor_check,
                                Text([keyboards.text_button_yes,
                                     keyboards.text_button_no]),
                                state=DeleteSponsor.check, is_admin=True)

    dp.register_message_handler(sponsors_list,
                                Text(keyboards.text_button_sponsors_list),
                                state=Sponsors.main_menu, is_admin=True)
