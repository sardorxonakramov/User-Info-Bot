"""Ariza yasash uchun kerakli hududlarga solish uchun kerakli state"""
from aiogram.fsm.state import State, StatesGroup


class ArizaState(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    phone = State()
    position = State()
    goal = State()
    description = State()
    verify = State()
