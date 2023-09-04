from loader import dp, bot
from database import get_story_withdraw_by_uid
from keyboards.inline import ikb_btn_menu
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="story_withdraw")
async def callback_story_withdraw(call: CallbackQuery):
    language = call.from_user.language_code
    story = await get_story_withdraw_by_uid(call.from_user.id)
    await bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
    )
    text = '<code>'
    for i in story:
        line = f"{i[0].create_date} | {i[0].money}$ | 🟡 \n"
        text += line
    text += "</code>"
    await bot.send_message(
        text=text,
        chat_id=call.from_user.id,
        reply_markup=ikb_btn_menu(language)
    )