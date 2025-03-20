from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,ReplyKeyboardRemove

keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Ariza berish"),
            KeyboardButton(text="📋 Arizalarim",),
            KeyboardButton(text="Javob",description="Javob berish"),
        ],
        [
            KeyboardButton(text="📞 Aloqa"),
            KeyboardButton(text="❓ Yordam"),
        ],
    ],
    resize_keyboard=True,
    is_persistent=True,
    one_time_keyboard=False,
    input_field_placeholder="Menyuni tanlang",
)

