from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from loader import db


text_button_admin_menu = "🔑Админ панель"
text_button_back = '🔙Назад'

text_button_stat = '📊Статистика'
text_button_distribution = '📢Рассылка'
text_button_additional_funcs = '⚙️Дополнительно'

text_button_sponsors = '📈Обязка'
text_button_referral_links = '👥Рефка'
text_button_admins = '🔑Админы'
text_button_export_db = '📦Экспорт БД'

text_button_create_link = "➕Добавить ссылку"
text_button_delete_link = "➖Удалить ссылку"
text_button_my_links = "📄Мои ссылки"

text_button_add_sponsor = "➕Добавить канал"
text_button_delete_sponsor = "➖Удалить канал"
text_button_sponsors_list = "📄Текущие каналы"

text_button_subscribe = '➕Подписаться'
text_button_check = '✅Проверить'

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

    admin_menu = KeyboardButton(text_button_admin_menu)

    if user_id in db.get_admins_tg_id():
        keyboard.add(admin_menu)

    return keyboard


def admin_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    stat = KeyboardButton(text_button_stat)
    distribution = KeyboardButton(text_button_distribution)
    additional_func = KeyboardButton(text_button_additional_funcs)
    back = KeyboardButton(text_button_back)

    keyboard.row(distribution, stat)
    keyboard.add(additional_func)
    keyboard.add(back)

    return keyboard


def additional_func():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sponsors = KeyboardButton(text_button_sponsors)
    referral_links = KeyboardButton(text_button_referral_links)
    admins = KeyboardButton(text_button_admins)
    export_db = KeyboardButton(text_button_export_db)
    back = KeyboardButton(text_button_back)

    keyboard.row(sponsors, referral_links)
    keyboard.row(admins, export_db)
    keyboard.add(back)

    return keyboard


def referral_links():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    create_link = KeyboardButton(text_button_create_link)
    delete_link = KeyboardButton(text_button_delete_link)
    my_links = KeyboardButton(text_button_my_links)
    back = KeyboardButton(text_button_back)

    keyboard.row(delete_link, create_link)
    keyboard.add(my_links)
    keyboard.add(back)

    return keyboard


def referral_links_list():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    for name in db.get_ref_links():
        link = InlineKeyboardButton(name, callback_data=name)

        keyboard.add(link)

    return keyboard


def sponsors():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    add_channel = KeyboardButton(text_button_add_sponsor)
    remove_channel = KeyboardButton(text_button_delete_sponsor)
    sponsors_list = KeyboardButton(text_button_sponsors_list)
    back = KeyboardButton(text_button_back)

    keyboard.row(remove_channel, add_channel)
    keyboard.add(sponsors_list)
    keyboard.add(back)

    return keyboard


def sponsors_list():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    for sponsor in db.get_sponsors():
        sponsor = InlineKeyboardButton(sponsor['name'],
                                       callback_data=sponsor['name'])

        keyboard.add(sponsor)

    return keyboard


def subscribe_to_sponsors():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    check = InlineKeyboardButton(text_button_check, callback_data='check_subs')

    for sponsor in db.get_sponsors():
        channel = InlineKeyboardButton(sponsor['name'], sponsor['link'])
        keyboard.add(channel)

    keyboard.add(check)

    return keyboard
