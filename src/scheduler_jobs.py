from aiogram import Dispatcher

from loader import dp, scheduler


async def send_stat_to_admin(dp: Dispatcher):
    print('Hello')

def schedule_jobs():
    scheduler.add_job(send_stat_to_admin, 'cron', day='*', args=(dp,))
