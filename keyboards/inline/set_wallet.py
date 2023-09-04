from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation


def ikb_set_wallet_menu(language):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text=get_translation(language, "btn_accept"), callback_data="accept_wallet"),
         InlineKeyboardButton(text=get_translation(language, "btn_menu"), callback_data="menu")]
    ])