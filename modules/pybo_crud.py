from models import *
from schemas import *
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime
from passlib.context import CryptContext


def pybo_get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(PyboQuestionModel)\
        .order_by(PyboQuestionModel.create_date.desc())\
        .order_by(PyboQuestionModel.subject.desc())

    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list  # 전체 개수, 페이징 적용된 질문 목록


def pybo_get_question(db: Session, question_idx: int):
    question = db.query(PyboQuestionModel).get(question_idx)
    return question


def pybo_create_answer(
        db: Session,
        question: PyboQuestionModel,
        answer_create: PyboAnswerCreateSchema,
        user: PyboUserModel):
    db_answer = PyboAnswerModel(
        question=question,
        content=answer_create.content,
        create_date=datetime.now(),
        user=user)
    db.add(db_answer)
    db.commit()


def pybo_create_question(
        db: Session,
        question_create: PyboQuestionCreateSchema,
        user: PyboUserModel):
    db_question = PyboQuestionModel(
        subject=question_create.subject,
        content=question_create.content,
        create_date=datetime.now(),
        user=user)
    db.add(db_question)
    db.commit()


def pybo_make_db(db: Session):
    user1 = pybo_get_user(db, 'test1')
    user2 = pybo_get_user(db, 'test2')
    for i in range(5):
        # subject = f'테스트 데이터 {i+1:03d}'
        # print(subject)
        if i < 3:
            q = PyboQuestionModel(
                subject=f'테스트 데이터 {i+1:03d}',
                content=f'내용없음 {i+1:03d}',
                create_date=datetime.now(),
                user=user1)
            db.add(q)
        else:
            q = PyboQuestionModel(
                subject=f'테스트 데이터 {i+1:03d}',
                content=f'내용없음 {i+1:03d}',
                create_date=datetime.now(),
                user=user2)
            db.add(q)
    db.commit()


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def pybo_create_user(db: Session, user_create: PyboUserCreateSchema):
    db_user = PyboUserModel(
        username=user_create.username,
        password=pwd_context.hash(user_create.password1),
        email=user_create.email
    )
    db.add(db_user)
    db.commit()


def pybo_get_existing_user(db: Session, user_create: PyboUserCreateSchema):
    return db.query(PyboUserModel).filter(
        (PyboUserModel.username == user_create.username) |
        (PyboUserModel.email == user_create.email)
    ).first()


def pybo_get_user(db: Session, username: str):
    return db.query(PyboUserModel).filter(PyboUserModel.username == username).first()


def pybo_update_question(
        db: Session,
        db_question: PyboQuestionModel,
        question_update: PyboQuestionUpdateSchema):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    # db.add(db_question)
    db.commit()


def pybo_delete_question(db: Session, db_question: PyboQuestionModel):
    db.delete(db_question)
    db.commit()


def pybo_get_answer(db: Session, answer_idx: int):
    return db.query(PyboAnswerModel).get(answer_idx)


def pybo_update_answer(
        db: Session,
        db_answer: PyboAnswerModel,
        answer_update: PyboAnswerUpdateSchema):
    db_answer.content = answer_update.content
    db_answer.modify_date = datetime.now()
    db.commit()


def pybo_delete_answer(db: Session, db_answer: PyboAnswerModel):
    db.delete(db_answer)
    db.commit()


def pybo_vote_question(
        db: Session, db_question: PyboQuestionModel, db_user: PyboUserModel):
    db_question.voter.append(db_user)
    db.commit()


def pybo_vote_answer(
        db: Session, db_answer: PyboAnswerModel, db_user: PyboUserModel):
    db_answer.voter.append(db_user)
    db.commit()


def pybo_get_search_list(db: Session, skip: int = 0, limit: int = 0, keyword: str = ''):
    search_list = db.query(PyboQuestionModel)
    if keyword:
        search = f'%%{keyword}%%'
        sub_query = db.query(PyboAnswerModel.question_idx, PyboAnswerModel.content, PyboUserModel.username)\
            .outerjoin(PyboUserModel, and_(PyboAnswerModel.user_idx == PyboUserModel.idx)).subquery()
        search_list = search_list\
            .outerjoin(PyboUserModel)\
            .outerjoin(sub_query, and_(sub_query.c.question_idx == PyboQuestionModel.idx))\
            .filter(
                PyboQuestionModel.subject.ilike(search) |  # 질문제목
                PyboQuestionModel.content.ilike(search) |  # 질문내용
                PyboUserModel.username.ilike(search) |  # 질문작성자
                sub_query.c.content.ilike(search) |  # 답변내용
                sub_query.c.username.ilike(search)  # 답변작성자
            )
    total = search_list.distinct().count()
    search_list = search_list.order_by(PyboQuestionModel.create_date.desc())\
        .offset(skip).limit(limit).distinct().all()
    return total, search_list
