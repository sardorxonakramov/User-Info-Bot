"""ReplyKeybordMurkupda knopklar yartilgan file"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Asosiy menyu klaviaturasi
keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Referal link"),
            KeyboardButton(text="📋 Achkolar"),
            KeyboardButton(text="Javob"),
        ],
        [
            KeyboardButton(text="📞 Aloqa"),
            KeyboardButton(text="❓ Yordam"),
        ],
    ],
    resize_keyboard=True,
    is_persistent=True,
    one_time_keyboard=True,
    input_field_placeholder="Menyuni tanlang",
)


# Aloqa klaviaturasi
contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telifon nommer", request_contact=True),
            KeyboardButton(text="🏞️ manzilingizni kiritnig", request_location=True),
        ],
    ],
    resize_keyboard=True,
    is_persistent=True,
    one_time_keyboard=True,
    input_field_placeholder="Aloqa uchun tugmani bosing",
)
