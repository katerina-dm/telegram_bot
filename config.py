# конфигурации, настройки
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TG_API_KEY")

#интервал уменьшения показателей питомца  в секундах 
TIME_INTERVAL = 10

#словарик в котором будем хратить изменения
DECREASE_PARAMS = {
    "hunger": - 5,
    "energy": -3,
    "happiness": -1,
}