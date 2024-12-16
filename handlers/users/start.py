from aiogram import types, F
from aiogram.filters import Command
from utils.config import bot, dp
from handlers.users.keyboard import chanel_keyboard_status, random_questions_F_key, back_about_f_key, back_about_and_contact_f_key
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.text import user_startup_text, user_startup_text_no_sub,help_text,about_text 
from handlers.users.keyboard import random_question_button,get_invite_button , Tag_key, tag_reply_key, menu_keyboard, view_video



@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = await get_invite_button(bot)
    if message.chat.type == "private":
        user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=message.from_user.id)
        if user_channel_status.status != 'left':
            await message.answer("Привет. Я бот для обещения.Нажмите кнопку ниже, чтобы добавить бота в группу как администратора:", reply_markup=keyboard)
        else:
            await message.answer(user_startup_text_no_sub, reply_markup=chanel_keyboard_status())
    elif message.chat.type == 'group' or message.chat.type == 'supergroup':
        await message.answer("Теперь я в группе! Вот меню:", reply_markup=menu_keyboard())


@dp.message(Command("menu"))
async def menu_command(message: types.Message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        await message.answer("Вот меню вопросов:", reply_markup=menu_keyboard())

@dp.callback_query(F.data == "new_start")
async def new_start_funck_key(callback: types.CallbackQuery):
    await callback.message.delete()
    user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=callback.from_user.id)
    if user_channel_status.status != 'left':
        await callback.message.answer('Спасибо за подписку!')
        await callback.message.answer(user_startup_text, reply_markup=random_questions_F_key())
    else:
        await callback.message.answer('Ты все еще не подписался')
    await callback.answer()


@dp.callback_query(F.data == "help_F_key")
async def help_command(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(help_text, reply_markup=back_about_f_key())
    await callback.answer()


@dp.callback_query(F.data == "back_to_start_F_key")
async def back_to_start_F_key_command(callback: types.CallbackQuery):
    await callback.message.delete()
    user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=callback.message.from_user.id)
    if user_channel_status.status != 'left':
        await callback.message.answer(user_startup_text, reply_markup=random_questions_F_key())
    else:
        await callback.message.answer('Для начала подпишись на наш канал', reply_markup=chanel_keyboard_status())
    await callback.answer()

@dp.callback_query(F.data == "about_F_key")
async def about_F_key_command(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(about_text, reply_markup=back_about_and_contact_f_key())
    await callback.answer()



@dp.callback_query(F.data == "video_to_menu")
async def video_to_menu_command(callback: types.CallbackQuery):
    telegram_id = callback.message.chat.id 
    telegram_id = str(telegram_id)
    telegram_id = telegram_id[1:]
    await callback.message.delete()
    await callback.message.answer(f"Длfя просмотра видео перейдите по ссылке",reply_markup=view_video(id=telegram_id))
    await callback.answer()


@dp.callback_query(F.data == "about_F_key")
async def about_F_key_command(callback: types.CallbackQuery):
    await callback.message.answer("Пока что этой функции нету")


from aiogram.types.input_file import BufferedInputFile
@dp.message(Command("send_gif"))
async def send_gif(message: types.Message):
    with open("startbackground.gif", "rb") as file:
        gif_file = BufferedInputFile(file.read(), filename="example.gif")
        caption = "This is a GIF!"
        await bot.send_animation(chat_id=message.chat.id, animation=gif_file, caption=caption)
