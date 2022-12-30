from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


text_button_first = '1'


def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    but1 = KeyboardButton(text_button_first)

    keyboard.row(but1)

    return keyboard
