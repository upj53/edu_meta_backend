from fastapi import APIRouter 

router = APIRouter() 

@router.get('/test_router_users/', tags=['test_router_users'])
async def test_router_read_users():
  return [{'username':'Rick'}, {'username':'Morty'}]

@router.get('/test_router_users/me', tags=['test_router_users'])
async def test_router_read_user_me():
  return {'username':'Wonjune'}

@router.get('/test_router_users/{username}', tags=['test_router_users'])
async def test_router_read_user(username:str):
  return {'username':username}