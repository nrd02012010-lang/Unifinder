from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Привет! Это UniFinder. Введи название университета.")

if _name_ == "_main_":
    executor.start_polling(dp, skip_updates=True)
