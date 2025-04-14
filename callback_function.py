from aiogram.types import CallbackQuery

async def delete_callback(callback: CallbackQuery):
    await callback.answer("Xabar o'chirildi")
    # await callback.answer("Xabar o'chirildi", show_alert=True)
    await callback.message.delete()
    await callback.message.answer("Xabar o'chirildi")