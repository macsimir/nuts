from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocketDisconnect

app = FastAPI()

# Хранение подключений
class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.get("/")
async def get():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WebSocket Client</title>
    </head>
    <body>
        <h1>WebSocket Client</h1>
        <input type="text" id="messageInput" placeholder="Введите сообщение" />
        <button onclick="sendMessage()">Отправить</button>
        <div id="messages"></div>

        <script>
            const ws = new WebSocket("ws://localhost:9000/ws");

            ws.onopen = () => {
                console.log("Соединение установлено");
            };

            ws.onmessage = (event) => {
                const messagesDiv = document.getElementById("messages");
                const messageElement = document.createElement("p");
                messageElement.textContent = event.data;
                messagesDiv.appendChild(messageElement);
            };

            ws.onclose = () => {
                console.log("Соединение закрыто");
            };

            function sendMessage() {
                const input = document.getElementById("messageInput");
                const message = input.value;
                ws.send(message);
                input.value = "";
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Вы сказали: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Клиент отключился")
