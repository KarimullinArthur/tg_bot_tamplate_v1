from aiogram.dispatcher.filters import BoundFilter
from aiogram.utils.exceptions import BadRequest
from aiogram import types

from loader import dp, db, bot
from markups import keyboards


class Sponsor(BoundFilter):
    key = 'check_sponsor'

    def __init__(self, check_sponsor):
        self.check_sponsor = check_sponsor

    async def check(self, message: types.Message):
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


dp.filters_factory.bind(Sponsor)
