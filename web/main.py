from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://nuts-g6i3.onrender.com/"],  # Укажите допустимые домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="web/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request, db: Session = Depends(get_db)):
#     Messages = db.query(Message).all()
#     messagss = [{"text": message.text} for message in Messages]
#     return templates.TemplateResponse("index.html", {"request": request, "message": messagss})

