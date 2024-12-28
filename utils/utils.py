from db.DATABASE import Session,User,Question, UserQuestion
import random


async def random_questions_F_funck(callback, tag_id):
    session = Session()
    user_telegram_id = callback.message.chat.id
    user = session.query(User).filter_by(telegram_id=user_telegram_id).first()
    if user is None:
        await callback.message.answer("Пользователь не найден в базе данных.")
        session.close()
        return    
    questions_with_tag = session.query(Question).filter_by(tag_question=tag_id).all()    
    if not questions_with_tag:
        await callback.message.answer("Нет доступных вопросов для этого тега.")
        session.close()
        return
    question = None
    user_question = None
    while not question or user_question:
        question = random.choice(questions_with_tag)
        user_question = session.query(UserQuestion).filter_by(user_id=user.user_id, question_id=question.question_id).first()

    user_question = UserQuestion(user_id=user.user_id, question_id=question.question_id, asked=True)
    session.add(user_question)
    session.commit()
    
    question_message = await callback.message.answer(question.question_text)
    session.close()


def convert_google_drive_link_preview(link):
    if "drive.google.com/file/d/" in link:
        file_id = link.split("file/d/")[1].split("/view")[0]
        preview_link = f"https://drive.google.com/file/d/{file_id}/preview"
        return preview_link
    else:
        return "Неправильный формат ссылки Google Drive"
convert_google_drive_link_preview(link="    ")



questions_about_past = [
    "Какое у тебя самое яркое детское воспоминание?",
    "Какие традиции вашей семьи были для тебя важны в детстве?",
    "Какое событие в школе запомнилось тебе больше всего?",
    "Какие увлечения у тебя были в юности?",
    "Что ты помнишь о своих первых друзьях?",
    "Какие уроки ты вынес из своих подростковых лет?",
    "Какой был твой первый опыт работы?",
    "Как ты провел свои летние каникулы в детстве?",
    "Какую роль в твоем воспитании сыграли родители?",
    "Какой самый запоминающийся праздник ты отмечал в детстве?",
    "Какие страхи или переживания ты испытывал в молодости?",
    "Какой совет, полученный в прошлом, ты считаешь особенно важным?",
    "Что изменилось в твоем восприятии мира с тех пор, как ты был моложе?",
    "Какое место или город оставили в твоем сердце наилучшие воспоминания?",
    "Какие книги или фильмы повлияли на твое мировоззрение в молодости?",
    "Как ты познакомился с первым человеком, который стал важен для тебя?",
    "Какой навык или хобби ты бы хотел развить в прошлом?",
    "Какие события или обстоятельства повлияли на твой жизненный путь?",
    "Как ты справлялся с трудными периодами в своей жизни?",
    "Какое наследие ты хотел бы оставить своим детям или близким?"
]
