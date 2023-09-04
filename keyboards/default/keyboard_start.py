from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lang import get_translation


def kb_start(language):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_translation(language, "btn_menu"))
            ]
        ],
        resize_keyboard=True
    )