from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang import get_translation


def ikb_partners_btn(language):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text="ruCaptcha 🟢", url='https://rucaptcha.com')],
        [InlineKeyboardButton(text="Anti Captcha 🟢", url='https://anti-captcha.com')],
        [InlineKeyboardButton(text="2Captcha 🔴", url='https://2captcha.com')],
        [InlineKeyboardButton(text=get_translation(language, "btn_menu"), callback_data="menu")]
    ])