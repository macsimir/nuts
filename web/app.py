from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketState
from typing import List, Dict
from utils.utils import convert_google_drive_link_preview  # Проверьте, что этот файл и функция существуют

app = FastAPI()

# Подключаем папку static для работы с CSS и JS
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# Настраиваем Jinja2 для шаблонов
templates = Jinja2Templates(directory="web/templates")


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Маршрут для чата с указанием комнаты
@app.get("/rooms/{id_room}", response_class=HTMLResponse)
async def get_chat_room(request: Request, id_room: int):
    return templates.TemplateResponse("index.html", {"request": request, "id_room": id_room})

