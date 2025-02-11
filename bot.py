import asyncio
import logging
import json
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums.content_type import ContentType
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode

logging.basicConfig(level=logging.INFO)

bot = Bot("8165843151:AAHSypvP2GMR5sz6Pl7Y9_pjShRsavFmc60")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    webAppInfo = types.WebAppInfo(url="https://mini-app-tg-three.vercel.app/")
    kb_list = [
        [types.KeyboardButton(text='📖 Наш канал'), types.KeyboardButton(text='🎰 Рулетка', web_app=webAppInfo)],
        [types.KeyboardButton(text='💵 Заказать выплату'), types.KeyboardButton(text='💳 Пополнение')]
    ]

    builder = types.ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='Воспользуйтесь меню'
    )
    
    await message.answer(text='Привет!', reply_markup=builder)

@dp.message(F.text.contains('Наш канал'))
async def process_command_1(message: types.Message):
    inline_kb = [
        [types.InlineKeyboardButton(text='Канал тут!', url='https://habr.com')]
    ]
    await message.reply("Первая инлайн кнопка" , reply_markup=types.InlineKeyboardMarkup(inline_keyboard=inline_kb))

@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f'<b>{data["title"]}</b>\n\n<code>{data["desc"]}</code>\n\n{data["text"]}', parse_mode=ParseMode.HTML)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())