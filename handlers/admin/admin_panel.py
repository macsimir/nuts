from aiogram import types, F
from aiogram.filters import Command
from utils.config import dp,bot
from db.DATABASE import User, Question, UserQuestion, Session, Tag,create_new_user,get_user_by_telegram_id,get_random_question_by_tag, UserTag
from handlers.users.keyboard import random_question_button,get_invite_button , Tag_key, tag_reply_key
from utils.utils import random_questions_F_funck
import random
from handlers.admin.keyboard import admin_panel_keyboard
# Инициализируем роутер

@dp.message(Command("admin_panel"))
async def admin_panel_func(message: types.Message):
    user_id = message.from_user.id
    # Отправляем сообщение в личные сообщения пользователя
    await bot.send_message(chat_id=user_id, text="Добро пожаловать в панель администратора!")
    
    # Если команда введена в группе, уведомляем пользователя в этом же чате
    if message.chat.type in ["group", "supergroup"]:
        await message.reply("Я отправил тебе доступ к панели администратора в личные сообщения.", reply_markup=admin_panel_keyboard())


# @dp.callback_query(F.data == "delete_q")
# async def random_questions_F_funck(callback: types.CallbackQuery):
#     await callback.message.delete()
#     session = Session()