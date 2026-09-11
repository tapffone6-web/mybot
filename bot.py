import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# حط هنا الـ Token لي عطاك BotFather بين علامتي التنصيص
API_TOKEN = AAGpvCRBUjlNtaVawiCCauxHkWYL6R9yeJw

# حط هنا الأيدي (ID) ديالك فتيليجرام باش تولي أنت الأدمن الوحيد
# (إذا ما عرفتيش الأيدي ديالك، صيفط رسالة لبوت userinfobot فتيليجرام ويعطيه ليك)
ADMIN_ID = 1985474484

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

users_balance = {}  
banned_users = set()  
promo_codes = {"START2026": 50}  
used_promos = set()  

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    if user_id in banned_users:
        await message.reply("❌ أنت محظور من استخدام هذا البوت.")
        return
    
    if user_id not in users_balance:
        users_balance[user_id] = 0.0  

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⛏️ تعدين", "📋 المهام")
    markup.add("📺 مشاهدة إعلانات", "🎁 برومو كود")
    markup.add("💰 رصيدي", "📤 سحب الأرباح")

    await message.answer("مرحباً بك في بوت التعدين والمهام! اختر ما تحب من القائمة أدناه:", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "💰 رصيدي")
async def check_balance(message: types.Message):
    user_id = message.from_user.id
    if user_id in banned_users: return
    balance = users_balance.get(user_id, 0.0)
    await message.answer(f"💰 رصيدك الحالي هو: {balance} نقطة/عملة.")

@dp.message_handler(lambda message: message.text == "⛏️ تعدين")
async def mining(message: types.Message):
    user_id = message.from_user.id
    if user_id in banned_users: return
    users_balance[user_id] = users_balance.get(user_id, 0.0) + 1.0
    await message.answer("⛏️ لقد قمت بعملية تعدين ناجحة! تمت إضافة 1 نقطة إلى رصيدك.")

@dp.message_handler(lambda message: message.text == "🎁 برومو كود")
async def ask_promo(message: types.Message):
    await message.answer("أرسل البرومو كود هكذا:\n`/promo CODE`", parse_mode="Markdown")

@dp.message_handler(commands=['promo'])
async def use_promo(message: types.Message):
    user_id = message.from_user.id
    if user_id in banned_users: return
    
    args = message.get_args()
    if not args:
        await message.answer("المرجو كتابة البرومو كود مع الأمر. مثال: `/promo START2026`", parse_mode="Markdown")
        return
    
    code = args.strip()
    if code in promo_codes:
        if (user_id, code) in used_promos:
            await message.answer("❌ لقد استخدمت هذا البرومو كود مسبقاً!")
        else:
            reward = promo_codes[code]
            users_balance[user_id] = users_balance.get(user_id, 0.0) + reward
            used_promos.add((user_id, code))
            await message.answer(f"✅ مبروك! حصلت على {reward} نقطة.")
    else:
        await message.answer("❌ البرومو كود غير صالح أو انتهت صلاحيته.")

@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    await message.answer("🛠️ **مرحباً بك في لوحة التحكم الخاصة بالأدمن**\n\n"
                         "الأوامر المتاحة:\n"
                         "• `/ban [ID]` - حظر مستخدم\n"
                         "• `/unban [ID]` - إلغاء حظر مستخدم\n"
                         "• `/addbal [ID] [Amount]` - إضافة رصيد لمستخدم", parse_mode="Markdown")

@dp.message_handler(commands=['ban'])
async def ban_user(message: types.Message):
    if message.from_user.id != ADMIN_ID: return
    try:
        target_id = int(message.get_args())
        banned_users.add(target_id)
        await message.answer(f"✅ تم حظر المستخدم {target_id} بنجاح.")
    except:
        await message.answer("❌ خطأ، اكتب الأمر هكذا: `/ban ID`", parse_mode5="Markdown")

@dp.message_handler(commands=['addbal'])
async def add_balance(message: types.Message):
    if message.from_user.id != ADMIN_ID: return
    try:
        args = message.get_args().split()
        target_id = int(args[0])
        amount = float(args[1])
        users_balance[target_id] = users_balance.get(target_id, 0.0) + amount
        await message.answer(f"✅ تمت إضافة {amount} إلى رصيد المستخدم {target_id}.")
        await bot.send_message(target_id, f"🎉 لقد قام الإدارة بإضافة {amount} إلى رصيدك!")
    except:
        await message.answer("❌ خطأ، اكتب الأمر هكذا: `/addbal ID AMOUNT`", parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
