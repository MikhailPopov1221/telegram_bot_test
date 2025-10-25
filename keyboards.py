from aiogram import types


BTN_FEED = "🌯 Покормить"
BTN_PLAY = "🥎 Поиграть"
BTN_SLEEP = "💤 Спать"
BTN_STATUS = "📊 Статус"
BTN_EXIT = "⭕ Выход"


main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
        [types.KeyboardButton(text=BTN_SLEEP), types.KeyboardButton(text=BTN_STATUS)],
        [types.KeyboardButton(text=BTN_EXIT)]
    ],
    resize_keyboard=True
)

remove_kb = types.ReplyKeyboardRemove()


food_kb = types.InlineKeyboardMarkup(
    inline_keyboard= [
        [
            types.InlineKeyboardButton(text="🥩 Стейк", callback_data="feed_steak"),
            types.InlineKeyboardButton(text="🍗 Индейка", callback_data="feed_turkey")
            ],
        
        [
            types.InlineKeyboardButton(text="🥃 Дать попить", callback_data="feed_water")
            ]
    ]
)