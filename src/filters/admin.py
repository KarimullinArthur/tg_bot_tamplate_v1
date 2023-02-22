from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from loader import db
from loader import dp


class Admin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message) -> bool:
        if message.from_user.id == db.get_admins_tg_id():
            return True

        else:
            return False


dp.filters_factory.bind(Admin)
