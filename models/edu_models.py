from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    Text,
    DateTime,
    ForeignKey,
    Table,
    JSON,
)
from sqlalchemy.orm import relationship
from modules.db import Base
from modules.db import ENGINE


class EduUserModel(Base):
    __tablename__ = "edu_user"
    idx = Column(Integer, primary_key=True)
    userid = Column(String(30), unique=True, nullable=False)
    usertype = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    current_classroom = Column(Integer, nullable=False)


class EduSubjectModel(Base):
    __tablename__ = "edu_subject"
    idx = Column(Integer, primary_key=True)
    subject_title = Column(String(100), nullable=True)
    subject_main_idea = Column(Text, nullable=True)
    subject_main_1 = Column(Text, nullable=True)
    subject_main_2 = Column(Text, nullable=True)
    subject_main_3 = Column(Text, nullable=True)
    subject_goal = Column(Text, nullable=True)
    subject_goal_detail = Column(Text, nullable=True)


class EduObjectModel(Base):
    __tablename__ = "edu_object"
    idx = Column(Integer, primary_key=True)
    subject_idx = Column(Integer, ForeignKey("edu_subject.idx"), nullable=False)
    object_title = Column(String(100), nullable=False)
    object_detail = Column(Text, nullable=True)


class EduProblemModel(Base):
    __tablename__ = "edu_problem"
    idx = Column(Integer, primary_key=True)
    object_idx = Column(Integer, ForeignKey("edu_object.idx"), nullable=False)
    problem_level = Column(Integer, nullable=False)
    problem_answer: list = Column(JSON, nullable=True)
    problem_question = Column(Text, nullable=True)
    problem_content = Column(Text, nullable=True)
    problem_result = Column(Text, nullable=True)
    level_1_selection_answer = Column(String(300), nullable=True)
    level_1_selection_1 = Column(String(300), nullable=True)
    level_1_selection_2 = Column(String(300), nullable=True)
    level_1_selection_3 = Column(String(300), nullable=True)
    level_2_initcodes = Column(Text, nullable=True)
    level_2_num_of_answers = Column(Integer, nullable=True)
    level_2_answer_1: list = Column(JSON, nullable=True)
    level_2_answer_2: list = Column(JSON, nullable=True)
    level_2_answer_3: list = Column(JSON, nullable=True)
    level_2_answer_4: list = Column(JSON, nullable=True)
    level_2_answer_5: list = Column(JSON, nullable=True)
    level_2_scores_precent: list = Column(JSON, nullable=True)
    level_3_initcodes = Column(Text, nullable=True)


class EduClassroomModel(Base):
    __tablename__ = "edu_classroom"
    idx = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    object_idx = Column(Integer, ForeignKey("edu_object.idx"), nullable=False)
    previous_classroom_idx = Column(Integer, nullable=False)
    # JSON 에러 해결 https://hello-bryan.tistory.com/558
    level_1_num_of_problems = Column(Integer, default=0)
    level_2_num_of_problems = Column(Integer, default=0)
    level_3_num_of_problems = Column(Integer, default=0)
    level_1_problems: list = Column(JSON, nullable=True)
    level_2_problems: list = Column(JSON, nullable=True)
    level_3_problems: list = Column(JSON, nullable=True)
    level_1_problems_scores: list = Column(JSON, nullable=True)
    level_2_problems_scores: list = Column(JSON, nullable=True)
    level_3_problems_scores: list = Column(JSON, nullable=True)
    total_score = Column(Integer, default=0)
    score_is_show = Column(Integer, default=0)


class EduMyClassroomModel(Base):
    __tablename__ = "edu_my_classroom"
    idx = Column(Integer, primary_key=True)
    userid = Column(String(30), nullable=False)
    classroom_idx = Column(Integer, ForeignKey("edu_classroom.idx"), nullable=False)
    current_problem_seq = Column(Integer, nullable=True, default=0)
    classroom_status = Column(Integer, nullable=True, default=0)
    time_goal_at = Column(DateTime, nullable=True, default=None)
    time_goal_status = Column(Integer, nullable=True, default=0)
    time_goal = Column(DateTime, nullable=True, default=None)
    time_goal_delay: list = Column(JSON, nullable=True, default=[])
    chatgpt: list = Column(JSON, nullable=True, default=[])
    chatgpt_dialog: list = Column(JSON, nullable=True, default=[])
    created_at = Column(DateTime, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None)


class EduMyAnswerModel(Base):
    __tablename__ = "edu_my_answer"
    idx = Column(Integer, primary_key=True)
    userid = Column(String(30), nullable=False)
    classroom_idx = Column(Integer, ForeignKey("edu_classroom.idx"), nullable=False)
    problem_seq = Column(Integer, nullable=False)
    problem_idx = Column(Integer, nullable=False)
    selection_list: list = Column(JSON, nullable=True)
    answer: list = Column(JSON, nullable=True)
    is_correct: list = Column(JSON, nullable=True)
    is_correct_teacher: list = Column(JSON, nullable=True)
    answer_status = Column(Integer, nullable=True)
    comment_to_student = Column(JSON, nullable=True)
    memo_from_teacher = Column(JSON, nullable=True)
    particial_score = Column(Integer, default=0)
    answer_score = Column(Integer, default=0)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

# Base.metadata.create_all(bind=ENGINE)
