// static/chat.js

// Получаем ID комнаты из URL
const roomId = window.location.pathname.split("/").pop();
const ws = new WebSocket(`ws://${window.location.host}/ws/rooms/${roomId}`);

// Обработка входящих сообщений
ws.onmessage = function (event) {
    const messageContainer = document.getElementById("message-container");
    const message = document.createElement("div");
    message.textContent = event.data;
    messageContainer.appendChild(message);
    messageContainer.scrollTop = messageContainer.scrollHeight; // Прокручиваем вниз
};

// Отправка сообщений
function sendMessage() {
    const input = document.getElementById("messageInput");
    if (input.value) {
        ws.send(input.value);
        input.value = '';
    }
}
