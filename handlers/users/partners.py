from loader import dp, bot
from lang import get_translation
from keyboards.inline import ikb_partners_btn
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="partners")
async def callback_menu(call: CallbackQuery):
    language = call.from_user.language_code
    await bot.edit_message_text(
        text=get_translation(language, 'enter_text_from_image'),
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=ikb_partners_btn(language)
    )