from database import get_user_by_uid
from loader import dp, bot
from lang import get_translation
from keyboards.inline import ikb_wallet_menu
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="wallet")
async def callback_wallet_menu(call: CallbackQuery):
    language = call.from_user.language_code
    user = await get_user_by_uid(call.from_user.id)
    await bot.edit_message_text(
        text=get_translation(language, 'wallet'),
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=ikb_wallet_menu(language, round(user.balance, 2))
    )
