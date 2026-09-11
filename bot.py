import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

API_TOKEN = "8779410844:AAHiGxuDjJ_tLjdGHTQDKpuLFaj842w041Q"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    game_url = "https://tapffone6-web.github.io/network/"
    
    markup.add(
        InlineKeyboardButton(
            text="⛏️ افتح لعبة التعدين", 
            web_app=WebAppInfo(url=game_url)
        )
    )
    
    await message.reply(
        "مرحباً بك في بوت التعدين الخاص بك! 🚀\nاضغط على الزر أسفله لبدء اللعبة:", 
        reply_markup=markup
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, relax=0.1)
