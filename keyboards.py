from aiogram import types

BTN_FEED = "🥪 Покормить"
BTN_PLAY = "🏀 Поиграть"
BTN_SLLEP = "💤 Спать"
BTN_STATUS = "✔ Статус"
BTN_EXIT = "💢 Выход"

#создаем клавиатуру
main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
        [types.KeyboardButton(text=BTN_SLLEP), types.KeyboardButton(text=BTN_STATUS)],
        [types.KeyboardButton(text=BTN_EXIT)]
    ],
    resize_keyboard=True #растянуть клавиатуру под экран
)

#удаление клавиуатуры
remove_kb = types.ReplyKeyboardRemove()

food_kb = types.InlineKeyboardMarkup(
    inline_keyboard= [
        [
            types.InlineKeyboardButton(text="🍨 Мороженка", callback_data="Ice cream"),
            types.InlineKeyboardButton(text="🥐 Креветка", callback_data="Shrimp")
        ],

        [
            types.InlineKeyboardButton(text="🥃 Дать попить", callback_data="drink")
        ]
    ]

)