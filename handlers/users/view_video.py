from aiogram import types, F
from aiogram.filters import Command
from utils.config import bot, dp
from handlers.users.keyboard import view_video
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from utils.text import user_startup_text, user_startup_text_no_sub,help_text,about_text 
from db.DATABASE import User, Question, UserQuestion, Session, Tag,create_new_user,get_user_by_telegram_id,get_random_question_by_tag, UserTag



@dp.message(Command("test"))
async def start_command(message: types.Message):
    web_app_url = 'https://nuts-g6i3.onrender.com'  # URL вашего веб-приложения
    keyboard = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(text="Открыть Web App", web_app=WebAppInfo(url=web_app_url))
    keyboard.add(web_app_button)
    
    await message.answer("Нажмите на кнопку ниже, чтобы открыть Web App.", reply_markup=keyboard)

@dp.callback_query(F.data == "video_to_menu")
async def video_to_menu_command(callback: types.CallbackQuery):
    telegram_id = callback.message.chat.id 
    await callback.message.delete()
    await callback.message.answer(f"Длfя просмотра видео перейдите по ссылке",reply_markup=view_video(id=telegram_id))
    await callback.answer()

