import logging
import asyncio
from utils.config import dp, bot

logging.basicConfig(level=logging.INFO)

async def start_bot():
    from handlers.users import start, random_question, view_video
    from handlers.admin import admin_panel
    logging.info("Starting Telegram bot...")
    await dp.start_polling(bot)

async def start_web_app():
    from tests.main import app
    # from web.main import app
    import uvicorn
    logging.info("Starting FastAPI server...")
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=9000,
        log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    bot_task = asyncio.create_task(start_bot())
    web_task = asyncio.create_task(start_web_app())
    await asyncio.gather(bot_task, web_task)

if __name__ == "__main__":
    logging.info("Launching bot and FastAPI server...")
    asyncio.run(main())
