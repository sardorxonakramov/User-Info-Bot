"""Men yaratgan barcha filterlar"""

from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link
from aiogram import Bot
# from main import CHANNEL_ID

CHANNEL_ID = -1001749261929
class is_text_in_message(Filter):
    def __init__(self, text: list):
        self.text = text
    async def __call__(self, message: Message):
        return message.text in self.text
    
class is_subscribe_in_my_channel(Filter):
    async def __call__(self,message:Message, bot:Bot):
        user_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            return False
        else:
            await message.answer("Botdan foydalanish uchun kanalga obuna bo'lishingiz kerak.")
            return False