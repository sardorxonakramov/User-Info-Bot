""" inline keyboard builder bilan ishlaymiz"""

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from calendar import Calendar

kalendar = Calendar()
# Kalendarni yaratish
kalendarLST = kalendar.itermonthdays2(2025,4)

inline_builder = InlineKeyboardBuilder()

lst = ['Du','Se',"Cho",'Pay','Juma',"Shan","Ya"]
for i in lst:
    inline_builder.button(text=f"{i}",callback_data="delete")


for day in kalendarLST:
    if day[0] != 0:
        inline_builder.button(text=f"{day[0]:02}",callback_data="delete")
    else:
        inline_builder.button(text="  ",callback_data="null")



inline_builder.adjust(7,repeat=True)















# kalendarni to'g'ri tartibda chiqarish uchun ishlatilgan kod
# for i in kalendarLST:
#     print(str(i[0]).zfill(2) if i[0] else "  ",end=" ")
#     if i[1] == 6:
#         print()




















# inline builderni sinab ko'rish uchun yozilgan kod edi buu
# inline_builder = InlineKeyboardBuilder()

# inline_builder.button(text="Button 1", callback_data="ok")
# inline_builder.button(text="salom",callback_data="delete")
# inline_builder.row(
#     InlineKeyboardButton(
#         text="Button 2", callback_data="delete"
#     )
   
# )