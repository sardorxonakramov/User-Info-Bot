from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types, html

async def set_my_commands(bot: Bot):
    """Bot uchun buyruqlarni sozlash"""
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Yordam"),
        BotCommand(command="/info", description="Foydalanuvchi haqida ma'lumot"),
        BotCommand(command="/menu", description="Menu"),
    ]
    await bot.set_my_commands(commands)
