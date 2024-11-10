### Инструкция по сборке и запуску

1. Сохраните все файлы (`Dockerfile`, `requirements.txt`, `main.py`) в одну директорию.
2. Выполните сборку Docker образа:
   ```bash
   docker build -t aiogram-fastapi-bot .
   ```
3. Запустите контейнер:
   ```bash
   docker run -d -p 8000:8000 aiogram-fastapi-bot
   ```

FastAPI сервер будет доступен по адресу `http://localhost:8000`, а Telegram бот начнет работать параллельно с ним.