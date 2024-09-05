from fastapi import FastAPI, Form, Request, File, UploadFile, Depends, Body
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import timedelta, datetime
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values
from typing import Annotated
from modules.db import get_db
from sqlalchemy.orm import Session
from starlette import status
from models import *
from schemas import *
from modules import *

router = APIRouter(prefix="/pybo", tags=["pybo"])
config = dotenv_values(".env")
domain = config["DOMAIN_URL"]
templates = Jinja2Templates(directory="./templates")

ACCESS_TOKEN_EXPIRE_MINUTES = 60*24
SECRET_KEY = 'f9d2b97ee5c112796127fc6af1b1d19b0d80d97142b80f5bbb635665f85f1c6f'
ALGORITHM = 'HS256'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/pybo/user/login')


@router.get("/hello")
async def hello():
    return {"message": "안녕하세요 파이보"}


@router.get("/list", response_model=PyboQuestionListSchema)
async def question_list(
        db: Session = Depends(get_db),
        page: int = 0, size: int = 10, keyword:str=''):
    # total, _question_list = pybo_get_question_list(
        # db, skip=page*size, limit=size)
    total, _question_list = pybo_get_search_list(
        db, page*size, size, keyword)
    return {
        'total': total,
        'question_list': _question_list
    }


@router.get("/detail/{question_idx}", response_model=PyboQuestionSchema)
async def question_detail(question_idx: int, db: Session = Depends(get_db)):
    question = pybo_get_question(db, question_idx)
    return question


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = pybo_get_user(db, username)
        if user is None:
            raise credentials_exception
        return user


@router.post('/answer/create/{question_idx}', status_code=status.HTTP_204_NO_CONTENT)
async def answer_create(
        question_idx: int,
        _answer_create: PyboAnswerCreateSchema = Body(...),
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    # create answer
    question = pybo_get_question(db, question_idx)
    if not question:
        raise HTTPException(status_code=404, detail='Question not found')
    pybo_create_answer(
        db,
        question,
        _answer_create,
        current_user)


@router.post('/question/create', status_code=status.HTTP_204_NO_CONTENT)
async def question_create(
        _question_create: PyboQuestionCreateSchema,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    pybo_create_question(
        db,
        _question_create,
        current_user)


@router.get('/make-db')
async def make_db(db: Session = Depends(get_db)):
    pybo_make_db(db)


@router.post('/user/create', status_code=status.HTTP_204_NO_CONTENT)
async def user_create(
        _user_create: PyboUserCreateSchema,
        db: Session = Depends(get_db)):
    user = pybo_get_existing_user(db, _user_create)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='이미 존재하는 사용자 아이디 또는 이메일입니다.'
        )
    pybo_create_user(db, _user_create)


@router.post('/user/login', response_model=PyboTokenSchema)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):
    # check user and password
    user = pybo_get_user(db, form_data.username)
    # print(f'{form_data.username}, {form_data.password}')
    # print(f'{user.username}, {user.password}')
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    # make access token
    data = {
        'sub': user.username,
        'exp': datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': user.username
    }


@router.put('/question/update', status_code=status.HTTP_204_NO_CONTENT)
async def question_update(
        _question_update: PyboQuestionUpdateSchema,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    db_question = pybo_get_question(db, _question_update.question_idx)
    if not db_question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='데이터를 찾을 수 없습니다.')
    if current_user.idx != db_question.user.idx:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='수정 권한이 없습니다.')
    pybo_update_question(db, db_question, _question_update)


@router.delete('/question/delete', status_code=status.HTTP_204_NO_CONTENT)
async def question_delete(
        _question_delete: PyboQuestionDeleteSchema,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    db_question = pybo_get_question(db, _question_delete.question_idx)
    if not db_question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='데이터를 찾을 수 없습니다.')
    if current_user.idx != db_question.user.idx:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='삭제 권한이 없습니다.')
    pybo_delete_question(db, db_question)


@router.get('/answer/detail/{answer_idx}', response_model=PyboAnswerSchema)
async def answer_detail(answer_idx: int, db: Session = Depends(get_db)):
    answer = pybo_get_answer(db, answer_idx)
    return answer


@router.put('/answer/update', status_code=status.HTTP_204_NO_CONTENT)
async def answer_update(
        _answer_update: PyboAnswerUpdateSchema,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    db_answer = pybo_get_answer(db, _answer_update.answer_idx)
    if not db_answer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='데이터를 찾을 수 없습니다.')
    if current_user.idx != db_answer.user.idx:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='수정 권한이 없습니다.')
    pybo_update_answer(db, db_answer, _answer_update)


@router.delete('/answer/delete', status_code=status.HTTP_204_NO_CONTENT)
async def answer_delete(
        _answer_delete: PyboAnswerDeleteScheme,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    db_answer = pybo_get_answer(db, _answer_delete.answer_idx)
    if not db_answer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='데이터를 찾을 수 없습니다.')
    if current_user.idx != db_answer.user.idx:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='삭제 권한이 없습니다.')
    pybo_delete_answer(db, db_answer)


@router.post('/question/vote', status_code=status.HTTP_204_NO_CONTENT)
async def question_vote(
        _question_vote: PyboQuestionVoteSchema,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    db_question = pybo_get_question(db, _question_vote.question_idx)
    if not db_question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='데이터를 찾을 수 없습니다.')
    pybo_vote_question(db, db_question, current_user)


@router.post('/answer/vote', status_code=status.HTTP_204_NO_CONTENT)
async def answer_vote(
        _answer_vote: PyboAnswerVoteSchema,
        db: Session = Depends(get_db),
        current_user: PyboUserModel = Depends(get_current_user)):
    db_answer = pybo_get_answer(db, _answer_vote.answer_idx)
    if not db_answer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='데이터를 찾을 수 없습니다')
    pybo_vote_answer(db, db_answer, current_user)
