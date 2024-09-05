import os
from dotenv import dotenv_values
from fastapi import FastAPI, Form, Request, File, UploadFile, Depends, Body
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from typing import Union, List, Set, Annotated, Dict, Any
from pydantic import BaseModel, HttpUrl
from modules.db import session
from routers import *
from models import *

app = FastAPI()
app.include_router(router_edu.router)
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.mount("/assets", StaticFiles(directory="./frontend/assets"))
config = dotenv_values(".env")
config_server_status = config["SERVER_STATUS"]
allow_origins_value = ''
if config_server_status == 'localhost':
    allow_origins_value = config["LOCALHOST_URL_VALUE"]
elif config_server_status == 'goorm':
    allow_origins_value = config["DOMAIN_GOORM_URL_VALUE"]
elif config_server_status == 'homeserver':
    allow_origins_value = config["DOMAIN_HOME_VALUE"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[allow_origins_value],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/favicon.ico")
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(
        path=file_path,
        headers={"Content-Disposition": "attachment; filename=" + file_name},
    )

@app.get("/")
async def konkuk_edu_index():
    # print('config_server_status=',config_server_status)
    if config_server_status == 'localhost':
        return FileResponse("./frontend/index-konkuk-localhost.html")
    elif config_server_status == 'goorm':
        return FileResponse("./frontend/index-konkuk.html")
    elif config_server_status == 'homeserver':
        return FileResponse("./frontend/index-konkuk-homeserver.html")
