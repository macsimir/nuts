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

