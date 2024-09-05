from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from modules.db import Base
from modules.db import ENGINE

question_voter = Table(
    'pybo_question_voter',
    Base.metadata,
    Column('user_idx', Integer, ForeignKey('pybo_user.idx'), primary_key=True),
    Column('question_idx', Integer, ForeignKey('pybo_question.idx'), primary_key=True)
)

answer_voter=Table(
    'pybo_answer_voter',
    Base.metadata,
    Column('user_idx', Integer, ForeignKey('pybo_user.idx'), primary_key=True),
    Column('answer_idx', Integer, ForeignKey('pybo_answer.idx'), primary_key=True)
)

class PyboQuestionModel(Base):
    __tablename__ = 'pybo_question'
    idx = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_idx = Column(Integer, ForeignKey('pybo_user.idx'), nullable=True)
    user = relationship('PyboUserModel', backref='question_users')
    modify_date = Column(DateTime, nullable=True)
    voter=relationship('PyboUserModel', secondary=question_voter, backref='question_voters')


class PyboAnswerModel(Base):
    __tablename__ = 'pybo_answer'
    idx = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_idx = Column(Integer, ForeignKey('pybo_question.idx'))
    question = relationship('PyboQuestionModel', backref='answers')
    user_idx = Column(Integer, ForeignKey('pybo_user.idx'), nullable=True)
    user = relationship('PyboUserModel', backref='answer_users')
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('PyboUserModel', secondary=answer_voter, backref='answer_voters')


class PyboUserModel(Base):
    __tablename__ = 'pybo_user'
    idx = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False)


Base.metadata.create_all(bind=ENGINE)
