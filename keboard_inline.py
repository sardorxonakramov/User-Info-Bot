"""Inline keyboard for telegram bot"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inlene_markab = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Button 1", callback_data="delete")]
    ]
)
