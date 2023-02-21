from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from loader import db


text_button_first = 'Кнопка'
text_button_admin_menu = "Админ панель"
text_button_back = '🔙Назад'

text_button_stat = '📊Статистика'
text_button_distribution = '📢Рассылка'
text_button_additional_func = '⚙️Дополнительно'

text_button_sponsors = '📈Спонсерка'
text_button_referrals = '👥Рефка'
text_button_admins = '🔑Админы'
text_button_export_db = '📦Экспорт БД'

text_button_cancel = '🚫Отмена'
text_button_yes = '✅Да'
text_button_no = '🚫Нет'


def cancel():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    cancel = KeyboardButton(text_button_cancel)
    keyboard.add(cancel)

    return keyboard


def check_yes_no(text_yes=text_button_yes, text_no=text_button_no):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    yes = KeyboardButton(text_yes)
    no = KeyboardButton(text_no)

    keyboard.add(yes)
    keyboard.add(no)

    return keyboard


def custom_url_markup(text, url):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton(text, url=url)
    keyboard.add(button)

    return keyboard


def main_menu(user_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    but1 = KeyboardButton(text_button_first)
    admin_menu = KeyboardButton(text_button_admin_menu)

    keyboard.row(but1)
    if user_id in db.get_admins_tg_id():
        keyboard.add(admin_menu)

    return keyboard


def admin_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    stat = KeyboardButton(text_button_stat)
    distribution = KeyboardButton(text_button_distribution)
    additional_func = KeyboardButton(text_button_additional_func)
    back = KeyboardButton(text_button_back)

    keyboard.row(distribution, stat)
    keyboard.add(additional_func)
    keyboard.add(back)

    return keyboard


def additional_func():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sponsors = KeyboardButton(text_button_sponsors)
    referrals = KeyboardButton(text_button_referrals)
    admins = KeyboardButton(text_button_admins)
    export_db = KeyboardButton(text_button_export_db)
    back = KeyboardButton(text_button_back)

    keyboard.row(sponsors, referrals)
    keyboard.row(admins, export_db)
    keyboard.add(back)

    return keyboard
