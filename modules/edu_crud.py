# python libraries
import pickle
import datetime
import random
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from dotenv import dotenv_values
from openai import OpenAI

# user libraries
from models import (
    EduUserModel,
    EduSubjectModel,
    EduObjectModel,
    EduProblemModel,
    EduClassroomModel,
    EduMyClassroomModel,
    EduMyAnswerModel,
)
from schemas import (
    EduDevelopProblemSchema,
    EduUserCreateScheme,
    EduUserUpdateScheme,
    EduUserMyClassroomUpdateScheme,
    EduUserMyClassroomScheme,
    EduUserAnswerScheme,
    EduDevelopClassroomSchema,
)

pwd_context_edu = CryptContext(schemes=["bcrypt"], deprecated="auto")

config = dotenv_values(".env")

openai = OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

'''
with open("./modules/subject_list_dump.pickle", "rb") as f:
subject_list_dump = pickle.load(f)

subject_list_dump = [
    {
        "idx": 1,
        "subject_title": "파이썬 프로그래밍 기초 Part 1",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 2,
        "subject_title": "파이썬 프로그래밍 기초 Part 2",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 3,
        "subject_title": "알고리즘과 프로그래밍 Part 1",
        "subject_main_idea": """- 문제를 효율적으로 해결하기 위해서는 문제를 추상화하고, 프로그래밍을 위한 알고리즘을 설계한다.
- 데이터 모델링을 하기 위해 문제 해결에 필요한 데이터 간의 관계를 분석하고, 정의한다.
- 프로그래밍을 통한 자동화는 다양한 학문 분야의 문제를 해결하는 데 도움을 준다.""",
        "subject_main_1": """- 문제 분해와 모델링
- 정렬, 탐색 알고리즘
- 자료형
- 표준입출력과 파일입출력
- 다차원 데이터 활용
- 제어 구조의 응용
- 클래스와 인스턴스""",
        "subject_main_2": """- 문제를 분해하고 모델링하기
- 알고리즘의 수행 과정 및 효율성 비교 · 분석하기
- 문제 해결에 적합한 자료형과 입출력 구조를 활용하여 프로그램 작성하기
- 복잡한 문제를 해결하기 위해 제어 구조와 다차원 데이터 구조를 복합적으로 활용하기
- 클래스를 정의하고 인스턴스를 생성하여 문제 해결에 적합한 객체를 구현하기""",
        "subject_main_3": """- 문제 해결 모델을 구성하고 적극적으로 표현하는 자세
- 알고리즘 효율의 가치와 영향력을 인식하고 적극적으로 탐구하는 태도
- 다양한 학문 분야의 문제 해결을 위해 설계한 알고리즘을 프로그램으로 구현하는 실천적 자세
- 디지털 사회의 민주시민으로서 협력적 문제 해결력의 중요성을 인식하는 자세""",
        "subject_goal": """1. 복잡한 문제를 해결 가능한 작은 문제로 분해하고 모델링한다.
2. 데이터를 정렬하는 다양한 알고리즘의 특징과 효율을 비교 · 분석한다.
3. 데이터를 탐색하는 다양한 알고리즘의 특징과 효율을 비교 · 분석한다.
4. 자료형의 종류와 특성을 알고, 접합한 자료형을 선택하여 프로그램을 작성한다.
5. 표준입출력과 파일입출력을 활용한 프로그램을 작성한다.
6. 다차원 데이터 구조를 활용한 프로그램을 작성한다.
7. 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.
8. 객체를 구현하는 클래스와 인스턴스를 활용하여 프로그램을 작성한다.
9. 실생활 및 다양한 학문 분야의 문제 해결을 위한 프로그램을 협력적으로 설계 · 구현한다.
10. 문제 해결을 위한 프로그램의 성능을 평가하고 공유한다.""",
        "subject_goal_detail": """- 복잡한 문제를 분석하는 단계에서 좀 더 작은 문제로 분해하는 과정을 수행하며, 해결하기 용이하도록 단순화나 구조화하는 모델링 단계를 수행할 수 있어야 한다. 작은 문제의 해결 결과를 종합하는 과정에서 작은 문제를 모두 수행했을 때 전체 문제 해결이 원활하게 이루어지는지, 오류가 없는지를 확인할 수 있어야 한다.
- 여러 가지 정렬, 탐색 알고리즘을 적용하여 실생활의 간단한 데이터의 정렬, 탐색 문제를 해결할 수 있어야 한다. 정렬, 탐색 알고리즘의 수행 과정을 분석해보고 문제에 따라 알고리즘의 효율성이 다를 수 있음을 설명할 수 있어야 한다.
- 실생활의 사례를 활용하여 객체 지향의 기본 개념을 이해하고 필요성을 설명할 수 있어야 한다. 클래스와 객체를 생성하고 문제 해결을 위한 프로그램 구현에 활용할 수 있어야 한다.""",
    },
    {
        "idx": 4,
        "subject_title": "알고리즘과 프로그래밍 Part 2",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 5,
        "subject_title": "인공지능 Part 1",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 6,
        "subject_title": "인공지능 Part 2",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
]

with open("./modules/object_list_dump.pickle", "rb") as f:
    object_list_dump = pickle.load(f)

with open("./modules/problem_list_dump.pickle", "rb") as f:
    problem_list_dump = pickle.load(f)

with open("./modules/classroom_list_dump.pickle", "rb") as f:
    classroom_list_dump = pickle.load(f)

with open("./modules/my_classroom_list_dump.pickle", "rb") as f:
    my_classroom_list_dump = pickle.load(f)

classroom_list_dump = [
    {
        "idx": 1,
        "title": "변수와 자료형의 이해와 활용",
        "object_idx": 1,
        "previous_classroom_idx": 0,
        "level_1_problems": [1, 2, 3, 4],
        "level_2_problems": [6, 7, 8, 9],
        "level_3_problems": [11, 12],
    },
    {
        "idx": 2,
        "title": "연산자의 이해와 활용",
        "object_idx": 2,
        "previous_classroom_idx": 1,
        "level_1_problems": [16, 17, 18, 19],
        "level_2_problems": [21, 22, 23, 24],
        "level_3_problems": [26, 27],
    },
    {
        "idx": 3,
        "title": "선택 제어문의 이해와 활용",
        "object_idx": 3,
        "previous_classroom_idx": 2,
        "level_1_problems": [31, 32, 33, 34],
        "level_2_problems": [36, 37, 38, 39],
        "level_3_problems": [41, 42],
    },
    {
        "idx": 4,
        "title": "반복 제어문의 이해와 활용",
        "object_idx": 4,
        "previous_classroom_idx": 3,
        "level_1_problems": [46, 47, 48, 49],
        "level_2_problems": [51, 52, 53, 54],
        "level_3_problems": [56, 57],
    },
]
my_classroom_list_dump = [
    {
        "idx": 4,
        "userid": "user1",
        "classroom_idx": 4,
        "current_problem_seq": 1,
        "answers": {},
        "created_at": "2024-04-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 1,
        "userid": "user1",
        "classroom_idx": 1,
        "current_problem_seq": 1,
        "created_at": "2024-02-25 22:22:22",
        "updated_at": "",
    },
    {
        "idx": 2,
        "userid": "user1",
        "classroom_idx": 3,
        "created_at": "2024-03-25 00:00:00",
        "updated_at": "",
    },
    {
        "idx": 3,
        "userid": "user2",
        "classroom_idx": 3,
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
]

my_answer_list_dump = [
    {
        "idx": 1,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 1,
        "problem_idx": 46,
        "selection_list": [1, 0, 2, 3],
        "answer": ["2"],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 2,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 2,
        "problem_idx": 47,
        "selection_list": [1, 2, 3, 0],
        "answer": [],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 3,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 3,
        "problem_idx": 48,
        "selection_list": [2, 3, 0, 1],
        "answer": [],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 4,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 4,
        "problem_idx": 49,
        "selection_list": [0, 3, 1, 2],
        "answer": [],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 5,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 5,
        "problem_idx": 51,
        "selection_list": [],
        "answer": ["i in range(1, 101)", "total += i"],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 6,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 6,
        "problem_idx": 52,
        "selection_list": [],
        "answer": ["i <= 100", "total += i"],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 7,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 7,
        "problem_idx": 53,
        "selection_list": [],
        "answer": [],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 8,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 8,
        "problem_idx": 54,
        "selection_list": [],
        "answer": [],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 9,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 9,
        "problem_idx": 56,
        "selection_list": [],
        "answer": [
            """point = 0
total = 0
for i in range(1, 21, 1):
    text = str(i) + '회 다트 점수를 입력하세요: '
    point = input(text)
    point = int(point)
"""
        ],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
    {
        "idx": 10,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 10,
        "problem_idx": 57,
        "selection_list": [],
        "answer": [],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",
    },
]
'''


def edu_get_existing_user(db: Session, user_create: EduUserCreateScheme):
    print('#'*30)
    print(user_create.userid, user_create.email)
    print('#'*30)
    return (
        db.query(EduUserModel)
        .filter(
            (EduUserModel.userid == user_create.userid)
            | (EduUserModel.email == user_create.email)
        )
        .first()
    )


def edu_create_user(db: Session, user_create: EduUserCreateScheme):
    db_user = EduUserModel(
        userid=user_create.userid,
        usertype=user_create.usertype,
        password=pwd_context_edu.hash(user_create.password1),
        username=user_create.username,
        email=user_create.email,
        current_classroom=user_create.current_classroom,
    )
    db.add(db_user)
    db.commit()


def edu_get_user(db: Session, userid: str):
    return db.query(EduUserModel).filter(EduUserModel.userid == userid).first()


def edu_update_user(
    db: Session, db_user: EduUserModel, user_update: EduUserUpdateScheme
):
    print("def edu_update_user")
    db_user.username = user_update.username
    db_user.email = user_update.email
    db_user.current_classroom = user_update.current_classroom
    if user_update.password1.strip() != "":
        db_user.password = pwd_context_edu.hash(user_update.password1)
    db.commit()


def edu_get_user_list(db: Session):  # , skip: int, limit: int):
    _user_list = (
        db.query(EduUserModel)
        .filter(EduUserModel.usertype == "student")
        .order_by(EduUserModel.idx)
    )

    total = _user_list.count()
    # user_list = _user_list.offset(skip).limit(limit).all()
    return total, _user_list


def edu_get_subject_list(db: Session):
    subject_list = db.query(EduSubjectModel).order_by(EduSubjectModel.idx)
    return subject_list


def edu_get_subject(db: Session, idx: int):
    return db.query(EduSubjectModel).filter(EduSubjectModel.idx == idx).first()


def edu_get_object_list(db: Session):
    object_list = db.query(EduObjectModel).order_by(EduObjectModel.idx)
    return object_list


def edu_get_object(db: Session, idx: int):
    obj = db.query(EduObjectModel).filter(EduObjectModel.idx == idx).first()
    return obj


def edu_get_problem_list(db: Session):
    problem_list = db.query(EduProblemModel).order_by(EduProblemModel.idx)
    return problem_list


def edu_get_problem(db: Session, idx: int):
    problem = db.query(EduProblemModel).filter(EduProblemModel.idx == idx).first()
    return problem


def edu_update_problem(
    db: Session, db_problem: EduProblemModel, update_problem: EduDevelopProblemSchema
):
    db_problem.object_idx = update_problem.object_idx
    db_problem.problem_level = update_problem.problem_level
    db_problem.problem_answer = update_problem.problem_answer
    db_problem.problem_question = update_problem.problem_question
    db_problem.problem_content = update_problem.problem_content
    db_problem.problem_result = update_problem.problem_result
    db_problem.level_1_selection_answer = update_problem.level_1_selection_answer
    db_problem.level_1_selection_1 = update_problem.level_1_selection_1
    db_problem.level_1_selection_2 = update_problem.level_1_selection_2
    db_problem.level_1_selection_3 = update_problem.level_1_selection_3
    db_problem.level_2_initcodes = update_problem.level_2_initcodes
    db_problem.level_2_num_of_answers = update_problem.level_2_num_of_answers
    db_problem.level_2_answer_1 = update_problem.level_2_answer_1
    db_problem.level_2_answer_2 = update_problem.level_2_answer_2
    db_problem.level_2_answer_3 = update_problem.level_2_answer_3
    db_problem.level_2_answer_4 = update_problem.level_2_answer_4
    db_problem.level_2_answer_5 = update_problem.level_2_answer_5
    db_problem.level_2_scores_precent = update_problem.level_2_scores_precent
    db_problem.level_3_initcodes = update_problem.level_3_initcodes
    db.commit()


def edu_get_classroom_list(db: Session):
    classroom_list = db.query(EduClassroomModel).order_by(EduClassroomModel.idx)
    return classroom_list


def edu_get_classroom(db: Session, idx: int):
    classroom = db.query(EduClassroomModel).filter(EduClassroomModel.idx == idx).first()
    return classroom


def edu_get_my_classroom_list(db: Session, userid: str):
    my_classroom_list = (
        db.query(EduMyClassroomModel)
        .filter(EduMyClassroomModel.userid == userid)
        .order_by(EduMyClassroomModel.idx)
    )
    return my_classroom_list


def edu_get_my_classroom(db: Session, userid: str, classroom_idx: int):
    my_classroom = (
        db.query(EduMyClassroomModel)
        .filter(
            (EduMyClassroomModel.userid == userid)
            & (EduMyClassroomModel.classroom_idx == classroom_idx)
        )
        .first()
    )
    if not my_classroom:
        my_classroom = EduMyClassroomModel(
            userid=userid,
            classroom_idx=classroom_idx,
            created_at=datetime.datetime.now(),
        )
        db.add(my_classroom)
        db.commit()
    return my_classroom


def edu_get_my_classroom_idx(db: Session, idx: int):
    my_classroom = (
        db.query(EduMyClassroomModel).filter(EduMyClassroomModel.idx == idx).first()
    )
    return my_classroom


def edu_update_my_classroom(
    db: Session,
    db_user: EduUserModel,
    db_my_classroom: EduMyClassroomModel,
    user_classroom_update: EduUserMyClassroomUpdateScheme,
):
    db_user.current_classroom = user_classroom_update.current_classroom
    db_my_classroom.classroom_idx = user_classroom_update.current_classroom
    db_my_classroom.time_goal_at = user_classroom_update.time_goal_at
    db_my_classroom.time_goal_status = user_classroom_update.time_goal_status
    db_my_classroom.time_goal = user_classroom_update.time_goal
    db_my_classroom.time_goal_delay = user_classroom_update.time_goal_delay
    db_my_classroom.created_at = datetime.datetime.now()
    db.commit()

def edu_update_my_classroom_time_set(
    db: Session,
    db_my_classroom: EduMyClassroomModel,
    user_classroom_update: EduUserMyClassroomUpdateScheme,
):
    # print('#'*30)
    # print(user_classroom_update.time_goal_status)
    # print(datetime.datetime.now())
    # print(datetime.datetime.now()+datetime.timedelta(hours=user_classroom_update.time_goal_status))
    # print('#'*30)
    time_now = datetime.datetime.now()
    time_goal = time_now + datetime.timedelta(hours=user_classroom_update.time_goal_status)
    db_my_classroom.time_goal_at = time_now
    db_my_classroom.time_goal_status = user_classroom_update.time_goal_status
    db_my_classroom.time_goal = time_goal
    db_my_classroom.updated_at = datetime.datetime.now()
    db.commit()


def edu_update_my_classroom_time_delay(
    db: Session,
    db_my_classroom: EduMyClassroomModel,
    user_classroom_update: EduUserMyClassroomUpdateScheme,
):
    time_now = datetime.datetime.now()
    time_goal = time_now + datetime.timedelta(hours=user_classroom_update.time_goal_status)
    db_my_classroom.time_goal = time_goal
    db_my_classroom.time_goal_delay = user_classroom_update.time_goal_delay
    db_my_classroom.updated_at = datetime.datetime.now()
    db.commit()


def edu_update_current_problem(
    db: Session,
    db_my_classroom: EduMyClassroomModel,
    update_my_classroom: EduUserMyClassroomScheme,
):
    db_my_classroom.current_problem_seq = update_my_classroom.current_problem_seq
    db_my_classroom.updated_at = datetime.datetime.now()
    db.commit()


def edu_get_my_answer(
    db: Session, userid: str, classroom_idx: int, problem_idx: int, problem_seq: int
):
    my_answer = (
        db.query(EduMyAnswerModel)
        .filter(
            (EduMyAnswerModel.userid == userid)
            & (EduMyAnswerModel.classroom_idx == classroom_idx)
            & (EduMyAnswerModel.problem_idx == problem_idx)
        )
        .first()
    )
    if not my_answer:
        sh_list = [i for i in range(4)]
        random.shuffle(sh_list)
        my_answer = EduMyAnswerModel(
            userid=userid,
            classroom_idx=classroom_idx,
            problem_seq=problem_seq,
            problem_idx=problem_idx,
            selection_list=sh_list,
            answer=[],
            is_correct=[],
            is_correct_teacher=[],
            answer_status=0,
            comment_to_student=[],
            memo_from_teacher=[],
            particial_score=0,
            answer_score=0,
            created_at=datetime.datetime.now(),
        )
        db.add(my_answer)
        db.commit()
    return my_answer


def edu_create_my_answer(
    db: Session, userid: str, classroom_idx: int, problem_idx: int, problem_seq: int
):
    sh_list = [i for i in range(4)]
    random.shuffle(sh_list)
    my_answer = EduMyAnswerModel(
        userid=userid,
        classroom_idx=classroom_idx,
        problem_seq=problem_seq,
        problem_idx=problem_idx,
        selection_list=sh_list,
        answer=[],
        is_correct=[],
        is_correct_teacher=[],
        answer_status=0,
        comment_to_student=[],
        memo_from_teacher=[],
        particial_score=0,
        answer_score=0,
        created_at=datetime.datetime.now(),
    )
    db.add(my_answer)
    db.commit()


def edu_get_my_answer_idx(db: Session, idx: int):
    my_answer = db.query(EduMyAnswerModel).filter(EduMyAnswerModel.idx == idx).first()
    return my_answer


def edu_update_my_answer(
    db: Session, db_answer: EduMyAnswerModel, update_answer: EduUserAnswerScheme
):
    db_answer.answer = update_answer.answer
    db_answer.is_correct_teacher = update_answer.is_correct_teacher
    db_answer.answer_status = update_answer.answer_status
    db_answer.comment_to_student = update_answer.comment_to_student
    db_answer.memo_from_teacher = update_answer.memo_from_teacher
    db_answer.particial_score = update_answer.particial_score
    db_answer.answer_score = update_answer.answer_score
    db_answer.updated_at = datetime.datetime.now()
    db.commit()


def edu_get_my_answer_list(db: Session, userid: str, idx: int):
    my_answer_list = (
        db.query(EduMyAnswerModel)
        .filter(
            (EduMyAnswerModel.userid == userid)
            & (EduMyAnswerModel.classroom_idx == idx)
        )
        .order_by(EduMyAnswerModel.problem_seq)
    )
    return my_answer_list


def edu_get_my_problem_list(db: Session, problems: list):
    # print(str(problems))
    result = list()
    for i in problems:
        result.append(edu_get_problem(db, i))
    return result


def edu_update_my_classroom_status(
    db: Session, db_my_classroom: EduMyClassroomModel, classroom_status: int
):
    db_my_classroom.classroom_status = classroom_status
    db_my_classroom.updated_at = datetime.datetime.now()
    db.commit()


def edu_score_my_answers(
    db: Session, db_answer: EduMyAnswerModel, db_problem: EduProblemModel
):
    # print(f"answer idx={db_answer.idx}, problem idx={db_problem.idx}")
    is_correct = []
    answer_status = 0
    if db_problem.problem_level == 1:
        answer = db_answer.selection_list.index(0) + 1
        if answer == int(db_answer.answer[0]):
            is_correct.append(1)
        else:
            is_correct.append(0)
        answer_status = 2
        print("#" * 30)
        print(f"문제 {db_answer.problem_seq} 번")
        print(f"selection_list={db_answer.selection_list}")
        print(f"answer={answer}")
        print(f"my_answer={int(db_answer.answer[0])}")
        print(f"score={is_correct}")
        print("#" * 30)
    elif db_problem.problem_level == 2:
        if db_problem.level_2_num_of_answers > 0:
            for i in range(db_problem.level_2_num_of_answers):
                answer_list = []
                if i == 0:
                    answer_list = db_problem.level_2_answer_1
                elif i == 1:
                    answer_list = db_problem.level_2_answer_2
                elif i == 2:
                    answer_list = db_problem.level_2_answer_3
                elif i == 3:
                    answer_list = db_problem.level_2_answer_4
                else:
                    answer_list = db_problem.level_2_answer_5
                my_answer = db_answer.answer[i]
                for a in answer_list:
                    if my_answer == a:
                        is_correct.append(1)
                        break
                    else:
                        is_correct.append(0)
                        break
                print("#" * 30)
                print(f"문제 {db_answer.problem_seq} 번 - ({i+1})")
                print(f"답안={answer_list}")
                print(f"나의 답안={my_answer}")
                print(f"채점={is_correct}")
                print("#" * 30)
            answer_status = 2
    elif db_problem.problem_level == 3:
        is_correct.append(0)
        answer_status = 1
    db_answer.is_correct = is_correct
    db_answer.answer_status = answer_status
    db.commit()


def edu_get_evaluate_my_classroom_list(
    db: Session,
):
    my_classroom_list = db.query(EduMyClassroomModel).order_by(
        EduMyClassroomModel.updated_at.desc(),
        EduMyClassroomModel.created_at.desc(),
        EduMyClassroomModel.idx,
    )
    return my_classroom_list


def edu_update_classroom_only_problem_number(
    db: Session,
    db_classroom: EduClassroomModel,
    update_classroom: EduDevelopClassroomSchema,
):
    db_classroom.level_1_num_of_problems = update_classroom.level_1_num_of_problems
    db_classroom.level_2_num_of_problems = update_classroom.level_2_num_of_problems
    db_classroom.level_3_num_of_problems = update_classroom.level_3_num_of_problems
    db.commit()


def edu_update_classroom_all(
    db: Session,
    db_classroom: EduClassroomModel,
    update_classroom: EduDevelopClassroomSchema,
):
    db_classroom.title = update_classroom.title
    db_classroom.object_idx = update_classroom.object_idx
    db_classroom.previous_classroom_idx = update_classroom.previous_classroom_idx
    db_classroom.level_1_num_of_problems = update_classroom.level_1_num_of_problems
    db_classroom.level_2_num_of_problems = update_classroom.level_2_num_of_problems
    db_classroom.level_3_num_of_problems = update_classroom.level_3_num_of_problems
    db_classroom.level_1_problems = update_classroom.level_1_problems
    db_classroom.level_2_problems = update_classroom.level_2_problems
    db_classroom.level_3_problems = update_classroom.level_3_problems
    db_classroom.level_1_problems_scores = update_classroom.level_1_problems_scores
    db_classroom.level_2_problems_scores = update_classroom.level_2_problems_scores
    db_classroom.level_3_problems_scores = update_classroom.level_3_problems_scores
    db_classroom.total_score = update_classroom.total_score
    db_classroom.score_is_show = update_classroom.total_score
    db.commit()


def edu_init_my_classroom_chatgpt(db: Session, db_my_classroom: EduMyClassroomModel):
    chatgpt = list()
    chatgpt.append(
        {
            "role": "system",
            "content": "You will be provided with a piece of Python code, and your task is to provide ideas for efficiency improvements.",
        }
    )
    chatgpt.append(
        {"role": "system", "content": "And translate your answer in korean."}
    )
    db_my_classroom.chatgpt = chatgpt
    db.commit()


def edu_get_ai_message(db: Session, db_my_classroom: EduMyClassroomModel, dialog: str):
    chatgpt = db_my_classroom.chatgpt[:]
    chatgpt.append({"role": "user", "content": dialog})
    response = openai.chat.completions.create(
        model=config["OPENAI_MODEL"], messages=chatgpt, temperature=0.7, max_tokens=1000
    )
    return response.choices[0].message.content


def edu_update_ai_message(
    db: Session, db_my_classroom: EduMyClassroomModel, dialog: str, ai_message: str
):
    chatgpt = db_my_classroom.chatgpt[:]
    chatgpt.append({"role": "user", "content": dialog})
    chatgpt.append({"role": "assistant", "content": ai_message})
    db_my_classroom.chatgpt = chatgpt
    db.commit()


# ----------------- make_db -----------------#


def make_db_subject(db: Session):
    for i in subject_list_dump:
        subject = EduSubjectModel(
            subject_title=i["subject_title"],
            subject_main_idea=i["subject_main_idea"],
            subject_main_1=i["subject_main_1"],
            subject_main_2=i["subject_main_2"],
            subject_main_3=i["subject_main_3"],
            subject_goal=i["subject_goal"],
            subject_goal_detail=i["subject_goal_detail"],
        )
        db.add(subject)
        db.commit()
    return {"result": "ok"}


def make_db_object(db: Session):
    for i in object_list_dump:
        obj = EduObjectModel(
            idx=i["idx"],
            subject_idx=i["subject_idx"],
            object_title=i["object_title"],
            object_detail=i["object_detail"],
        )
        db.add(obj)
        db.commit()
    return {"result": "ok"}


def make_db_problem(db: Session):
    for i in problem_list_dump:
        prob = EduProblemModel(
            object_idx=i["object_idx"],
            problem_level=i["problem_level"],
            problem_answer=("problem_answer" in i) and i["problem_answer"] or "",
            problem_question=("problem_question" in i) and i["problem_question"] or "",
            problem_content=("problem_content" in i) and i["problem_content"] or "",
            problem_result=("problem_result" in i) and i["problem_result"] or "",
            level_1_selection_answer=("level_1_selection_answer" in i)
            and i["level_1_selection_answer"]
            or "",
            level_1_selection_1=("level_1_selection_1" in i)
            and i["level_1_selection_1"]
            or "",
            level_1_selection_2=("level_1_selection_2" in i)
            and i["level_1_selection_2"]
            or "",
            level_1_selection_3=("level_1_selection_3" in i)
            and i["level_1_selection_3"]
            or "",
            level_2_initcodes=("level_2_initcodes" in i)
            and i["level_2_initcodes"]
            or "",
            level_2_num_of_answers=("level_2_num_of_answers" in i)
            and int(i["level_2_num_of_answers"])
            or 0,
            level_2_answer_1=("level_2_answer_1" in i) and i["level_2_answer_1"] or "",
            level_2_answer_2=("level_2_answer_2" in i) and i["level_2_answer_2"] or "",
            level_2_answer_3=("level_2_answer_3" in i) and i["level_2_answer_3"] or "",
            level_2_answer_4=("level_2_answer_4" in i) and i["level_2_answer_4"] or "",
            level_2_answer_5=("level_2_answer_5" in i) and i["level_2_answer_5"] or "",
            level_3_initcodes=("level_3_initcodes" in i)
            and i["level_3_initcodes"]
            or "",
        )
        db.add(prob)
        db.commit()
    return {"result": "ok"}


def make_db_classroom(db: Session):
    for i in classroom_list_dump:
        classroom = EduClassroomModel(
            title=i["title"],
            object_idx=i["object_idx"],
            previous_classroom_idx=i["previous_classroom_idx"],
            level_1_problems=i["level_1_problems"],
            level_2_problems=i["level_2_problems"],
            level_3_problems=i["level_3_problems"],
        )
        db.add(classroom)
        db.commit()
    return {"result": "ok"}


my_classroom_list_dump = [
    {
        "idx": 1,
        "userid": "user1",
        "classroom_idx": 1,
        "created_at": datetime.date(2024, 2, 25),
        "updated_at": "",
    },
    {
        "idx": 2,
        "userid": "user1",
        "classroom_idx": 3,
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 3,
        "userid": "user2",
        "classroom_idx": 3,
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 4,
        "userid": "user1",
        "classroom_idx": 4,
        "created_at": datetime.date(2024, 4, 25),
        "updated_at": "",
    },
]


def make_db_my_classroom(db: Session):
    for i in my_classroom_list_dump:
        my_classroom = EduMyClassroomModel(
            userid=i["userid"],
            classroom_idx=i["classroom_idx"],
            current_problem_seq=1,
            created_at=i["created_at"],
        )
        db.add(my_classroom)
        db.commit()
    return {"result": "ok"}


my_answer_list_dump = [
    {
        "idx": 1,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 1,
        "problem_idx": 46,
        "selection_list": [1, 0, 2, 3],
        "answer": ["2"],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 2,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 2,
        "problem_idx": 47,
        "selection_list": [1, 2, 3, 0],
        "answer": [],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 3,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 3,
        "problem_idx": 48,
        "selection_list": [2, 3, 0, 1],
        "answer": [],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 4,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 4,
        "problem_idx": 49,
        "selection_list": [0, 3, 1, 2],
        "answer": [],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 5,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 5,
        "problem_idx": 51,
        "selection_list": [],
        "answer": ["i in range(1, 101)", "total += i"],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 6,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 6,
        "problem_idx": 52,
        "selection_list": [],
        "answer": ["i <= 100", "total += i"],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 7,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 7,
        "problem_idx": 53,
        "selection_list": [],
        "answer": [],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 8,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 8,
        "problem_idx": 54,
        "selection_list": [],
        "answer": [],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 9,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 9,
        "problem_idx": 56,
        "selection_list": [],
        "answer": [
            """point = 0
total = 0
for i in range(1, 21, 1):
    text = str(i) + '회 다트 점수를 입력하세요: '
    point = input(text)
    point = int(point)
"""
        ],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
    {
        "idx": 10,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 10,
        "problem_idx": 57,
        "selection_list": [],
        "answer": [],
        "created_at": datetime.date(2024, 3, 25),
        "updated_at": "",
    },
]


def make_db_my_answer(db: Session):
    for i in my_answer_list_dump:
        my_answer = EduMyAnswerModel(
            userid=i["userid"],
            classroom_idx=i["classroom_idx"],
            problem_seq=i["problem_seq"],
            problem_idx=i["problem_idx"],
            selection_list=i["selection_list"],
            answer=i["answer"],
            created_at=i["created_at"],
        )
        db.add(my_answer)
        db.commit()
    return {"result": "ok"}


'''
"idx": 2,
"subject_idx": 1,
"object_title": "연산자",
"object_detail": """- 1차원 배열의 데이터 구조를 활용한 프로그램을 작성한다.""",

class EduObjectModel(Base):
    __tablename__ = "edu_object"
    idx = Column(Integer, primary_key=True)
    subject_idx = Column(Integer, ForeignKey('edu_subject.idx'), nullable=False)
    object_title = Column(String(100), nullable=False)
    object_detail = Column(Text, nullable=True)

class EduProblemModel(Base):
    __tablename__ = "edu_problem"
    idx = Column(Integer, primary_key=True)
    object_idx = Column(Integer, ForeignKey('edu_object.idx'), nullable=False)
    problem_level = Column(Integer, nullable=False)
    problem_answer = Column(Text, nullable=True)
    problem_question = Column(Text, nullable=True)
    problem_content = Column(Text, nullable=True)
    problem_result = Column(Text, nullable=True)
    level_1_selection_answer = Column(String(300), nullable=True)
    level_1_selection_1 = Column(String(300), nullable=True)
    level_1_selection_2 = Column(String(300), nullable=True)
    level_1_selection_3 = Column(String(300), nullable=True)
    level_2_initcodes = Column(Text, nullable=True)
    level_2_num_of_answers = Column(Integer, nullable=True)
    level_2_answer_1 = Column(String(300), nullable=True)
    level_2_answer_2 = Column(String(300), nullable=True)
    level_2_answer_3 = Column(String(300), nullable=True)
    level_2_answer_4 = Column(String(300), nullable=True)
    level_2_answer_5 = Column(String(300), nullable=True)
    level_3_initcodes = Column(Text, nullable=True)

        "idx": 1,
        "title": "변수와 자료형의 이해와 활용",
        "object_idx": 1,
        "previous_classroom_idx": 0,
        "level_1_problems": [1, 2, 3, 4],
        "level_2_problems": [6, 7, 8, 9],
        "level_3_problems": [11, 12],
class EduClassroomModel(Base):
    __tablename__ = "edu_classroom"
    idx = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    object_idx = Column(Integer, ForeignKey("edu_object.idx"), nullable=False)
    previous_classroom_idx = Column(Integer, nullable=False)
    level_1_problems = Column(String(300), nullable=True)
    level_2_problems = Column(String(300), nullable=True)
    level_3_problems = Column(String(300), nullable=True)

        "idx": 1,
        "userid": "user1",
        "classroom_idx": 1,
        'created_at': '2024-02-25 11:11:11',
        'updated_at': '',

class EduMyClassroomModel(Base):
    __tablename__ = "edu_my_classroom"
    idx = Column(Integer, primary_key=True)
    userid = Column(String(30), nullable=False)
    classroom_idx = Column(Integer, ForeignKey("edu_classroom.idx"), nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

        "idx": 1,
        "userid": "user1",
        "classroom_idx": 4,
        "problem_seq": 1,
        "problem_idx": 46,
        "selection_list": [1, 0, 2, 3],
        "answer": ["2"],
        "created_at": "2024-03-25 11:11:11",
        "updated_at": "",

classroom EduMyAnswerModel(Base):
    __tablename__ = "edu_my_answer"
    idx = Column(Integer, primary_key=True)
    userid = Column(String(30), nullable=False)
    classroom_idx = Column(Integer, ForeignKey("edu_classroom.idx"), nullable=False)
    problem_seq = Column(Integer, nullable=False)
    problem_idx = Column(Integer, nullable=False)
    selection_list = Column(String(300), nullable=True)
    answer = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
'''


def make_db(db: Session):
    # result = db_subject(db)
    # result = db_object(db)
    # result = db_problem(db)
    # result = db_classroom(db)
    # result = db_my_classroom(db)
    # result = db_my_answer(db)
    # return result
    return {"result": "ok"}
