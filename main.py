from aiogram import Bot, Dispatcher, filters
from asyncio import run
from environs import Env

from function import echo, get_user_info, help_answer
from menu import set_my_commands

env = Env()
env.read_env()
dp = Dispatcher()
Token = env.str("TOKEN")


async def startup_answer(bot: Bot):
    """Bot ishga tushganda ishga tushdi degan xabarni yuborish aynan berilgan chat id ga"""
    await bot.send_message(chat_id=7266833448, text="Bot ishga tushdi")


async def shutdown_answer(bot: Bot):
    """Bot ishni to'xtatganda ishni to'xtatdi degan xabarni yuborish aynan berilgan chat id ga"""
    await bot.send_message(chat_id=7266833448, text="Bot ishdan to'xtadi")


async def start():
    """Botni ishga tushirish"""
    """Har bir botni ishga tushurish uchun register qilish kerak"""
    bot = Bot(token=Token)
    dp.shutdown.register(shutdown_answer)
    dp.startup.register(startup_answer)
    dp.message.register(get_user_info, filters.Command("info"))
    dp.message.register(help_answer, filters.Command("help"))
    await set_my_commands(bot)
    dp.message.register(echo)
    await dp.start_polling(bot, polling_timeout=0)
    # polling_timeout bu botga jevob yozililekkanda kutish vaqti


run(start())
