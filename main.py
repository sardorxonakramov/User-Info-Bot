from aiogram import Bot, Dispatcher, types, html
from asyncio import run
from environs import Env    

env = Env()
env.read_env()
dp = Dispatcher()
Token = env.str("TOKEN")

async def startup_answer(bot:Bot):
    '''Bot ishga tushganda ishga tushdi degan xabarni yuborish aynan berilgan chat id ga'''
    await bot.send_message(chat_id=7266833448, text="Bot ishga tushdi")

async def shutdown_answer(bot:Bot):
    '''Bot ishni to'xtatganda ishni to'xtatdi degan xabarni yuborish aynan berilgan chat id ga'''
    await bot.send_message(chat_id=7266833448, text="Bot ishdan to'xtadi")

async def echo(message:types.Message,bot:Bot):
    '''Foydalanuvchi yuborgan xabarni qayta yuborish'''
    await bot.send_message(chat_id=message.chat.id, text=message.text)


async def start():
    '''Botni ishga tushirish'''
    '''Har bir botni ishga tushurish uchun register qilish kerak'''
    bot = Bot(token=Token)
    dp.shutdown.register(shutdown_answer)
    dp.startup.register(startup_answer)
    dp.message.register(echo)
    await dp.start_polling(bot, polling_timeout=0) 
    # polling_timeout bu botga jevob yozililekkanda kutish vaqti


run(start())