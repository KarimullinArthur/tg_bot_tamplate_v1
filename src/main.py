import time

import logging
import logging.handlers
from aiogram import executor

from loader import dp, scheduler
from scheduler_jobs import schedule_jobs
from handlers.user import main_menu


def log_setup():
    logging.getLogger('apscheduler.executors.default').propagate = False
    log_handler = logging.handlers.WatchedFileHandler('../logs/main.log')
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        '%b %d %H:%M:%S')
    formatter.converter = time.gmtime
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)


main_menu.register_client_main_menu(dp)


async def on_startup(dp):
    schedule_jobs()


def main():
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    log_setup()
    logging.info("Start!")
    main()
