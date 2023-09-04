from aiogram import types

from database import get_user_by_uid, add_user_in_db
from loader import dp, bot
from aiogram.dispatcher import filters
from lang import get_translation
from keyboards.inline import ikb_btn_menu


@dp.message_handler(filters.Command('start'))
async def command_start(message: types.Message):
    user = await get_user_by_uid(message.from_user.id)
    if user is None:
        await add_user_in_db(message.from_user.id)

    language = message.from_user.language_code
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer_photo(photo=open('start_img.jpg', 'rb'),
                               caption=get_translation(language, 'start_message'),
                               reply_markup=ikb_btn_menu(language))
