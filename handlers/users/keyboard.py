from aiogram import types

def view_video(id):
    buttons = [
        [types.InlineKeyboardButton(text="Просмотр Видео", url=f"https://nuts-g6i3.onrender.com/message"),],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard



def menu_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Случайные вопросы", callback_data="random_questions_F_key")],
        # [types.InlineKeyboardButton(text="Просмотр Видео", callback_data="video_to_menu"),],
        # [types.InlineKeyboardButton(text="Вопросы на знания друг друга", callback_data="questions_about_knowing")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def chanel_keyboard_status():
    buttons = [
        [types.InlineKeyboardButton(text="Подписаться", url="https://t.me/macsimomg")],
        [types.InlineKeyboardButton(text="Проверка подписки", callback_data="new_start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def random_questions_F_key():
    
    buttons = [
        [types.InlineKeyboardButton(text="Подобрная инструкция", callback_data="help_F_key"),types.InlineKeyboardButton(text="Информация", callback_data="about_F_key")],
        [types.InlineKeyboardButton(text="Запустить", callback_data="random_questions_F_key")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def back_about_f_key():
    buttons = [
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_start_F_key")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def back_about_and_contact_f_key():
    buttons = [
        [types.InlineKeyboardButton(text="Все вопросы", url="https://t.me/macsimir"),types.InlineKeyboardButton(text="Оснвной телеграмм канал", url="https://t.me/macsimomg")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_start_F_key")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def random_question_button():
    kb = [
        [
            types.KeyboardButton(text="Новый вопрос"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
    return keyboard

async def get_invite_button(bot):
    bot_username = (await bot.get_me()).username  # Получаем имя пользователя бота асинхронно
    invite_url = f"https://t.me/{bot_username}?startgroup=true"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить бота в группу",
                    url=invite_url
                )
            ]
        ]
    )
    return keyboard# def selection_tags_button():
#     buttons = [
#         [types.InlineKeyboardButton(text="1", callback_data="random_questions_F_key")],
#         [types.InlineKeyboardButton(text="2", callback_data="help_F_key")]
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Функция для формирования клавиатуры с тегами
def create_tags_keyboard(tags):
    keyboard = InlineKeyboardMarkup(row_width=2)  # Размещаем кнопки по 2 в строке
    for tag in tags:
        button = InlineKeyboardButton(tag.tag_name, callback_data=f"tag_{tag.tag_id}")
        keyboard.add(button)
    
    return keyboard



def Tag_key():
    buttons = [
        [types.InlineKeyboardButton(text="Философия", callback_data="F_Philosophy")],
        [types.InlineKeyboardButton(text="О жизни", callback_data="F_Life")],
        [types.InlineKeyboardButton(text="Отдых и досуг", callback_data="F_rest")],
        [types.InlineKeyboardButton(text="Отношения", callback_data="F_Relationship")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
    

def tag_reply_key():
    kb = [
        [
            types.KeyboardButton(text="🚀 Новый вопрос")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
    return keyboard

def Relationship_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="🌶️", callback_data="P_1")],
        [types.InlineKeyboardButton(text="🌶️🌶️", callback_data="P_2")],
        [types.InlineKeyboardButton(text="🌶️🌶️🌶️", callback_data="P_3")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
