from fastapi import FastAPI, Form, Request, File, UploadFile, Depends, Body
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel 
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values
from typing import Annotated 

fake_users_db = {
  "upj53": {
    "username": "upj53",
    "full_name": "Wonjune Park",
    "email": "upj53@daum.net",
    "hashed_password": "fakehashedsecret",
    "disabled": False,
  },
  "alice": {
    "username": "alice",
    "full_name": "Alice Wonderson",
    "email": "alice@example.com",
    "hashed_password": "fakehashedsecret2",
    "disabled": True,
  },
}

router = APIRouter(
  prefix='/my_test',
  tags=['my_test']
)
config = dotenv_values('.env')
domain = config['DOMAIN_URL']
templates = Jinja2Templates(directory='./templates')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/my_test/token')

def fake_hash_password(password: str):
  return 'fakehashed' + password

class TestUser(BaseModel):
  username: str 
  email: str | None = None 
  full_name: str | None = None 
  disabled: bool | None = None

class TestUserInDB(TestUser):
  hashed_password: str

def get_user(db, username: str):
  if username in db:
    user_dict = db[username]
    return TestUserInDB(**user_dict)

def fake_decode_token(token):
  user = get_user(fake_users_db, token)
  return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  user = fake_decode_token(token)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication credentials",
      headers={"WWW-Authenticate": "Bearer"},
    )      
  return user

async def get_current_active_user(
  current_user: Annotated[TestUser, Depends(get_current_user)]
):
  if current_user.disabled:
    raise HTTPException(status_code=400, detail='Inactive user')
  return current_user

@router.post('/token')
async def test_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
  user_dict = fake_users_db.get(form_data.username)
  if not user_dict:
    raise HTTPException(status_coe=400, detail='Incorrect username or password')
  user = TestUserInDB(**user_dict) 
  hashed_password = fake_hash_password(form_data.password)
  if not hashed_password == user.hashed_password:
    raise HTTPException(status_code=400, detail='Incorrect username or password')
  return {'access_token':user.username, 'token_type':'bearer'}

@router.get('/', response_class=HTMLResponse)
async def router_test_main(request: Request):
  context = {
    'domain': domain,
    'request': request
  }
  return templates.TemplateResponse('test-main.html', context)

@router.get('/users/me')
async def router_test_read_users_me(
  current_user: Annotated[TestUser, Depends(get_current_active_user)]
):
  return current_user

@router.get('/items')
async def router_test_items(token: Annotated[str, Depends(oauth2_scheme)]):
  return {'token': token}