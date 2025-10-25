# все функции которые отвечают за перехват событий
from db import pets
from aiogram import Dispatcher, types, F
from aiogram.filters import Command

from keyboards import (
    main_kb,
    food_kb,
    BTN_EXIT,
    BTN_FEED,
    BTN_PLAY,
    BTN_SLLEP,
    BTN_STATUS
) 


def progress_bar(value: int, length: int):
    filled = int(value/100 * 10)
    return "🟩" * filled + "⬛" * (length - filled)

async def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler,Command("start"))
    dp.message.register(play_pet,F.text == BTN_PLAY)
    dp.message.register(feed_pet,F.text == BTN_FEED)
    dp.message.register(slip_pet,F.text == BTN_SLLEP)
    dp.message.register(status_pet, F.text ==  BTN_STATUS)
    dp.callback_query.register(food_callbeck_handler, lambda c: c.data.startswith("feed_")) #перехватчик кнопок кормления




async def start_handler(message: types.Message):
    user_id = message.from_user.id

    if user_id not in pets:
        new_pet = {
            "name": "Pepsik 🦎",
            "hunger": 50,
            "energy": 50,
            "happiness": 50,
        }

        pets[user_id] = new_pet

    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        f"Познакомься со своим питомцем: {pets[user_id]["name"]}!\n"
        f"Позаботься о нем!",
        reply_markup=main_kb
    )


async def feed_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return  
    pet = pets[user_id]
    await message.answer(
        f"Чем вы хотите покормить {pet['name']}?",
        reply_markup=food_kb
    )

    #pet["hunger"] = min(pet["hunger"] + 10, 100)
    #pet["energy"] = max(pet["energy"] - 5, 0)
    #await message.answer(f"{pet['name']} вкусно покушал!")


async def play_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100)
    pet["energy"] = max(pet["energy"] - 15, 0)
    await message.answer(f"{pet['name']} весело поиграл!")


async def slip_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["hunger"] = min(pet["hunger"] - 10, 100)
    pet["energy"] = max(pet["energy"] + 15, 0)
    await message.answer(f"{pet['name']} ушел спать!")


async def status_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    hun = pet['hunger']
    en = pet['energy']
    hap = pet['happiness']

    status = (
        f"Статус вашего питомца {pet['name']}\n"
        f"Сытость: {hun}% {progress_bar(hun ,10)}\n"
        f"Энергия: {en}% {progress_bar(en ,10)}\n"
        f"Счастье: {hap}% {progress_bar(hap ,10)}\n"
    )
    await message.answer(status)

async def food_callbeck_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in pets:
        await callback.message.edit_text("Сначала запусти бота с помощью команды /start")
        return
    
    pet = pets[user_id]
    food = callback.data
    message = ""
    h = pet["hunger"]

    if food == "feed_Ice cream":
        h = pet["hunger"] + 20
        message = f"Вы покормили {pet['name']} вкусной мороженкой "
    
    elif food == "feed_Shrimp":
        h = pet["hunger"] + 15
        message = f"Вы покормили {pet['name']} запеченной креветкой"
    
    elif food == "feed_drink":
        h = pet["hunger"] + 5
        message = f"Вы дали {pet['name']} попить воды"
    
    pet["hunger"] = min(100, h)

    await callback.message.edit_text(message)
    await callback.answer(
        f"Сытость {pet['name']} -- {pet["hunger"]}/100"
        f"{progress_bar(pet["hunger"], 10)}"
        )