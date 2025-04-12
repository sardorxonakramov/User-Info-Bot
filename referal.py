from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link
from keyboards_bot import keyboards
import database


async def referal_link(message: Message, bot: Bot):
    """Foydalanuvchiga shaxsiy referal linkni yuborish"""
    user_id = message.from_user.id
    referal_url = await create_start_link(bot, payload=str(user_id))
    await message.answer(
        f"Sizning referal linkingiz:\n{referal_url}", reply_markup=keyboards
    )


async def check_referal(message: Message):
    """Foydalanuvchi referal orqali kirganda uni tizimga qo‘shish"""
    if message.text.startswith("/start "):
        payload = message.text.split(" ")[1]
        if payload.isdigit():
            inviter_id = int(payload)
            new_user_id = message.from_user.id
            if new_user_id != inviter_id:
                database.add_user(new_user_id, inviter_id)
                await message.answer(
                    f"Siz {inviter_id} tomonidan taklif qilindingiz!\n{inviter_id} foydalanuvchiga 1 ochko qo‘shildi.",
                    reply_markup=keyboards,
                )
            else:
                await message.answer(
                    "O'zingizni taklif qila olmaysiz!", reply_markup=keyboards
                )


async def show_points(message: Message):
    """Foydalanuvchining ochkolarini ko‘rsatish"""
    user_id = message.from_user.id
    points = database.get_points(user_id)
    await message.answer(f"Sizda {points} ochko bor.", reply_markup=keyboards)


async def reply_answer(message: Message):
    """Javob tugmasi bosilganda xabar yuborish"""
    await message.answer("Siz 'Javob' tugmasini bosdingiz!", reply_markup=keyboards)


def register_handlers(dp: Dispatcher):
    """Referal tizimi uchun handlerlarni ro‘yxatdan o‘tkazish"""
    dp.message.register(referal_link, F.text == "📝 Referal link")
    dp.message.register(show_points, F.text == "📋 Achkolar")
    dp.message.register(reply_answer, F.text == "Javob")
