from aiogram import executor
from handlers import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from database import start_db


async def on_startup(dp):
    await start_db()

    await on_startup_notify(dp)
    await set_default_commands(dp)

    print("Bot started")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)