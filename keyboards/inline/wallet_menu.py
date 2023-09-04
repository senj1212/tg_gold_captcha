from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation


def ikb_wallet_menu(language, current_balance):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text=get_translation(language, "current_balance", current_balance=current_balance), callback_data="not_work")],
        [InlineKeyboardButton(text=get_translation(language, "btn_withdraw"), callback_data="withdraw")],
        [InlineKeyboardButton(text=get_translation(language, "btn_set_wallet"), callback_data="set_wallet")],
        [InlineKeyboardButton(text=get_translation(language, "btn_wallet_story"), callback_data="story_withdraw")],
        [InlineKeyboardButton(text=get_translation(language, "btn_menu"), callback_data="menu")]
    ])