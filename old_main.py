import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("TG_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# обработчик команды /start
@dp.message(Command("start"))
async def start_henler(message: types.Message):
    await message.answer("Привет! Ты запустил бота")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)
    

if __name__ =="__main__":
    asyncio.run(main())
