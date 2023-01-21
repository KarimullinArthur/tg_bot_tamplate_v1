from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from loader import db


text_button_first = '1'
text_button_admin_menu = 'adm'

text_button_stat = 'Stat'


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

    keyboard.row(stat)

    return keyboard
