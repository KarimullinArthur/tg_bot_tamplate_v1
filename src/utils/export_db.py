import os

import config
from loader import db


def backup_db():
    os.system(f"pg_dump -Fc {config.PG_DATABASE} > ../backups/backup.db")


def export_txt():
    _list = []

    for x in db.get_all_tg_id():
        _list.append(f"{x}\n")

    with open('../backups/backup.txt', 'w') as file:
        file.writelines(_list)
