import logging

from aiogram import Dispatcher

from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            pass
            # text = "Bot started"
            # await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as e:
            logging.exception(e)
