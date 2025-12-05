from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start_cmd(message: types.Message):
        await message.answer("Привет! Это UniFinder бот!")
