from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

# Создаем экземпляр FastAPI
app = FastAPI()

# Настраиваем Jinja2 для шаблонов
templates = Jinja2Templates(directory="web/templates")

# Маршрут для отображения HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
