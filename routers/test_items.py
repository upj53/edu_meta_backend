from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel 

from test_dependencies import get_token_header

router = APIRouter(
  prefix='/test_router_items',
  tags=['test_router_items'],
  dependencies=[Depends(get_token_header)],
  responses={404: {'description':'Not found'}}
)

fake_items_db = {'plumbus':{'name':'Plumbus'}, 'gun':{'name':'Portal Gun'}}

@router.get('/')
async def test_router_read_items():
  return fake_items_db

@router.get('/{item_id}')
async def test_router_read_item(item_id:str):
  if item_id not in fake_items_db:
    raise HTTPException(status_code=404, detail='Item not found')
  return {'name':fake_items_db[item_id]['name'], 'item_id':item_id}

class TestRouterUpdateItem(BaseModel):
  msg: str

@router.put(
  '/{item_id}',
  tags=['test_custom'],
  responses={403:{'description':'Operation forbidden'}}
)
async def test_router_update_item(item_id:str, model:TestRouterUpdateItem=Body(...)):
  if item_id != 'plumbus':
    raise HTTPException(
      status_code=403, detail='You can only update the item: plumbus'
    )
  print(f'fake_items_db[item_id] = {fake_items_db[item_id]}')
  print(f'model.msg = {model.msg}')
  fake_items_db[item_id].update({'msg':model.msg})
  print(f'fake_items_db[item_id] = {fake_items_db[item_id]}')
  return fake_items_db[item_id]