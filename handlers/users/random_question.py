from aiogram import types, F
from aiogram.filters import Command
from utils.config import dp,bot
from db.DATABASE import User, Question, UserQuestion, Session, Tag,create_new_user,get_user_by_telegram_id,get_random_question_by_tag, UserTag
from handlers.users.keyboard import random_question_button,get_invite_button , Tag_key, tag_reply_key, Relationship_keyboard
from utils.utils import random_questions_F_funck
import random


@dp.callback_query(F.data == "random_questions_F_key")
async def random_questions_F_funck(callback: types.CallbackQuery):
    await callback.message.delete()
    session = Session() 
    user_id = callback.message.chat.id
    user = get_user_by_telegram_id(telegram_id=user_id, session=session)
    telegram_id = callback.message.chat.id
    

    user = session.query(User).filter_by(telegram_id=telegram_id).first()

    if callback.message.chat.type == "private":
        keyboard = await get_invite_button(bot)  # Передаем bot как аргумент
        await callback.message.answer("Нажмите кнопку ниже, чтобы добавить бота в группу как администратора:", reply_markup=keyboard)
    else:
        if user:
            await callback.message.answer(
                "Привет, о чем сегодня хотите поговорить?",
                reply_markup=Tag_key()
            )
        else:
            new_user = User(telegram_id=telegram_id, privilege="User")
            session.add(new_user)
            session.commit()
            create_new_user(session=session, telegram_id=user_id)
            await callback.message.answer(
                "Привет, о чем сегодня хотите поговорить?",
                reply_markup=Tag_key()
            )
    # await callback.message.answer("Текст")



@dp.callback_query(F.data.startswith("F_"))
async def callbacks_num(callback: types.CallbackQuery):
    await callback.message.delete()
    action = callback.data.split("_")[1]

    if action == "Philosophy":
        await callback.message.answer('Теперь вам будут выводиться философские вопросы! 🧠✨ \n И наконец-то вы сможете блеснуть своим философским духом друг с другом! 🤔💬 \nЧтобы получить новый вопрос, просто нажмите на кнопку "Новый вопрос"!')
        await random_questions_F_funck(callback=callback,tag_id=1)
    elif action == "Life":
        await callback.message.answer("Жизнь")
        await random_questions_F_funck(callback=callback,tag_id=2)
    elif action == "rest":
        await callback.message.answer("Отдых и досуг")
        await random_questions_F_funck(callback=callback,tag_id=3)
    elif action == "Relationship":
        await callback.message.answer("Выбери степень вопросов:", reply_markup=Relationship_keyboard())

        # await callback.message.answer("Отношения")
    #     await random_questions_F_funck(callback=callback,tag_id=4)
    await callback.answer()


def get_random_question_by_tag(session):
    tag_id = 1
    questions = session.query(Question).filter(Question.tag_question == tag_id).all()
    if not questions:
        return None  # Если вопросов нет, возвращаем None
    random_question = random.choice(questions)
    return random_question.question_text
async def random_questions_F_funck(callback, tag_id, keyboard=None):
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

    try:
        session.add(user_question)
        session.commit()
        
        # Проверка на существование записи в UserTag
        existing_user_tag = session.query(UserTag).filter_by(telegram_id_user=user_telegram_id).first()
        
        if existing_user_tag:
            existing_user_tag.tag_id = tag_id
        else:
            new_user_tag = UserTag(telegram_id_user=user_telegram_id, tag_id=tag_id)
            session.add(new_user_tag)    

        session.commit()
        
        # Используем переданную клавиатуру, если она есть
        question_message = await callback.message.answer(question.question_text, reply_markup=tag_reply_key())
        
    except Exception as e:
        await callback.message.answer(f"Произошла ошибка: {str(e)}")
        session.rollback()
    finally:
        session.close()


@dp.message(F.text.lower() == "🚀 новый вопрос")
async def knopka_key_F_random(message: types.Message):
    session = Session()
    user_telegram_id = message.chat.id
    tag_to_user = session.query(UserTag).filter_by(telegram_id_user=user_telegram_id).first()
    tag_id = tag_to_user.tag_id
    user = session.query(User).filter_by(telegram_id=user_telegram_id).first()

    if user is None:
        await message.answer("Пользователь не найден в базе данных.")
        session.close()
        return    
    
    questions_with_tag = session.query(Question).filter_by(tag_question=tag_id).all()    
    if not questions_with_tag:
        await message.answer("Нет доступных вопросов для этого тега.")
        session.close()
        return

    question = None
    user_question = None
    while not question or user_question:
        question = random.choice(questions_with_tag)
        user_question = session.query(UserQuestion).filter_by(user_id=user.user_id, question_id=question.question_id).first()

    user_question = UserQuestion(user_id=user.user_id, question_id=question.question_id, asked=True)

    try:
        session.add(user_question)
        session.commit()
        
        # Проверка на существование записи в UserTag
        existing_user_tag = session.query(UserTag).filter_by(telegram_id_user=user_telegram_id).first()
        
        if existing_user_tag:
            existing_user_tag.tag_id = tag_id
        else:
            new_user_tag = UserTag(telegram_id_user=user_telegram_id, tag_id=tag_id)
            session.add(new_user_tag)    

        session.commit()
        
        # Используем переданную клавиатуру, если она есть
        question_message = await message.answer(question.question_text, reply_markup=tag_reply_key())
        
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")
        session.rollback()
    finally:
        session.close()