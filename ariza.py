from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from states import ArizaState
import re


async def set_get_first_name(message: types.Message, state: FSMContext):
    if len(message.text) >= 3:
        if any(char.isdigit() for char in message.text):
            await message.answer("Ismingizda raqam bo'lmasligi kerak")
        elif " " in message.text:
            await message.answer("Ismingizda probel bo'lmasligi kerak")
        else:
            await message.answer(
                f"Sizning ismingiz <b>{message.text.capitalize()}</b> qabul qilindi",
                parse_mode="html",
            )
            await state.update_data(first_name=message.text.capitalize())
            await message.answer("Familyangizni kiritng!")
            await state.set_state(ArizaState.last_name)

    else:
        await message.answer("Ismingiz 3 ta harfdan ko'p bo'lishi kerak")


async def set_get_last_name(message: types.Message, state: FSMContext):
    if len(message.text) >= 3:
        if any(char.isdigit() for char in message.text):
            await message.answer(
                "Familyangizda raqam bo'lmasligi kerak\nQayta kiriting"
            )
        elif " " in message.text:
            await message.answer(
                "Familyangizda probel bo'lmasligi kerak\nQayta kiriting"
            )
        else:
            await state.update_data(last_name=message.text.capitalize())
            await message.answer(
                f"Sizning ismingiz <b>{message.text.capitalize()}</b> qabul qilindi",
                parse_mode="html",
            )
            await message.answer("Yoshingizni kiriting:")

            await state.set_state(ArizaState.age)

    else:
        await message.answer(
            "Ismingiz 3 ta harfdan ko'p bo'lishi kerak\nQayta kiriting"
        )


async def set_get_age(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) >= 16:
            if int(message.text) <= 70:
                await state.update_data(age=message.text)
                await message.answer(
                    f"Sizni <b>{message.text}</b>-yoshingiz talabga javob beradi\nYoshingiz anketangizga qo'shildi.",
                    parse_mode="html",
                )
                await message.answer("Telifon raqamingizni kiriting:")
                await state.set_state(ArizaState.phone)

        else:
            await message.answer(
                "Siz hali balog'atga yetmagansiz! iltimos /cancel bosing"
            )


async def set_get_phone(message: types.Message, state: FSMContext):
    phone_pattern = re.compile(r"^\+998\d{9}$")  # +998 bilan boshlanadigan 9 ta raqam

    if phone_pattern.match(message.text):
        await state.update_data(phone=message.text)
        await message.answer(
            f"Sizning telefon raqamingiz {message.text} qabul qilindi ✅"
        )
        await message.answer("Lavozimingizni kiriting:")
        await state.set_state(ArizaState.position)  # Keyingi state'ga o'tish
    else:
        await message.answer(
            "Telefon raqam noto‘g‘ri formatda ❌\nTo‘g‘ri format: +998901234567"
        )


async def set_get_position(message: types.Message, state: FSMContext):
    """Foydalanuvchining lavozimini qabul qilish"""
    if len(message.text) >= 3:
        await state.update_data(position=message.text.capitalize())
        await message.answer(
            f"Sizning lavozimingiz '{message.text.capitalize()}' qabul qilindi ✅"
        )
        await message.answer("Maqsadingizni kiritnig kiriting:")

        await state.set_state(ArizaState.goal)  # Keyingi bosqichga o'tish
    else:
        await message.answer("Lavozim kamida 3 ta harfdan iborat bo‘lishi kerak ❌")


async def set_get_goal(message: types.Message, state: FSMContext):
    """Foydalanuvchining maqsadini qabul qilish"""
    if len(message.text) >= 5:
        await state.update_data(goal=message.text.capitalize())
        await message.answer(
            f"Sizning maqsadingiz '{message.text.capitalize()}' qabul qilindi ✅"
        )
        await message.answer("O'zingiz haqida ma'lumot kiriting:")

        await state.set_state(ArizaState.description)  # Keyingi bosqichga o'tish
    else:
        await message.answer("Maqsad kamida 5 ta harfdan iborat bo‘lishi kerak ❌")


async def set_get_description(message: types.Message, state: FSMContext):
    """Foydalanuvchining qo‘shimcha tavsifini qabul qilish"""
    if len(message.text) >= 10:
        await state.update_data(description=message.text.capitalize())
        await message.answer(
            f"Sizning tavsifingiz '{message.text.capitalize()}' qabul qilindi ✅"
        )
        data = await state.get_data()

        text = (
            f"# 📄 Malumotlar to'g'riligini tasdinglang:\n\n"
            f"👤 **Ism:** {data.get('first_name', 'Noma’lum')}\n"
            f"👥 **Familya:** {data.get('last_name', 'Noma’lum')}\n"
            f"📞 **Telefon:** {data.get('phone', 'Noma’lum')}\n"
            f"💼 **Lavozim:** {data.get('position', 'Noma’lum')}\n"
            f"🎯 **Maqsad:** {data.get('goal', 'Noma’lum')}\n"
            f"📝 **O'zingiz haqida:** {data.get('description', 'Noma’lum')}\n\n"
            f"✅ **To‘g‘ri bo‘lsa** 'Ha' yozing.\n❌ **Bekor qilish uchun** /cancel yuboring."
        )

        # Foydalanuvchiga tasdiqlash uchun yuborish
        await message.answer(text, parse_mode="Markdown")
        await state.set_state(ArizaState.verify)  # Keyingi bosqichga o'tish
    else:
        await message.answer("Tavsif kamida 10 ta harfdan iborat bo‘lishi kerak ❌")


import aiofiles


async def set_get_verify(message: types.Message, state: FSMContext, bot: Bot):
    # State'dan barcha ma'lumotlarni olish
    data = await state.get_data()

    admin_sender_text = (
        f"# 📄 Yangi ariza\n\n"
        f"👤 **Ism:** {data.get('first_name', 'Noma’lum')}\n"
        f"👥 **Familya:** {data.get('last_name', 'Noma’lum')}\n"
        f"📞 **Telefon:** {data.get('phone', 'Noma’lum')}\n"
        f"💼 **Lavozim:** {data.get('position', 'Noma’lum')}\n"
        f"🎯 **Maqsad:** {data.get('goal', 'Noma’lum')}\n"
        f"📝 **O'zingiz haqida:** {data.get('description', 'Noma’lum')}\n\n"
    )
    # Admin ID ga yuborish

    await bot.send_message(
        chat_id=7266833448, text=admin_sender_text, parse_mode="Markdown"
    )

    # Arizani .md faylga yozish
    async with aiofiles.open("arizalar.md", mode="w", encoding="utf-8") as file:
        await file.write(admin_sender_text + "\n\n-------------------------------\n")
    await message.answer(
        "Malumotlaringiz Kiritldi va adminga jo'natildi\n\nTez orada javob olasiz."
    )
    # State'ni tozalash
    await state.clear()
    del data


async def stop_command_answer_state(message: types.Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state is None:
        await message.answer("Arizani qayta to'ldirish uchun /application bosing")
    else:
        await state.clear()
        await message.answer("Arizangiz bekor qilindi❗️")
        await message.answer("Yana ariza berish uchun /application buyrug'ini bering.")


async def apllication_start(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(ArizaState.first_name)
