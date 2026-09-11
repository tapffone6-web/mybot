import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# التوكن الصحيح ديال بوتك
API_TOKEN = "8779410844:AAGpvCRBUjlNtaVawiCCauxHkWYL6R9yeJw"

# إعداد التسجيل لمراقبة التشغيل
logging.basicConfig(level=logging.INFO)

# إعداد البوت والمشغل
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# الرد على أمر /start مع زر فتح ميني أب (Mini App)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # إنشاء لوحة مفاتيح أفقية تحتوي على زر يفتح اللعبة
    markup = InlineKeyboardMarkup()
    
    # استبدل الرابط أدناه برابط لعبة التعدين أو الـ Mini App الخاص بك
    game_url = "https://your-mining-game-url.com"
    
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
