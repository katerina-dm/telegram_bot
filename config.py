# конфигурации, настройки
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TG_API_KEY")

#в которой будет храниться файл с базой данных
DB_NAME = "pet_bot.db"

#интервал уменьшения показателей питомца  в секундах 
TIME_INTERVAL = 10

#словарик в котором будем хратить изменения
DECREASE_PARAMS = {
    "hunger": - 5,
    "energy": -3,
    "happiness": -1,
}