
from aiogram import Bot, Dispatcher

import asyncio
from config import BOT_TOKEN # импортируем из файла config
from hundlers import register_handlers
from scheduler import start_sheduler



async def main():
    start_sheduler()
    print("Фоновые задачи запущены")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await register_handlers(dp)

    print("Бот запущен...")
    await dp.start_polling(bot)
    

if __name__ =="__main__":
    asyncio.run(main())

  