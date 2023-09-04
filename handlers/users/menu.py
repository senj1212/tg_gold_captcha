from database import set_user_work
from loader import dp, bot
from lang import get_translation
from keyboards.inline import ikb_main_menu
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="menu")
async def callback_menu(call: CallbackQuery):
    await set_user_work(call.from_user.id, False)
    language = call.from_user.language_code
    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )
    await bot.send_message(
        text=get_translation(language, 'menu_message'),
        chat_id=call.from_user.id,
        reply_markup=ikb_main_menu(language)
    )



