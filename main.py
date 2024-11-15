# main.py
import logging
import asyncio
from utils.config import dp, bot

logging.basicConfig(level=logging.INFO)

async def start_bot():
    from handlers.users import start, random_question,view_video # импортируем все обработчики
    from handlers.admin import admin_panel
    await dp.start_polling(bot)

async def start_web_app():
    from web.app import app
    import uvicorn
    config = uvicorn.Config(
        app,
        host="0.0.0.0",  # или 0.0.0.0 для общедоступного доступа
        port=1000,
        log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    # Создаем задачи для бота и веб-приложения
    bot_task = asyncio.create_task(start_bot())
    web_task = asyncio.create_task(start_web_app())
    # Дожидаемся завершения обеих задач
    await asyncio.gather(bot_task, web_task)

if __name__ == "__main__":
    print("Запуск бота и FastAPI сервера...")
    asyncio.run(main())
