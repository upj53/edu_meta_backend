from typing import Annotated 
from fastapi import Header, HTTPException 

async def get_token_header(): #x_token: Annotated[str, Header()]):
  print(f'get_token_header')

async def get_query_token(): #token: str):
  # print(f'get_query_token')
  pass

async def get_test_admin_token_header(x_token: Annotated[str, Header()]):
  if x_token != 'fake-super-secret-token':
    raise HTTPException(status_code=400, detail='X-Token header invalid')

async def get_test_admin_query_token(token: str):
  if token != 'upj53':
    raise HTTPException(status_code=400, detail='No upj53 token provided')