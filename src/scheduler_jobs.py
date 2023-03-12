from aiogram import Dispatcher

from loader import dp, scheduler
from handlers.admin.referral_links import register_refferal_links
from handlers.admin.sponsors import register_sponsors
from handlers.admin.admins_management import register_admins_management


async def update_handler(dp: Dispatcher):
    register_refferal_links(dp)
    register_sponsors(dp)
    register_admins_management(dp)


def schedule_jobs():
    scheduler.add_job(update_handler, 'cron', minute='*', args=(dp,))
