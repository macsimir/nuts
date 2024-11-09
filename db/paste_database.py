from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
from DATABASE import Tag,Question

Base = declarative_base()
user_agent = UserAgent()
headers = {
    "Accept": "*/*",
    "User-Agent": user_agent.random  # Call the method to get a random user agent
}

engine = create_engine('sqlite:///DATEBASE.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()




class PhilosophyQuestionExtractor:
    def __init__(self, tag, session):
        self.tag = tag
        self.session = session

    def fetch_questions_from_source_4(self):
        """Извлечение вопросов из первого источника."""
        url = "https://mensby.com/women/relations/interesnye-voprosy-dlja-razmyshlenija-list-voprosov-na-filosofskie-temy"
        headers = {"User-Agent": "Mozilla/5.0"}
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        questions = soup.find_all("p")

        self._save_questions(questions[12:-11])

    def fetch_questions_from_source_5(self):
        """Извлечение вопросов из второго источника."""
        url = "https://saytpozitiva.ru/filosofskiye-voprosy.html"
        headers = {"User-Agent": "Mozilla/5.0"}
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        questions = soup.find_all("li")

        self._save_questions(questions[15:-50], source=5)

    def _save_questions(self, questions, source=None):
        """Сохранение вопросов в файл и базу данных."""
        with open("test.txt", "a") as file:
            for i in questions:
                question_text = i.text.strip()

                # Удаляем номер вопроса, если он есть
                cleaned_question = re.sub(r'^\d+\.\s*', '', question_text)
                if source == 5:
                    # Удаление текста в скобках для второго источника
                    cleaned_question = re.sub(r'\([^)]*\)', '', cleaned_question).strip()

                # Создание объекта Question и добавление в базу данных
                question = Question(question_text=cleaned_question, tag_question=self.tag.tag_id)
                self.session.add(question)
                self.session.commit()

                print(f"Добавлен вопрос - {cleaned_question}")

def create_philosophy_questions(session):
    tag = session.query(Tag).filter_by(tag_text="Философия").first()
    extractor = PhilosophyQuestionExtractor(tag, session)
    extractor.fetch_questions_from_source_4()
    extractor.fetch_questions_from_source_5()
create_philosophy_questions(session)


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

def create_life_q():
    for i in questions_about_past:
        new_q = Question(question_text =i , tag_question=2)
        session.add(new_q)
        session.commit()
create_life_q()