from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio
from utils.config import BOT_TOKEN
# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Новости", url="https://example.com/news"),
            InlineKeyboardButton(text="Отзывы", url="https://example.com/reviews"),
        ]
    ])
    
    # Отправляем сообщение с фото
    photo_url = "Ссылка_на_ваше_изображение"  # Например, загрузите изображение в телеграм и используйте его ссылку
    caption = (
        "🔥 Покупай GOLD — Готовься к Праздникам!\n\n"
        "💰 Лучшая ЦЕНА и быстрые ВЫВОДЫ.\n"
        "✅ Все способы оплаты будут доступны к праздникам!\n"
        "⚡ Успей пополнить баланс выгодно.\n\n"
        "Жми /start"
    )
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=caption, reply_markup=keyboard)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp, skip_updates=True)
