from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from web.database import Base, engine, SessionLocal, Message, init_db
from typing import List
import json

app = FastAPI()

# Инициализация базы данных
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()
templates = Jinja2Templates(directory="web/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    Messages = db.query(Message).all()
    messagss = [{"text": message.text} for message in Messages]
    return templates.TemplateResponse("index.html", {"request": request, "message": messagss})

@app.get("/message", response_class=HTMLResponse)
def get_chat(request: Request):
    return templates.TemplateResponse("chat_with_video.html", {"request": request})

@app.get("/messages")
def get_all_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return [{"text": message.text} for message in messages]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            parsed_data = json.loads(data)

            if parsed_data['type'] == 'chat':
                new_message = Message(text=f"{parsed_data['name']}: {parsed_data['text']}")
                db.add(new_message)
                db.commit()
                db.refresh(new_message)

                await manager.broadcast(json.dumps({
                    "type": "chat",
                    "text": new_message.text
                }))
            elif parsed_data['type'] == 'video':
                await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

