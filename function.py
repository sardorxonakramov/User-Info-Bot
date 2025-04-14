"""Men yasagan funksiyalar"""

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Bot
import keyboards_bot,keboard_inline


async def echo(message: Message, bot: Bot):
    """Foydalanuvchi yuborgan xabarni qayta yuborish"""
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id, reply_markup=keboard_inline.inlene_markab)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")




async def get_user_info(message: Message, bot: Bot):
    """Foydalanuvchi haqida ma'lumot olish"""
    user = await bot.get_chat(chat_id=message.from_user.id)
    user_photo = await message.from_user.get_profile_photos()

    bio = user.bio or "Ma'lumot yo'q"
    first_name = user.first_name if user.first_name else "Benom"
    last_name = user.last_name or "Familya kiritilmagan"
    username = user.username
    ids = user.id
    created = getattr(user, "created_at", "Ma'lumot yo'q")
    location = user.location
    language_code = getattr(user, "language_code", "english")

    # Tug‘ilgan sanani formatlash
    birth_date = getattr(user, "birthdate", None)
    if birth_date:
        if (
            hasattr(birth_date, "day")
            and hasattr(birth_date, "month")
            and hasattr(birth_date, "year")
        ):
            birth_date = f"{birth_date.day:02}.{birth_date.month:02}.{birth_date.year}"
        elif isinstance(birth_date, str):  # Agar string bo‘lsa
            try:
                from datetime import datetime

                birth_date = datetime.fromisoformat(birth_date).strftime("%d.%m.%Y")
            except ValueError:
                birth_date = "Ma'lumot yo'q"
        else:
            birth_date = "Ma'lumot yo'q"
    else:
        birth_date = "Ma'lumot yo'q"

    # isbot = getattr(user, 'is_bot', False)

    xabar = (
        f"<b>📌 User haqida ma'lumotlar</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"🕴️ <b>Ism:</b> {first_name}\n"
        f"🧑🏻‍🦽‍➡️ <b>Familiya:</b> {last_name}\n"
        f"🎉 <b>Tug‘ilgan sana:</b> {birth_date}\n"
        f"🤵 <b>Username:</b> {('@' + username) if username else '-'}\n"
        f"📝 <b>Bio:</b> {bio}\n"
        f"🆔 <b>ID:</b> <code>{ids}</code>\n"
        # f"🤖 <b>Bot:</b> {isbot}\n"
        f"📅 <b>Created:</b> {created}\n"
        f"📍 <b>Location:</b> {location}\n"
        f"🌐 <b>Language:</b> {language_code}\n"
        f"━━━━━━━━━━━━━━━━━━━"
    )
    if user_photo:
        try:
            await message.answer_photo(
                photo=user_photo.photos[0][-1].file_id, caption=xabar, parse_mode="HTML"
            )
        except IndexError:
            await bot.send_message(
                chat_id=message.chat.id, text=xabar, parse_mode="HTML"
            )
    else:
        await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML")


async def help_answer(message: Message, bot: Bot):
    """Yordam"""
    xabar = (
        "📌 <b>Yordam</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "📝 <b>Bot haqida:</b>\n"
        "Botdan foydalanish uchun /start ni bosing\n"
        "📝 <b>Ariza berish:</b>\n"
        "Ariza berish uchun /application ni bosing\n"
        "📝 <b>Ma'lumot olish:</b>\n"
        "Foydalanuvchi haqida ma'lumot olish uchun /info ni bosing\n"
        "📝 <b>Yordam:</b>\n"
        "Yordam olish uchun /help ni bosing\n"
        "📝 <b>Menu:</b>\n"
        "Menu ni ko'rish uchun /menu ni bosing\n"
        "━━━━━━━━━━━━━━━━━━━"
    )
    await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML", reply_markup=keyboards_bot.keyboards)


async def menu_answer(message: Message, bot: Bot):
    """Menu"""
    xabar = (
        "📌 <b>Menu</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "📝 <b>Botni ishga tushurish:</b> /start\n"
        "📝 <b>Yordam:</b> /help\n"
        "📝 <b>Ariza berish:</b> /application\n"
        "📝 <b>User ma'lumot olish:</b> /info\n"
        "📝 <b>Menu:</b> /menu\n"
        "━━━━━━━━━━━━━━━━━━━"
    )
    await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML", reply_markup=keyboards_bot.keyboards)


async def start_answer(message: Message, bot: Bot):
    """Botni ishga tushirish"""
    xabar = "Bot ishga tushdi"
    await bot.send_message(chat_id=message.chat.id, text=xabar)


async def stop_answer(message: Message, bot: Bot):
    """Botni to'xtatish"""
    xabar = "Bot ishdan to'xtadi"
    await bot.send_message(chat_id=message.chat.id, text=xabar)

async def reply_keyboard_remove(message: Message, bot: Bot):
    """ReplyKeyboardRemove"""
    xabar = "Reply Keyboard Remove \n\n[Javob tugmalari o'chirlidi]"
    await bot.send_message(chat_id=message.chat.id, text=xabar, reply_markup=ReplyKeyboardRemove())

async def reply_contact_info(message: Message, bot: Bot):
  
    await bot.send_message(chat_id=message.chat.id, text=keyboards_bot.contact_keyboard.input_field_placeholder, parse_mode="HTML", reply_markup=keyboards_bot.contact_keyboard)

async def get_number_in_contact(message:Message,bot:Bot):
    """Foydalanuvchi telefon raqamini yuboradi"""
    if message.contact:
        phone_number = message.contact.phone_number
        user_id = message.contact.user_id
        
        # user_name = message.contact.model_config
        name = message.contact.first_name + " "+ message.contact.last_name
        xabar = (
            f"📌 <b>Foydalanuvchi raqami</b>\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"📞 <b>Raqam:</b> {phone_number}\n"
            f"🆔 <b>ID:</b> {user_id}\n"
            # f"📝 <b>Username:</b> {user_name}\n"
            f"👤 <b>Name:</b> {name}\n"
            f"━━━━━━━━━━━━━━━━━━━"
        )
        await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML")
        await message.answer_contact(phone_number=phone_number,first_name=name.split()[0], last_name=name.split()[1])
    else:
        await bot.send_message(chat_id=message.chat.id, text="Raqam yuborilmadi", reply_markup=keyboards_bot.keyboards)

async def get_location_in_contact(message: Message, bot: Bot):
    """Foydalanuvchi manzilini yuboradi"""
    if message.location:
        kenglik = message.location.latitude
        uzunlik = message.location.longitude
        xabar = (
            f"📌 <b>Foydalanuvchi manzili</b>\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"📍 <b>Manzil:</b> {kenglik}, {uzunlik}\n"
            f"━━━━━━━━━━━━━━━━━━━"
        )
        await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML")
        await message.answer_location(latitude=kenglik, longitude=uzunlik)
    else:
        await bot.send_message(chat_id=message.chat.id, text="Manzil yuborilmadi", reply_markup=keyboards_bot.keyboards)

async def majburiy_obuna(message: Message, bot: Bot):
    """Foydalanuvchini kanalga obuna qilish"""
    link = '@myjobs1'
    await message.answer(
        f"Botdan foydalanish uchun kanalga obuna bo'lishingiz kerak.\n kanal {link} ",
    
    )