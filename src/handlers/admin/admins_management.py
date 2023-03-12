import re

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text, ForwardedMessageFilter

from loader import db
from markups import keyboards
from markups import texts
from filters.admin import Admin
from states.admin.main_menu import AdminMain
from states.admin.additional_funcs import AdditionalFuncs
from states.admin.admin_management import AdminManagement
from states.admin.admin_management import AddAdmin, RemoveAdmin


async def admins_management(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.admin_management())
    await AdminManagement.main_menu.set()


async def add_admin(message: types.Message, state: FSMContext):
    await message.answer("Введи телеграм ID юзера,\
или просто перешли отнего сообщение",
                         reply_markup=keyboards.cancel())
    await AddAdmin.tg_id.set()


async def get_tg_id_for_add_admin_forward(message: types.Message,
                                          state: FSMContext):
    db.add_admin(message.forward_from.id)
    await message.reply('Готово', reply_markup=keyboards.admin_management())
    await AdminManagement.main_menu.set()


async def get_tg_id_for_add_admin(message: types.Message, state: FSMContext):
    if re.match('\d+', message.text):
        db.add_admin(message.text)
        await message.reply('Готово', reply_markup=keyboards.admin_management())
        await AdminManagement.main_menu.set()
    else:
        await message.reply("Это не ID")


async def remove_admin(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=keyboards.cancel())
    await message.answer("Выбери админа", reply_markup=keyboards.admin_list())
    await RemoveAdmin.tg_id.set()


async def get_tg_id_for_remove_admin(callback: types.callback_query,
                                     state: FSMContext):
    async with state.proxy() as data:
        data['delete_admin_tg_id'] = callback.data
    await callback.message.answer('Удаляем?',
                                  reply_markup=keyboards.check_yes_no())
    await RemoveAdmin.next()


async def remove_admin_check(message: types.Message, state: FSMContext):
    if message.text == keyboards.text_button_yes:
        async with state.proxy() as data:
            db.remove_admin(data['delete_admin_tg_id'])
            msg = 'Готово'
    else:
        msg = 'Отменил'

    await message.reply(msg, reply_markup=keyboards.admin_management())
    await AdminManagement.main_menu.set()


async def admin_list(message: types.Message, state: FSMContext):
    await message.answer(message.text,
                         reply_markup=keyboards.admin_list(url=True))


def register_admins_management(dp: Dispatcher):
    dp.register_message_handler(admins_management,
                                Text(keyboards.text_button_admins),
                                state=AdditionalFuncs, is_admin=True)

    dp.register_message_handler(add_admin,
                                Text(keyboards.text_button_add_admin),
                                state=AdminManagement.main_menu, is_admin=True)

    dp.register_message_handler(get_tg_id_for_add_admin_forward,
                                content_types='text',
                                state=AddAdmin.tg_id, is_forwarded=True)

    dp.register_message_handler(get_tg_id_for_add_admin,
                                content_types='text',
                                state=AddAdmin.tg_id)

    dp.register_message_handler(remove_admin,
                                Text(keyboards.text_button_remove_admin),
                                state=AdminManagement.main_menu, is_admin=True)

    dp.register_callback_query_handler(get_tg_id_for_remove_admin,
                                       text=db.get_admins_tg_id(),
                                       state=RemoveAdmin.tg_id)

    dp.register_message_handler(remove_admin_check,
                                Text((keyboards.text_button_yes,
                                      keyboards.text_button_no)),
                                state=RemoveAdmin.check)

    dp.register_message_handler(admin_list,
                                Text(keyboards.text_button_admin_list),
                                state=AdminManagement.main_menu,
                                is_admin=True)
