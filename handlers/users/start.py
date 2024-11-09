from aiogram import types, F
from aiogram.filters import Command
from utils.config import bot, dp
from handlers.users.keyboard import chanel_keyboard_status, random_questions_F_key, back_about_f_key, back_about_and_contact_f_key
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.text import user_startup_text, user_startup_text_no_sub,help_text,about_text 

@dp.message(Command("start"))
async def start_command(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=message.from_user.id)
    if user_channel_status.status != 'left':
        await message.answer(user_startup_text, reply_markup=random_questions_F_key())
    else:
        await message.answer(user_startup_text_no_sub, reply_markup=chanel_keyboard_status())


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
