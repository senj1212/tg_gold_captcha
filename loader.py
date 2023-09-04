from aiogram import Bot, types, Dispatcher
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

session_maker_m = [None]
def session_maker():
    return session_maker_m[0]

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)