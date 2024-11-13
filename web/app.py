from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.utils import convert_google_drive_link_preview
import uvicorn

# Создаем экземпляр FastAPI
app = FastAPI()

# Настраиваем Jinja2 для шаблонов
templates = Jinja2Templates(directory="web/templates")

# Маршрут для отображения HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/room", response_class=HTMLResponse)
async def room(request: Request):
    input_link = "https://drive.google.com/file/d/1f3ssRcCOhpYWbjMfBYInAJcpylrxHENo/view?usp=sharing"
    converted_link = convert_google_drive_link_preview(input_link)
    return templates.TemplateResponse("users_chat.html", {"request": request, "url":converted_link})
