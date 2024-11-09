from aiogram import types

def admin_panel_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Удалить вопрос", url="delete_q")],
        [types.InlineKeyboardButton(text="Добавить вопрос", callback_data="create_q")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
