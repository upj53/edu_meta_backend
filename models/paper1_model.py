from pydantic import BaseModel

class Paper1Model(BaseModel):
  role1: str
  content1: str
  role2: str
  content2: str
  role3: str
  content3: str