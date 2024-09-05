from sqlalchemy import Column, Integer, String
from pydantic import BaseModel 
from modules.db import Base 
from modules.db import ENGINE

class TestUserTable(Base):
  __tablename__ = 'test_user'
  idx = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(30), nullable=True)
  age = Column(Integer)

class TestUser(BaseModel):
  name: str 
  age: int

class TestUserModify(BaseModel):
  idx: int 
  name: str 
  age: int

# 테이블이 없으면 생성한다
Base.metadata.create_all(bind=ENGINE)