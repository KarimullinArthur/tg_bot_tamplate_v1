from aiogram.dispatcher.filters import BoundFilter
from aiogram.utils.exceptions import BadRequest
from aiogram import types

from loader import dp, db, bot


class Sponsor(BoundFilter):
    key = 'check_sponsor'

    def __init__(self, check_sponsor):
        self.check_sponsor = check_sponsor

    async def check(self, message: types.Message) -> bool:
        try:
            member = dict(await bot.get_chat_member(user_id=message.from_user.id,
                                                    chat_id=db.get_sponsors()[0]['tg_id']))
            await message.reply(member)
            if member['status'] == 'left':
                await message.reply('no')
                return False
            else:
                await message.reply('yes')
                return True

        except BadRequest:
            await message.reply('no')
            return False


dp.filters_factory.bind(Sponsor)
