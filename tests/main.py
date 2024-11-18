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

@app.get("/rooms/{room_id}", response_class=HTMLResponse)
async def get_room(request: Request, room_id: int, db: Session = Depends(get_db)):
    # Получаем сообщения только для указанной комнаты
    messages = db.query(Message).filter(Message.room_id == room_id).all()
    message_data = [{"text": message.text} for message in messages]

    return templates.TemplateResponse(
        "chat_with_video.html",
        {"request": request, "messages": message_data, "room_id": room_id}
    )


@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            parsed_data = json.loads(data)

            if parsed_data['type'] == 'chat':
                # Сохраняем сообщение в базу данных с привязкой к room_id
                new_message = Message(text=f"{parsed_data['name']}: {parsed_data['text']}", room_id=room_id)
                db.add(new_message)
                db.commit()

                # Отправляем сообщение всем клиентам комнаты
                await manager.broadcast(json.dumps({
                    "type": "chat",
                    "room_id": room_id,
                    "text": new_message.text
                }))
            elif parsed_data['type'] == 'video':
                await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
