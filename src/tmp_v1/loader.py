from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config

storage = RedisStorage2('localhost', 6379, db=5, pool_size=10,
                        prefix='my_fsm_key')
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()
