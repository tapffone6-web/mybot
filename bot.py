import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = "8779410844:AAGpvCRBUjlNtaVawiCCauxHkWYL6R9yeJw"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    # رابط لعبة التعدين الجاهز
    game_url = "https://telegram-mining-game-demo.netlify.app"
    
    markup.add(
        InlineKeyboardButton(
            text="🚀 افتح لعبة التعدين", 
            web_app=WebAppInfo(url=game_url)
        )
    )
    
    await message.reply(
        "مرحباً بك في بوت التعدين الخاص بك! ⛏️\nاضغط على الزر أسفله لبدء اللعبة والتعدين مباشرة:", 
        reply_markup=markup
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
