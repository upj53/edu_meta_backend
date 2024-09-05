from fastapi import APIRouter 

router = APIRouter() 

@router.get('/')
async def test_admin_get():
  return {'message':'Admin Page'}