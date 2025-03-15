from aiogram.types import Message
from aiogram import Bot

async def echo(message: Message, bot: Bot):
    """Foydalanuvchi yuborgan xabarni qayta yuborish"""
    await bot.send_message(chat_id=message.chat.id, text=message.text)


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
    # Tug‘ilgan sanani formatlash
    # Tug‘ilgan sanani formatlash
    birth_date = getattr(user, "birthdate", None)
    if birth_date:
        if hasattr(birth_date, "day") and hasattr(birth_date, "month") and hasattr(birth_date, "year"):
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
        f"🕴️ <b>Familiya:</b> {last_name}\n"
        f"🎉 <b>Tug‘ilgan sana:</b> {birth_date}\n"
        f"🤵 <b>Username:</b> {('@' + username) if username else '-'}\n"
        f"📝 <b>Bio:</b> {bio}\n"
        f"🆔 <b>ID:</b> <code>{ids}</code>\n"
        # f"🤖 <b>Bot:</b> {isbot}\n"
        f"📅 <b>Created:</b> {created}\n"
        f"━━━━━━━━━━━━━━━━━━━"
    )
    if user_photo:
        try :
            await message.answer_photo(photo=user_photo.photos[0][-1].file_id, caption=xabar, parse_mode="HTML")
        except IndexError:
            await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML")
    else:
        await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML")

async def help_answer(message: Message, bot: Bot):
    """Yordam"""
    xabar = (
        "📌 <b>Yordam</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "📝 <b>Bot haqida:</b>\n"
        "Botdan foydalanish uchun /start ni bosing\n"
        "📝 <b>Ma'lumot olish:</b>\n"
        "Foydalanuvchi haqida ma'lumot olish uchun /info ni bosing\n"
        "📝 <b>Yordam:</b>\n"
        "Yordam olish uchun /help ni bosing\n"
        "📝 <b>Menu:</b>\n"
        "Menu ni ko'rish uchun /menu ni bosing\n"
        "━━━━━━━━━━━━━━━━━━━"
    )
    await bot.send_message(chat_id=message.chat.id, text=xabar, parse_mode="HTML")