import logging
from aiogram import Bot, Dispatcher, executor, types
import os

# التوكن محطوط هنا نيشان باش ما يوقع ليك حتى مشكل
API_TOKEN = "AAGpvCRBUj1NtaVawiCC"

# إعداد التسجيل لمراقبة الأخطاء
logging.basicConfig(level=logging.INFO)

# إعداد البوت والمشغل
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# الرد على أمر /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("مرحباً بك! البوت شغال الآن 24/7 بنجاح 🚀")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
