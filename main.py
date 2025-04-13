"""Asosoiy file dastur ishlashi uchun"""

from aiogram import F, Bot, Dispatcher, filters
from asyncio import run
from environs import Env
from aiogram.fsm.storage.memory import MemoryStorage
import ariza
from states import ArizaState
import function
import filterlar
from menu import set_my_commands
import database
import referal

env = Env()
env.read_env()

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
Token = env.str("TOKEN")
# CHANNEL_ID = env.str("CHANNEL_ID")


async def startup_answer(bot: Bot):
    """Bot ishga tushganda ishga tushdi degan xabarni yuborish aynan berilgan chat id ga"""
    await bot.send_message(chat_id=7266833448, text="Bot ishga tushdi")
    await bot.send_message(chat_id=6774451595, text="Bot ishga tushdi")


async def shutdown_answer(bot: Bot):
    """Bot ishni to'xtatganda ishni to'xtatdi degan xabarni yuborish aynan berilgan chat id ga"""
    await bot.send_message(chat_id=7266833448, text="Bot ishdan to'xtadi")
    await bot.send_message(chat_id=6774451595, text="Bot ishdan to'xtadi")


async def start():
    """Botni ishga tushirish"""
    """Har bir botni ishga tushurish uchun register qilish kerak"""
    bot = Bot(token=Token)

    await set_my_commands(bot)
    # Keyboardlarni ro‘yxatdan o‘tkazish
    dp.message.register(function.majburiy_obuna, filterlar.is_subscribe_in_my_channel())

    dp.shutdown.register(shutdown_answer)
    dp.startup.register(startup_answer)
    dp.message.register(function.reply_keyboard_remove, F.text == "Cancel")
    dp.message.register(function.get_user_info, filters.Command("info"))
    dp.message.register(function.help_answer, filters.Command("help"))
    dp.message.register(function.start_answer, filters.Command("start"))
    dp.message.register(function.menu_answer, filters.Command("menu"))
    dp.message.register(function.stop_answer, filters.Command("stop"))
    dp.message.register(ariza.apllication_start, filters.Command("application"))

    # Har bir state uchun mos handlerlarni ro‘yxatdan o‘tkazish
    dp.message.register(ariza.set_get_first_name, ArizaState.first_name)
    dp.message.register(ariza.set_get_last_name, ArizaState.last_name)
    dp.message.register(ariza.set_get_age, ArizaState.age)
    dp.message.register(ariza.set_get_phone, ArizaState.phone)
    dp.message.register(ariza.set_get_position, ArizaState.position)
    dp.message.register(ariza.set_get_goal, ArizaState.goal)
    dp.message.register(ariza.set_get_description, ArizaState.description)
    dp.message.register(ariza.set_get_verify, ArizaState.verify)

    # Stop commandni ham qo‘shish
    dp.message.register(ariza.stop_command_answer_state, filters.Command("cancel"))

    # CONTACT  bilan ishlash
    dp.message.register(function.reply_contact_info, F.text == "📞 Aloqa")
    dp.message.register(function.get_number_in_contact, F.contact)
    dp.message.register(function.get_location_in_contact, F.location)

    # Filterlar bilan ishlash
    dp.message.register(function.echo)
    referal.register_handlers(dp)

    await dp.start_polling(bot, polling_timeout=0)
    # polling_timeout bu botga jevob yozililekkanda kutish vaqti


run(start())
