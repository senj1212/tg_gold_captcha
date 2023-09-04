from aiogram import types
from database import get_user_by_uid, change_user_balance
from loader import dp, bot, config
from lang import get_translation
from keyboards.inline import ikb_work_menu


@dp.callback_query_handler()
async def callback_check_captcha(call: types.CallbackQuery):
    language = call.from_user.language_code
    user = await get_user_by_uid(call.from_user.id)
    if user.worked:
        await bot.delete_message(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
        )
        if user.last_captcha == call.data:
            await change_user_balance(call.from_user.id, config.EARNINGS)
            await bot.send_message(chat_id=call.from_user.id,
                                   text=get_translation(language, "great_captcha", add_money=config.EARNINGS),
                                   reply_markup=ikb_work_menu(language))
        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=get_translation(language, "bad_captcha"),
                                   reply_markup=ikb_work_menu(language))
        user.worked = False
