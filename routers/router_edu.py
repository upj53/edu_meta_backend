# python libraries
from fastapi import FastAPI, Form, Request, File, UploadFile, Depends, Body
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.encoders import jsonable_encoder
import time
from dotenv import dotenv_values
from starlette import status
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from jose import jwt, JWTError

# user librarise
from modules.db import get_db
from schemas import (
    EduUserSchema,
    EduUserCreateScheme,
    EduUserUpdateScheme,
    EduUserMyClassroomUpdateScheme,
    EduUserListSchema,
    EduUserMyClassroomScheme,
    EduUserMyClassroomListScheme,
    EduUserAnswerScheme,
    EduUserMyClassroomAllScheme,
    EduTokenSchema,
    EduDesignSubjectSchema,
    EduDesignSubjectListSchema,
    EduDesignObjectSchema,
    EduDesignObjectListScheme,
    EduDevelopProblemSchema,
    EduDevelopProblemListSchema,
    EduDevelopClassroomSchema,
    EduDevelopClassroomListSchema,
    EduDevelopClassroomSchema,
    EduDevelopClassroomAllSchema,
    EduEvaluateClassroomStudentListScheme,
    EduUserMyClassroomChatgptUpdateScheme,
)
from modules import (
    edu_create_user,
    edu_get_existing_user,
    edu_get_user,
    pwd_context_edu,
    edu_update_user,
    edu_update_my_classroom,
    edu_get_my_classroom_idx,
    edu_update_current_problem,
    edu_get_my_answer_idx,
    edu_update_my_answer,
    edu_get_user_list,
    edu_get_subject,
    edu_get_subject_list,
    edu_get_object,
    edu_get_object_list,
    edu_get_problem,
    edu_get_problem_list,
    edu_update_problem,
    edu_get_classroom_list,
    edu_get_classroom,
    edu_get_my_classroom_list,
    edu_get_my_classroom,
    edu_get_my_answer,
    edu_get_my_answer_list,
    edu_create_my_answer,
    edu_get_my_problem_list,
    edu_update_my_classroom_status,
    edu_score_my_answers,
    edu_get_evaluate_my_classroom_list,
    edu_update_classroom_only_problem_number,
    edu_update_classroom_all,
    edu_update_my_classroom_time_delay,
    edu_update_my_classroom_time_set,
    edu_init_my_classroom_chatgpt,
    edu_get_ai_message,
    edu_update_ai_message,
    make_db,
)
from models import (
    EduUserModel,
    EduMyClassroomModel,
)


# router object
router = APIRouter(prefix="/edu", tags=["edu"])
config = dotenv_values(".env")
secret_key_value = config["SECRET_KEY"]

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = secret_key_value
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/edu/user/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userid: str = payload.get("sub")
        if userid is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = edu_get_user(db, userid)
        if user is None:
            raise credentials_exception
        return user


@router.post("/user/create", status_code=status.HTTP_204_NO_CONTENT)
async def create_user(_user_create: EduUserCreateScheme, db: Session = Depends(get_db)):
    user = edu_get_existing_user(db, _user_create)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 사용자 아이디 또는 이메일입니다.",
        )
    edu_create_user(db, _user_create)


@router.post("/user/login", response_model=EduTokenSchema)
async def user_login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # check userid and password
    user = edu_get_user(db, form_data.username)
    if not user or not pwd_context_edu.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자 아이디 또는 암호가 잘못됐습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # make access token
    data = {
        "sub": user.userid,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "userid": user.userid,
        "usertype": user.usertype,
        "current_classroom": user.current_classroom,
    }


@router.get("/user/{userid}", response_model=EduUserSchema)
async def get_user_info(
    db: Session = Depends(get_db),
    userid: str = "",
    current_user: EduUserModel = Depends(get_current_user),
):
    user = edu_get_user(db, userid)
    return user


@router.put("/user/update/{userid}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(
    _user_update: EduUserUpdateScheme,
    db: Session = Depends(get_db),
    userid: str = "",
    current_user: EduUserModel = Depends(get_current_user),
):
    db_user = edu_get_user(db, userid)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="사용자를 찾을 수 없습니다."
        )
    edu_update_user(db, db_user, _user_update)


@router.get("/student/list", response_model=EduUserListSchema)
async def get_student_list(
    db: Session = Depends(get_db),
    # page: int = 0,
    # size: int = 20,
    current_user: EduUserModel = Depends(get_current_user),
):
    total, _student_list = edu_get_user_list(db)  # , skip=page * size, limit=size)
    return {"total": total, "student_list": _student_list}


@router.get("/design/subject/list", response_model=EduDesignSubjectListSchema)
async def get_subject_list(
    db: Session = Depends(get_db),
    current_user: EduUserModel = Depends(get_current_user),
):
    # _subject_list = edu_get_subject_list_dump()
    _subject_list = edu_get_subject_list(db)
    return {"subject_list": _subject_list}


@router.get("/design/subject/{idx}", response_model=EduDesignSubjectSchema)
async def get_subject_view(
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    # subject = edu_get_subject_dump()
    subject = edu_get_subject(db, idx)
    return subject


@router.get("/design/object/list", response_model=EduDesignObjectListScheme)
async def get_object_list(
    db: Session = Depends(get_db),
    current_user: EduUserModel = Depends(get_current_user),
):
    # _object_list = edu_get_object_list_dump()
    _object_list = edu_get_object_list(db)
    return {"object_list": _object_list}


@router.get("/design/object/{idx}", response_model=EduDesignObjectSchema)
async def get_object_view(
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    # obj = edu_get_object_dump(idx)
    obj = edu_get_object(db, idx)
    return obj


@router.get("/develop/problem/list", response_model=EduDevelopProblemListSchema)
async def get_problem_list(
    db: Session = Depends(get_db),
    current_user: EduUserModel = Depends(get_current_user),
):
    # _problem_list = edu_get_problem_list_dump()
    _problem_list = edu_get_problem_list(db)
    return {"problem_list": _problem_list}


@router.get("/develop/problem/{idx}", response_model=EduDevelopProblemSchema)
async def get_problem_view(
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    # problem = edu_get_problem_dump(idx)
    problem = edu_get_problem(db, idx)
    return problem


@router.put("/develop/update/problem/{idx}", status_code=status.HTTP_204_NO_CONTENT)
async def update_problem(
    _update_problem: EduDevelopProblemSchema,
    db: Session = Depends(get_db),
    idx: int = 0,
):
    db_problem = edu_get_problem(db, idx)
    edu_update_problem(db, db_problem, _update_problem)


@router.get("/develop/classroom/list", response_model=EduDevelopClassroomListSchema)
async def get_classroom_list(
    db: Session = Depends(get_db),
    current_user: EduUserModel = Depends(get_current_user),
):
    # _classroom_list = edu_get_classroom_list_dump()
    _classroom_list = edu_get_classroom_list(db)
    return {"classroom_list": _classroom_list}


@router.get("/develop/classroom/{idx}", response_model=EduDevelopClassroomAllSchema)
async def get_classroom_view(
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    # classroom = edu_get_classroom_dump(idx)
    _classroom = edu_get_classroom(db, idx)
    _level_2_problems = []
    for i in _classroom.level_2_problems:
        _level_2_problems.append(edu_get_problem(db, i))
    return {
        "classroom": _classroom,
        "level_2_problems": _level_2_problems,
    }


@router.get("/student/classroom/{idx}", response_model=EduDevelopClassroomSchema)
async def get_classroom_view(
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    # classroom = edu_get_classroom_dump(idx)
    classroom = edu_get_classroom(db, idx)
    return classroom


@router.get(
    "/student/my-classroom/{userid}/list", response_model=EduUserMyClassroomListScheme
)
async def get_my_classroom_list(
    db: Session = Depends(get_db),
    userid: str = "",
    current_user: EduUserModel = Depends(get_current_user),
):
    # _my_classroom_list = edu_get_my_classroom_list_dump(userid)
    _my_classroom_list = edu_get_my_classroom_list(db, userid)
    return {"my_classroom_list": _my_classroom_list}


@router.get(
    "/student/my-classroom/{userid}/{classroom_idx}",
    response_model=EduUserMyClassroomScheme,
)
async def get_my_classroom(
    db: Session = Depends(get_db),
    userid: str = "",
    classroom_idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    # classroom = edu_get_my_classroom_dump(userid, classroom_idx)
    my_classroom = edu_get_my_classroom(db, userid, classroom_idx)
    if not my_classroom:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="해당 클래스룸이 없습니다.",
        )
    return my_classroom


@router.put(
    "/student/update/my-classroom/{userid}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_my_classroom(
    _user_classroom_update: EduUserMyClassroomUpdateScheme,
    db: Session = Depends(get_db),
    userid: str = "",
    current_user: EduUserModel = Depends(get_current_user),
):
    db_user = edu_get_user(db, userid)
    classroom_idx = _user_classroom_update.current_classroom
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="사용자를 찾을 수 없습니다."
        )
    if db_user.userid != _user_classroom_update.userid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="사용자 인증에 오류가 있습니다.",
        )
    db_my_classroom = edu_get_my_classroom(db, userid, classroom_idx)
    edu_update_my_classroom(db, db_user, db_my_classroom, _user_classroom_update)


@router.put(
    "/student/update/my-classroom-time-set/{idx}",
)
async def update_my_classroom_time_set(
    _user_classroom_update: EduUserMyClassroomUpdateScheme,
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    db_my_classroom = edu_get_my_classroom_idx(db, idx)
    edu_update_my_classroom_time_set(db, db_my_classroom, _user_classroom_update)


@router.put(
    "/student/update/my-classroom-time-delay/{idx}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_my_classroom_time_delay(
    _user_classroom_update: EduUserMyClassroomUpdateScheme,
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    db_my_classroom = edu_get_my_classroom_idx(db, idx)
    edu_update_my_classroom_time_delay(db, db_my_classroom, _user_classroom_update)


@router.put(
    "/student/update/current_problem/{idx}", status_code=status.HTTP_204_NO_CONTENT
)
async def update_my_classroom_current_problem(
    _update_my_classroom: EduUserMyClassroomScheme,
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    db_my_classroom = edu_get_my_classroom_idx(db, idx)
    if not db_my_classroom:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="클래스룸을 찾을 수 없습니다.",
        )
    # print(f"db_my_classroom.idx={db_my_classroom.idx}")
    # print(f"_update_my_classroom={_update_my_classroom.current_problem_seq}")
    edu_update_current_problem(db, db_my_classroom, _update_my_classroom)


@router.get(
    "/student/answer/{userid}/{classroom_idx}/{problem_idx}/{problem_seq}",
    response_model=EduUserAnswerScheme,
)
async def get_my_answer(
    db: Session = Depends(get_db),
    userid: str = "",
    classroom_idx: int = 0,
    problem_idx: int = 0,
    problem_seq: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    db_user = edu_get_user(db, userid)
    # answer = edu_get_my_answer_dump(userid, classroom_idx, problem_idx)
    answer = edu_get_my_answer(db, userid, classroom_idx, problem_idx, problem_seq)
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="사용자 답변을 찾을 수 없습니다.",
        )
    return answer


@router.put("/student/update/answer/{idx}", status_code=status.HTTP_204_NO_CONTENT)
async def update_my_answer(
    _update_answer: EduUserAnswerScheme,
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    db_answer = edu_get_my_answer_idx(db, idx)
    if not db_answer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="사용자 답변을 찾을 수 없습니다.",
        )
    edu_update_my_answer(db, db_answer, _update_answer)


@router.get(
    "/student/answer/list/{userid}/{idx}", response_model=EduUserMyClassroomAllScheme
)
async def get_my_answer_list_all(
    db: Session = Depends(get_db),
    userid: str = "",
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    _user = edu_get_user(db, userid)
    _classroom = edu_get_classroom(db, idx)
    _my_classroom = edu_get_my_classroom(db, userid, idx)
    if len(_my_classroom.chatgpt) == 0:
        edu_init_my_classroom_chatgpt(db, _my_classroom)
    _my_answer_list = edu_get_my_answer_list(db, userid, idx)
    if _my_answer_list.count() == 0:
        print("#" * 30)
        print("answers가 없습니다.")
        seq = 1
        for i in _classroom.level_1_problems:
            print(f"{seq}번: {i}")
            edu_create_my_answer(db, userid, idx, int(i), seq)
            seq += 1
        for i in _classroom.level_2_problems:
            print(f"{seq}번: {i}")
            edu_create_my_answer(db, userid, idx, int(i), seq)
            seq += 1
        for i in _classroom.level_3_problems:
            print(f"{seq}번: {i}")
            edu_create_my_answer(db, userid, idx, int(i), seq)
            seq += 1
        _my_answer_list = edu_get_my_answer_list(db, userid, idx)
        print("#" * 30)
    prb1 = list(_classroom.level_1_problems)
    prb2 = list(_classroom.level_2_problems)
    prb3 = list(_classroom.level_3_problems)
    # print(prb1 + prb2 + prb3)
    _problem_list = edu_get_my_problem_list(db, prb1 + prb2 + prb3)
    problem_seq = _my_classroom.current_problem_seq
    problem_idx = 0
    if problem_seq <= len(_classroom.level_1_problems):
        problem_idx = _classroom.level_1_problems[problem_seq - 1]
    elif problem_seq <= (
        len(_classroom.level_1_problems) + len(_classroom.level_2_problems)
    ):
        problem_idx = _classroom.level_2_problems[
            problem_seq - len(_classroom.level_1_problems) - 1
        ]
    else:
        problem_idx = _classroom.level_3_problems[
            problem_seq
            - len(_classroom.level_1_problems)
            - len(_classroom.level_2_problems)
            - 1
        ]
    # time.sleep(3)
    return {
        "student": _user,
        "classroom": _classroom,
        "my_classroom": _my_classroom,
        "my_answer_list": _my_answer_list,
        "problem_list": _problem_list,
        "num_of_problems": len(_classroom.level_1_problems)
        + len(_classroom.level_2_problems)
        + len(_classroom.level_3_problems),
        "current_problem_seq": problem_seq,
        "current_problem_idx": problem_idx,
    }


@router.put(
    "/student/update/my-classroom/status/{idx}", status_code=status.HTTP_204_NO_CONTENT
)
async def update_student_classroom_all(
    _update_my_classroom: EduUserMyClassroomScheme,
    db: Session = Depends(get_db),
    userid: str = "",
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    classroom_status = _update_my_classroom.classroom_status
    db_my_classroom = edu_get_my_classroom_idx(db, idx)
    edu_update_my_classroom_status(db, db_my_classroom, classroom_status)
    if classroom_status == 1:
        for i in _update_my_classroom.answers_idx_list:
            db_answer = edu_get_my_answer_idx(db, i)
            db_problem = edu_get_problem(db, db_answer.problem_idx)
            edu_score_my_answers(db, db_answer, db_problem)

        classroom_status = 2
        edu_update_my_classroom_status(db, db_my_classroom, classroom_status)


@router.put("/evaluate/update/classroom/{idx}", status_code=status.HTTP_204_NO_CONTENT)
async def update_teacher_score_classroom_all(
    db: Session = Depends(get_db),
    idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    db_my_classroom = edu_get_my_classroom_idx(db, idx)
    if db_my_classroom.classroom_status == 2:
        classroom_status = 3
        edu_update_my_classroom_status(db, db_my_classroom, classroom_status)


@router.get(
    "/evaluate/my-classroom/list", response_model=EduEvaluateClassroomStudentListScheme
)
async def get_evaluate_my_classroom_list(
    db: Session = Depends(get_db),
    current_user: EduUserModel = Depends(get_current_user),
):
    _my_classroom_list = edu_get_evaluate_my_classroom_list(db)
    total, _student_list = edu_get_user_list(db)
    _classroom_list = edu_get_classroom_list(db)
    # classroom_student_list = EduEvaluateClassroomStudentListScheme(
    # my_classroom_list = _my_classroom_list,
    # student_list = _student_list
    # )
    return {
        "my_classroom_list": _my_classroom_list,
        "student_list": _student_list,
        "classroom_list": _classroom_list,
    }


@router.put("/develop/update/classroom/{idx}/{mode}")
async def update_classroom(
    _update_classroom: EduDevelopClassroomSchema,
    db: Session = Depends(get_db),
    idx: int = 0,
    mode: str = "",
    current_user: EduUserModel = Depends(get_current_user),
):
    if mode == "all":
        db_classroom = edu_get_classroom(db, idx)
        edu_update_classroom_all(db, db_classroom, _update_classroom)
    elif mode == "num":
        db_classroom = edu_get_classroom(db, idx)
        edu_update_classroom_only_problem_number(db, db_classroom, _update_classroom)


@router.put("/student/ai_helper")
async def put_ai_chatgpt(
    _update_ai_dialog: EduUserMyClassroomChatgptUpdateScheme,
    db: Session = Depends(get_db),
    classroom_idx: int = 0,
    current_user: EduUserModel = Depends(get_current_user),
):
    classroom_idx = _update_ai_dialog.idx
    dialog = _update_ai_dialog.dialog
    db_my_classroom = edu_get_my_classroom_idx(db, classroom_idx)
    ai_message = edu_get_ai_message(db, db_my_classroom, dialog)
    edu_update_ai_message(db, db_my_classroom, dialog, ai_message)
    return {"ai_message": ai_message}


"""
@router.get("/make_db")
async def make_database(
    db: Session = Depends(get_db),
    current_user: EduUserModel = Depends(get_current_user),
):
    return make_db(db)
"""
