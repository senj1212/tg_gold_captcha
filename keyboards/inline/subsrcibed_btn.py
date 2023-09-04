from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation
from loader import config

def ikb_btn_subsibe(language):
    kb = InlineKeyboardMarkup(row_width=1)
    for btn in config.list_chanel:
        kb.add(InlineKeyboardButton(text=btn["name"], url=btn["url"]))
    kb.add(InlineKeyboardButton(text=get_translation(language, "btn_subscribed"), callback_data="subscribed"))
    return kb