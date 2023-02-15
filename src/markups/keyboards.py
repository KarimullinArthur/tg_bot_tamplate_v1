from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from loader import db


text_button_first = 'Кнопка'
text_button_admin_menu = 'Админ панель'
text_button_back = '🔙Назад'

text_button_stat = '📊Статистика'
text_button_distribution = '📢Рассылка'
text_button_additional_func = '⚙️Дополнительно'


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
    back = KeyboardButton(text_button_back)
    distribution = KeyboardButton(text_button_distribution)

    keyboard.row(distribution, stat)
    keyboard.add(back)

    return keyboard


def additional_func():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    back = KeyboardButton(text_button_back)

    keyboard.add(back)

    return keyboard
