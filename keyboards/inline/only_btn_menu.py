from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation

def ikb_btn_menu(language):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text=get_translation(language, "btn_menu"), callback_data="menu")]
    ])