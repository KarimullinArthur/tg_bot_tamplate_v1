from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from loader import db


class Admin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        if message.from_user.id == 1151974450:
            return True

        else:
            return False
