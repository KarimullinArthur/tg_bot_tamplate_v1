from aiogram import Dispatcher

from loader import dp, scheduler
from handlers.admin.referral_links import register_refferal_links


async def update_handler(dp: Dispatcher):
    register_refferal_links(dp)


def schedule_jobs():
    scheduler.add_job(update_handler, 'cron', minute='*', args=(dp,))
