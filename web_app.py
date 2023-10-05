from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('6292013883:AAHyMICr3dnSgzRLPeN20F73FvDk98SX_2w')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть сайт', web_app=WebAppInfo(url='https://ru.wikipedia.org/wiki/%D0%A5%D0%B8%D0%BD%D0%BA%D0%B0%D0%BB%D0%B8')))
    await message.answer('Здарова!!', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Ваше имя: {res["name"]}. Ваш Email: {res["email"]}. Ваш телефон: {res["phone"]}.')

executor.start_polling(dp)