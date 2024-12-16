from aiogram import types, F
from aiogram.filters import Command
from utils.config import dp,bot
from db.DATABASE import User, Question, UserQuestion, Session, Tag,create_new_user,get_user_by_telegram_id,get_random_question_by_tag, UserTag
from handlers.users.keyboard import random_question_button,get_invite_button , Tag_key, tag_reply_key
from utils.utils import random_questions_F_funck
import random
from handlers.admin.keyboard import admin_panel_keyboard


@dp.callback_query(F.data == "questions_about_knowing")
async def new_start_funck_key(callback: types.CallbackQuery):
    if callback.from_user.is_bot:  # Проверяем, бот ли пользователь
        await callback.answer("Боты не могут взаимодействовать с этим ботом.", show_alert=True)
        return

    # Удаляем сообщение
    await callback.message.delete()

    # Отправляем сообщение пользователю
    user_id = callback.from_user.id
    await bot.send_message(chat_id=user_id, text="Добро пожаловать в панель администратора!")

    # Проверяем, является ли чат группой
    if callback.message.chat.type in ["group", "supergroup"]:
        # Отправляем сообщение в группу, но используем метод send_message вместо reply
        await bot.send_message(
            chat_id=callback.message.chat.id,  # Указываем ID чата группы
            text="Я отправил тебе доступ к панели администратора в личные сообщения."
        )
