from aiogram.filters import Filter
from aiogram.types import Message

class is_text_in_message(Filter):
    def __init__(self, text: list):
        self.text = text
    async def __call__(self, message: Message):
        return message.text in self.text