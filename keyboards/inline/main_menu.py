from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation
from core import get_current_online

def ikb_main_menu(language):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text=get_translation(language, "btn_start_work"), callback_data="start_work")],
        [InlineKeyboardButton(text=get_translation(language, "btn_partners"), callback_data="partners")],
        [InlineKeyboardButton(text=get_translation(language, "btn_wallet"), callback_data="wallet")],
        [InlineKeyboardButton(text=get_translation(language, "btn_current_online", current_online=get_current_online()), callback_data="_")],
    ])