import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
BD_USERNAME = str(os.getenv("BD_USERNAME"))
DB_PASS = str(os.getenv("DB_PASS"))
DB_NAME = str(os.getenv("DB_NAME"))
DB_PORT = str(os.getenv("DB_PORT"))
HOST = str(os.getenv("HOST"))
MIN_WITHDRAW = int(os.getenv("MIN_WITHDRAW"))
EARNINGS = float(os.getenv("EARNINGS"))

list_chanel = [{"name": "LOLZ_NEWS", "url":"https://t.me/lolz_news"},
               {"name": "Страшно красиво", "url":"https://t.me/+b2A_8tcc2Q9kYTFi"}]

admins_id = []
