from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import random 
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    privilege = Column(String)

    @classmethod
    def telegram_id_exists(cls, session, telegram_id):
        return session.query(cls).filter(cls.telegram_id == telegram_id).first() is not None

class UserTag(Base):
    __tablename__ = 'user_tags'
    telegram_id_user = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.tag_id'), primary_key=True)

class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(Text)
    tag_question = Column(Integer, ForeignKey("tag.tag_id"))
    tag = relationship("Tag")

class UserQuestion(Base):
    __tablename__ = 'user_questions'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'), primary_key=True)
    asked = Column(Boolean, default=False)

class Tag(Base):
    __tablename__ = "tag"
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_text = Column(Text)

engine = create_engine('sqlite:///DATEBASE.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_random_question_by_tag(session):
    tag_id = 1
    questions = session.query(Question).filter(Question.tag_question == tag_id).all()
    if not questions:
        return None  # Если вопросов нет, возвращаем None
    random_question = random.choice(questions)
    return random_question.question_text


def get_random_tag(session):
    tag_count = session.query(Tag).count()
    if tag_count == 0:
        return None
    random_tag_id = random.randint(1, tag_count)
    return session.query(Tag).filter_by(tag_id=random_tag_id).first()


def get_user_by_telegram_id(telegram_id, session):
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    return user
async def create_new_user(session, telegram_id):
    privilege = "user"
    new_user = User(telegram_id=telegram_id, privilege=privilege)
    try:
        session.add(new_user)
        session.commit()
        print(f"User {telegram_id} created successfully")
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {str(e)}")

def create_tag(session):
    """Создание таблицы тегов"""
    tags_list = [
        "Философия",
        "Жизнь",
        "Отношения_1",
        "Отдых и досуг",
        "Отношения_2",
        "Отношения_3",
    ]
    for tag_text in tags_list:
        tag = Tag(tag_text=tag_text)
        session.add(tag)
    session.commit()
    session.close()

def get_user_by_telegram_id(session, telegram_id):
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    return user

if __name__ == "__main__":
    # Создаем сессию для взаимодействия с БД
    session = Session()

    try:
        # Проверяем, создана ли таблица users
        users_exist = session.query(User).first()
        if users_exist:
            print("Таблица users создана.")
        else:
            print("Таблица users не создана.")
    except Exception as e:
        print(f"Ошибка при проверке таблицы users: {e}")
    
    try:
        # Проверяем, создана ли таблица questions
        questions_exist = session.query(Question).first()
        if questions_exist:
            print("Таблица questions создана.")
        else:
            print("Таблица questions не создана.")
    except Exception as e:
        print(f"Ошибка при проверке таблицы questions: {e}")

    try:
        # Проверяем, создана ли таблица user_questions
        user_questions_exist = session.query(UserQuestion).first()
        if user_questions_exist:
            print("Таблица user_questions создана.")
        else:
            print("Таблица user_questions не создана.")
    except Exception as e:
        print(f"Ошибка при проверке таблицы user_questions: {e}")

    try:
        create_tag(session=session)
        print("Таблица с тегами создана ")
    except Exception as e:
        print(f"Ошибка при проверке таблицы user_questions: {e}")