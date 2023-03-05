from aiogram import types
from aiogram.utils.exceptions import BadRequest

from loader import db, bot
from markups import keyboards


async def check_subs(message: types.Message):
    for sponsor in db.get_sponsors():
        try:
            member = dict(await bot.get_chat_member(user_id=message.chat.id,
                                                    chat_id=sponsor['tg_id']))
            if member['status'] == 'left':
                await message.reply('no',
                                reply_markup=keyboards.subscribe_to_sponsors())
                return False

        except BadRequest:
            await message.reply('no',
                                reply_markup=keyboards.subscribe_to_channel())
            return False

    return True
