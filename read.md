Запрос для нейросети, чтобы описать задачу и получить помощь с функционалом, может выглядеть следующим образом:

---

**Описание задачи:**

Мне нужно реализовать Telegram-бота на базе библиотеки Aiogram 3.0, который выполняет следующий функционал:

1. Бот создает комнату, доступную для пользователей чата после ввода команды `/create_room`.
   - Пользователи могут войти в комнату или выйти из нее в любой момент через кнопки.
   - Для этого используются inline-кнопки с действиями: «Войти в комнату» и «Выйти из комнаты».

2. После создания комнаты бот может отправлять каждому участнику комнаты вопросы через личные сообщения (команда `/ask_questions`).
   - Вопросы отправляются только тем, кто вошел в комнату.
   - Если участников комнаты меньше 2, бот уведомляет, что опрос невозможен.

3. Когда пользователь отвечает на вопрос в личном чате с ботом, его ответ автоматически выводится в общий групповой чат, откуда была создана комната.

**Дополнительные детали:**
- Обработчик состояний (`FSMContext`) используется для отслеживания ответов пользователей.
- Ответы пользователей отправляются в общий чат с указанием имени пользователя, чтобы остальные видели их ответы.
- Если что-то идет не так (например, бот не может отправить сообщение), обрабатываются исключения.
