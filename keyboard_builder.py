# from aiogram.utils import ReplyKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


builder = ReplyKeyboardBuilder()
builder.button(text="Кнопка 1")
builder.button(text="Кнопка 2")
builder.add(
    KeyboardButton(text='Knopka 3')
)
builder.row(
    # bulder qilib qo'shsa hatolik berar ekan
    # builder.button(text='Кнопка 4'),
    # to'g'ri yondashuv
    KeyboardButton(text="Кнопка 4"),
    KeyboardButton(text="Кнопка 5"),
    KeyboardButton(text="Кнопка 6"),
    KeyboardButton(text="Кнопка 7"),

    width=2,
)
# bu knopkaga dizay berish ekan qanday tartibda chiqish kerakligini ko'rsatish uchun
builder.adjust(1,2,4)

# yangi buliderga copy qilish
builder2 = builder.copy()
builder2.add(KeyboardButton(text="Bu knopkani bosma"))

# ikkinchi builderni builderga birlashtirib yuboruvchi metod


