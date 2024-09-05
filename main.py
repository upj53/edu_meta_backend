from dotenv import dotenv_values
from fastapi import FastAPI, Form, Request, File, UploadFile, Depends, Body
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from typing import Union, List, Set, Annotated, Dict, Any
from pydantic import BaseModel, HttpUrl
from papers.paper1 import get_chatgpt
from papers.paper2 import get_feedback, get_dialog
from modules.db import session
from models.test_mysql_user import TestUserTable, TestUser, TestUserModify
from models.paper2_model import Paper2Model
from test_dependencies import get_query_token, get_token_header
from test_dependencies import get_test_admin_token_header, get_test_admin_query_token
from routers import *
from models import *
from internal import test_admin

import os
import time
import requests

# app = FastAPI()
app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(test_users.router)
app.include_router(test_items.router)
app.include_router(router_test.router)
app.include_router(router_pybo.router)
app.include_router(router_edu.router)
app.include_router(
    test_admin.router,
    prefix="/test_admin",
    tags=["test_admin"],
    dependencies=[Depends(get_test_admin_token_header)],
    responses={418: {"description": "I am a teapot"}},
)

config = dotenv_values(".env")
config_server_status = config["SERVER_STATUS"]
allow_origins_value = ''
if config_server_status == 'localhost':
    allow_origins_value = config["LOCALHOST_URL_VALUE"]
elif config_server_status == 'goorm':
    allow_origins_value = config["DOMAIN_GOORM_URL_VALUE"]
elif config_server_status == 'homeserver':
    allow_origins_value = config["DOMAIN_HOME_VALUE"]
domain = config["DOMAIN_URL"]
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[allow_origins_value],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/assets", StaticFiles(directory="./frontend/assets"))

message = list()
paper2_feedback_msg = list()
paper2_dialog_msg = list()

""" template 6 lines
@app.('/', response_class=HTMLResponse)
async def (request: Request):
  context = {
    'domain': domain,
    'request': request
  }
  return templates.TemplateResponse( '.html', context)
"""

"""
@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    context = {
        'domain': domain,
        'request': request
    }
    return templates.TemplateResponse('main.html', context)
"""


@app.get("/favicon.ico")
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(
        path=file_path,
        headers={"Content-Disposition": "attachment; filename=" + file_name},
    )


@app.get("/paper1", response_class=HTMLResponse)
async def paper1_get(request: Request):
    context = {"domain": domain, "request": request}
    return templates.TemplateResponse("paper1.html", context)


@app.post("/paper1-init")
async def paper1_init(
    request: Request,
    role1: Annotated[str, Form()],
    content1: Annotated[str, Form()],
    role2: Annotated[str, Form()],
    content2: Annotated[str, Form()],
    role3: Annotated[str, Form()],
    content3: Annotated[str, Form()],
):
    context = {}
    context["domain"] = domain
    context["request"] = request

    global message
    message = list()
    message.append({"role": role1, "content": content1})
    message.append({"role": role2, "content": content2})
    message.append({"role": role3, "content": content3})
    # print(f'1.{role1:9s}\t{content1}')
    # time.sleep(3)
    # context['chatgpt'] = 'hello world\nget init chat gpt'
    context["chatgpt"] = get_chatgpt(message)
    message.append({"role": "assistant", "content": context["chatgpt"]})
    for m in message:
        role = m["role"]
        content = m["content"]
        print(f"{role:9s}\t: {content}")
    return context["chatgpt"]
    # return templates.TemplateResponse(
    # 'paper1.html', {'context':context}
    # )


@app.post("/paper1-single")
async def paper1_single(
    request: Request,
    role: Annotated[str, Form()],
    content: Annotated[str, Form()],
):
    context = {}
    context["domain"] = domain
    context["request"] = request

    global message
    if len(message) == 0:
        return "(에러) 이전 단계를 먼저 실행시켜주세요."
    message.append({"role": role, "content": content})
    # time.sleep(3)
    # context['chatgpt'] = 'hello world\nget single chat gpt'
    context["chatgpt"] = get_chatgpt(message)
    message.append({"role": "assistant", "content": context["chatgpt"]})
    for m in message:
        role = m["role"]
        content = m["content"]
        print(f"{role:9s}\t: {content}")
    return context["chatgpt"]
    # return templates.TemplateResponse(
    # '.html', {'context':context}
    # )


@app.post("/paper1-reset")
async def paper1_reset(request: Request):
    context = {}
    context["domain"] = domain
    context["request"] = request
    global message
    message = list()
    print(f"reset message list")
    # return templates.TemplateResponse(
    # '.html', {'context':context}
    # )


@app.get("/paper2", response_class=HTMLResponse)
async def paper2(request: Request):
    context = {"domain": domain, "request": request}
    return templates.TemplateResponse("paper2.html", context)


@app.get("/paper2-editor", response_class=HTMLResponse)
async def paper2_editor(request: Request):
    context = {"domain": domain, "request": request}
    return templates.TemplateResponse("paper2-editor.html", context)


@app.post("/paper2-feedback")
async def paper2_feedback(feedback: Paper2Model = Body(...)):
    global paper2_feedback_msg
    paper2_feedback_msg = list()
    paper2_feedback_msg.append(
        {
            "role": "system",
            "content": "You will be provided with a piece of Python code, and your task is to provide ideas for efficiency improvements.",
        }
    )
    paper2_feedback_msg.append(
        {"role": "system", "content": "And translate your answer in korean."}
    )
    paper2_feedback_msg.append({"role": "user", "content": feedback.dialog})

    # print(f'{feedback.dialog}')
    return get_feedback(paper2_feedback_msg)


@app.post("/paper2-dialog")
async def paper2_dialog(dialog: Paper2Model = Body(...)):
    global paper2_dialog_msg
    # paper2_dialog_msg = list()
    if len(paper2_dialog_msg) == 0:
        paper2_dialog_msg.append(
            {
                "role": "system",
                "content": "You are a teacher of Python programming. Your task is answering the following questions.",
            }
        )
        paper2_dialog_msg.append(
            {"role": "system", "content": "Translate all your answers in korean."}
        )
        paper2_dialog_msg.append({"role": "user", "content": dialog.dialog})
        gpt_answer = get_dialog(paper2_dialog_msg)
        paper2_dialog_msg.append({"role": "assistant", "content": gpt_answer})
        return gpt_answer
    else:
        paper2_dialog_msg.append({"role": "user", "content": dialog.dialog})
        gpt_answer = get_dialog(paper2_dialog_msg)
        paper2_dialog_msg.append({"role": "assistant", "content": gpt_answer})
        return gpt_answer
    """
    paper2_dialog_msg.append(
      {
        'role': 'user',
        'content': dialog.dialog
      }
    )
  """

    # print(f'{dialog.dialog}')
    return get_dialog(paper2_dialog_msg)


# -------------------------------------------------------------
# 테스트 코드
# -------------------------------------------------------------


@app.get("/Test", response_class=HTMLResponse)
async def test_fetch_test(request: Request):
    context = {"domain": domain, "request": request}
    return templates.TemplateResponse("test-main.html", context)


@app.get("/test-form1")
async def form1_get(request: Request):
    context = dict()
    context["request"] = request
    return templates.TemplateResponse("test-form1.html", context)


@app.post("/test-form1")
async def form1_post(request: Request):
    time.sleep(5)
    result = {"a": 1234, "b": "b"}
    return result


@app.get("/test-fetch", response_class=HTMLResponse)
async def test_fetch_test(request: Request):
    context = dict()
    context["domain"] = domain
    context["request"] = request
    context["test"] = "test"
    context["upj53"] = 53
    return templates.TemplateResponse("test-fetch.html", context)


class TestModel(BaseModel):
    name: str
    age: int


@app.post("/test-fetch-post1")
async def test_fetch_post1(request: Request):
    context = dict()
    context["domain"] = domain
    context["request"] = request
    return context


db_list = []


class TestCity(BaseModel):
    name: str
    timezone: str


class TestCityModify(BaseModel):
    idx: int
    name: str
    timezone: str


@app.get("/test-cities", response_class=HTMLResponse)
async def test_get_cities(request: Request):
    context = dict()
    context["domain"] = domain
    context["request"] = request
    global db_list
    rs_city = []
    cnt = 0
    for city in db_list:
        url = f'http://worldtimeapi.org/api/timezone/{city["timezone"]}'
        r = requests.get(url)
        cur_time = r.json()["datetime"]
        cnt += 1
        rs_city.append(
            {
                "idx": cnt,
                "name": city["name"],
                "timezone": city["timezone"],
                "current_time": cur_time,
            }
        )

    context["rs_city"] = rs_city
    return templates.TemplateResponse("test_city_list.html", context)


@app.get("/test-cities/{city_id}", response_class=HTMLResponse)
async def test_get_city(request: Request, city_id: int):
    context = dict()
    context["domain"] = domain
    context["request"] = request
    city = db_list[city_id - 1]
    r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
    cur_time = r.json()["datetime"]
    context["idx"] = city_id
    context["name"] = city["name"]
    context["timezone"] = city["timezone"]
    context["cur_time"] = cur_time
    return templates.TemplateResponse("test_city_detail.html", context)


# ----------데이터를 HTML Form 형태로 받는 방법----------


@app.post("/test-cities-1")
async def test_create_city_1(name: str = Form(...), timezone: str = Form(...)):
    db_list.append({"name", name, "timezone", timezone})
    return db_list[-1]


# ----------데이터를 json 형태로 받는 방법----------


@app.post("/test-cities-2")
async def test_create_city_2(request: Request, model: TestCity = Body(...)):
    db_list.append({"name": model.name, "timezone": model.timezone})
    for i in db_list:
        print(f'{i["name"]} {i["timezone"]}')
    return db_list[-1]


@app.put("/test-cities")
async def test_modify_city(city: TestCityModify = Body(...)):
    db_list[city.idx - 1] = {"name": city.name, "timezone": city.timezone}
    return db_list[city.idx - 1]


@app.delete("/test-cities/{city_id}")
async def test_delete_city(city_id: int):
    db_list.pop(city_id - 1)
    return {"result": "data deleted"}


# ----------Mysql 데이터베이스 사용하기----------


@app.get("/test-users", response_class=HTMLResponse)
async def test_read_users(request: Request):
    context = dict()
    context["domain"] = domain
    context["request"] = request
    users = session.query(TestUserTable).all()
    user_list = list()
    for u in users:
        user_list.append({"idx": u.idx, "name": u.name, "age": u.age})
    context["users"] = user_list
    return templates.TemplateResponse("test_user_list.html", context)


@app.get("/test-users/{user_id}")
async def test_read_user(user_id: int):
    user = session.query(TestUserTable).filter(TestUserTable.idx == user_id).first()
    return user


@app.post("/test-user")
# /user?name="이름"&age=10
async def test_create_user(model: TestUser = Body(...)):
    user = TestUserTable()
    user.name = model.name
    user.age = model.age

    session.add(user)
    session.commit()
    # print(f'사용자 {user.name} 생성됨')

    return f"사용자 {user.name} 생성됨"


@app.put("/test-users")
# users = [{}, {}, {}]
async def test_update_users():
    return ""


@app.put("/test-user")
async def test_update_user(model: TestUserModify = Body(...)):
    user = session.query(TestUserTable).filter(TestUserTable.idx == model.idx).first()
    user.name = model.name
    user.age = model.age
    session.commit()
    return f"사용자 {user.name} 수정됨"


@app.delete("/test-user/{user_id}")
async def test_delete_user(user_id: int):
    print(f"user_id: {user_id}")
    user = session.query(TestUserTable).filter(TestUserTable.idx == user_id).delete()
    session.commit()
    return f"사용자 삭제됨"


@app.get("/test-python-editor", response_class=HTMLResponse)
async def test_python_editor(request: Request):
    context = {"domain": domain, "request": request}
    return templates.TemplateResponse("test-python-editor.html", context)


@app.get("/test-iframe-python-editor", response_class=HTMLResponse)
async def test_iframe_python_editor(request: Request):
    context = {"domain": domain, "request": request}
    return templates.TemplateResponse("test-iframe-python-editor.html", context)


# ----------Test Frontend: Pybo Service----------


@app.get("/test-pybo-svelte")  #
async def test_pybo_index():
    return FileResponse("./frontend/index-pybo.html")


@app.get("/edu/")  #
async def test_edu_index():
    return FileResponse("./frontend/index-edu.html")


@app.get("/")
async def konkuk_edu_index():
    # print('config_server_status=',config_server_status)
    if config_server_status == 'localhost':
        return FileResponse("./frontend/index-konkuk-localhost.html")
    elif config_server_status == 'goorm':
        return FileResponse("./frontend/index-konkuk.html")
    elif config_server_status == 'homeserver':
        return FileResponse("./frontend/index-konkuk-homeserver.html")
