from aiogram import types, F
from aiogram.filters import Command
from utils.config import bot, dp
from handlers.users.keyboard import chanel_keyboard_status, random_questions_F_key, back_about_f_key, back_about_and_contact_f_key
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from utils.text import user_startup_text, user_startup_text_no_sub,help_text,about_text 


@dp.message(Command("test"))
async def start_command(message: types.Message):
    web_app_url = 'https://nuts-g6i3.onrender.com'  # URL вашего веб-приложения
    keyboard = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(text="Открыть Web App", web_app=WebAppInfo(url=web_app_url))
    keyboard.add(web_app_button)
    
    await message.answer("Нажмите на кнопку ниже, чтобы открыть Web App.", reply_markup=keyboard)

