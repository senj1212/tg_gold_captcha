from aiogram import types

from database import get_user_by_uid, change_user_balance, add_story_withdraw
from loader import dp, bot, config
from lang import get_translation
from keyboards.inline import ikb_btn_menu, ikb_btn_subsibe


@dp.callback_query_handler(text="withdraw")
async def callback_withdraw(call: types.CallbackQuery):
    language = call.from_user.language_code
    user = await get_user_by_uid(call.from_user.id)
    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )
    if user.balance < config.MIN_WITHDRAW:
        await bot.send_message(chat_id=call.from_user.id,
                                text=get_translation(language, "little_money", min_withdraw=config.MIN_WITHDRAW),
                                reply_markup=ikb_btn_menu(language))
    elif user.wallet == "":
        await bot.send_message(chat_id=call.from_user.id,
                                text=get_translation(language, "no_wallet"),
                                reply_markup=ikb_btn_menu(language))
    else:
        await bot.send_message(chat_id=call.from_user.id,
                                text=get_translation(language, "subscribe"),
                                reply_markup=ikb_btn_subsibe(language))


@dp.callback_query_handler(text="subscribed")
async def callback_great_withdraw(call: types.CallbackQuery):
    language = call.from_user.language_code
    user = await get_user_by_uid(call.from_user.id)
    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )
    balance = user.balance
    await change_user_balance(call.from_user.id, -balance)
    await add_story_withdraw(call.from_user.id, balance)
    await bot.send_message(chat_id=call.from_user.id,
                           text=get_translation(language, "great_withdraw"),
                           reply_markup=ikb_btn_menu(language))
