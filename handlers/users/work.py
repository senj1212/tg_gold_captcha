from database import set_user_work, set_last_captcha
from loader import dp, bot
from lang import get_translation
from keyboards.inline import ikb_enter_captcha_menu
from aiogram.types import CallbackQuery
from core import get_random_captcha


@dp.callback_query_handler(text="start_work")
async def callback_menu(call: CallbackQuery):
    language = call.from_user.language_code
    pattern, file, l_pattern = get_random_captcha(call.from_user.id)
    await set_last_captcha(call.from_user.id, pattern)
    await set_user_work(call.from_user.id, True)

    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=file,
                         caption=get_translation(language, 'enter_text_from_image'),
                         reply_markup=ikb_enter_captcha_menu(language, l_pattern))

