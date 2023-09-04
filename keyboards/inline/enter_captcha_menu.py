from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation

def ikb_enter_captcha_menu(language, list_pattern):
    buttons_per_row = 2
    kb = InlineKeyboardMarkup()
    for i in range(0, len(list_pattern), buttons_per_row):
        row = list_pattern[i:i + buttons_per_row]  # Выбираем кнопки для текущего ряда
        kb.add(*[InlineKeyboardButton(text=p, callback_data=p) for p in row])
    kb.add(InlineKeyboardButton(text=get_translation(language, "btn_menu"), callback_data="menu"))
    return kb