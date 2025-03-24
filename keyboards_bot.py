from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📝 Refaral link",
                description="Do'stingizni taklif qilish uchun havola",
            ),
            KeyboardButton(
                text="📋 Achkolar", description="TAklif qilingan do'stlaringiz soni"
            ),
            KeyboardButton(text="Javob", description="Javob berish"),
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
