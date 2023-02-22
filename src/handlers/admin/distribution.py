import asyncio

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import BotBlocked
from aiogram.utils.exceptions import BadRequest

from loader import db
from loader import bot
from markups import keyboards
from states.admin.main_menu import AdminMain
from states.admin.distribution import Distribution


async def distribution(message: types.Message, state: FSMContext):
    await message.answer("Что отправляем?", reply_markup=keyboards.cancel())
    await Distribution.message.set()


async def distribution_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message_id'] = message.message_id
        try:
            if dict(message)['reply_markup']:
                data['button_text'] = dict(message.reply_markup.inline_keyboard[0][0])['text']
                data['button_url'] = dict(message.reply_markup.inline_keyboard[0][0])['url']

                await bot.copy_message(message.from_user.id, message.chat.id,
                                       data['message_id'],
                                       reply_markup=keyboards.custom_url_markup(
                                           data['button_text'], data['button_url'])
                                       )
                await bot.send_message(message.from_user.id, "Отправляем?",
                                       reply_to_message_id=data['message_id'],
                                       reply_markup=keyboards.check_yes_no())
                await Distribution.check.set()

        except Exception:
            await message.answer("Добавить кнопку?",
                                 reply_markup=keyboards.check_yes_no())
            await Distribution.next()


async def distribution_keyboard(message: types.Message, state: FSMContext):
    if message.text == keyboards.text_button_yes:
        await message.answer("Название кнопки?",
                             reply_markup=keyboards.cancel())
        await Distribution.button_name.set()

    else:
        async with state.proxy() as data:
            await bot.copy_message(message.from_user.id, message.chat.id,
                                   data['message_id'])
            await bot.send_message(message.from_user.id, "Отправляем?",
                                   reply_to_message_id=data['message_id'],
                                   reply_markup=keyboards.check_yes_no())
        await Distribution.check.set()


async def distribution_button_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['button_text'] = message.text

    await message.reply('Ссылка?')
    await Distribution.next()


async def distribution_button_url(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['button_url'] = message.text

            await bot.copy_message(message.from_user.id, message.chat.id,
                                   data['message_id'],
                                   reply_markup=keyboards.custom_url_markup(
                                       data['button_text'], data['button_url'])
                                   )
            await bot.send_message(message.from_user.id, "Отправляем?",
                                   reply_to_message_id=data['message_id'],
                                   reply_markup=keyboards.check_yes_no())
        await Distribution.next()

    except BadRequest:
        await message.reply("Это не ссылка")


async def distribution_check(message: types.Message, state: FSMContext):
    if message.text == keyboards.text_button_yes:
        await AdminMain.main_menu.set()

        suc_send = 0
        fail_send = 0

        await message.answer("📢Рассылка началась",
                             reply_markup=keyboards.admin_menu())

        async with state.proxy() as data:
            for tg_id in db.get_all_tg_id(only_live=True):
                try:
                    if data['button_text'] != '':
                        await bot.copy_message(tg_id,
                                               message.from_user.id,
                                               data['message_id'],
                                               reply_markup=keyboards.custom_url_markup(
                                                    data['button_text'],
                                                    data['button_url']))
                    else:
                        await bot.copy_message(tg_id,
                                               message.from_user.id,
                                               data['message_id'])

                    suc_send += 1
                    await asyncio.sleep(1)

                except BotBlocked:
                    fail_send += 1
                    db.set_user_activity(tg_id, False)

                except Exception:
                    fail_send += 1

            await bot.send_message(message.from_user.id,
                                   f'''✅Рассылка закончилась\n
Получили {suc_send}
Не удалось {fail_send}''',
                                   reply_to_message_id=message.message_id-2)

            data['button_text'] = ''
            data['button_url'] = ''
    else:
        await message.answer('Отменил', reply_markup=keyboards.admin_menu())
        await AdminMain.main_menu.set()

        data['button_text'] = ''
        data['button_url'] = ''


def register_distribution(dp: Dispatcher):
    dp.register_message_handler(distribution,
                                Text(keyboards.text_button_distribution),
                                state=AdminMain)

    dp.register_message_handler(distribution_message,
                                content_types=['text', 'photo', 'video',
                                               'animation'],
                                state=Distribution.message, is_admin=True)

    dp.register_message_handler(distribution_keyboard,
                                Text([keyboards.text_button_yes,
                                     keyboards.text_button_no]),
                                state=Distribution.keyboard, is_admin=True)

    dp.register_message_handler(distribution_button_name,
                                content_types='text',
                                state=Distribution.button_name, is_admin=True)

    dp.register_message_handler(distribution_button_url,
                                content_types='text',
                                state=Distribution.button_url, is_admin=True)

    dp.register_message_handler(distribution_check,
                                Text([keyboards.text_button_yes,
                                     keyboards.text_button_no]),
                                state=Distribution.check, is_admin=True)
