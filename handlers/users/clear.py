from aiogram import types
from loader import dp, bot

@dp.message_handler()
async def clear_handler(message: types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)