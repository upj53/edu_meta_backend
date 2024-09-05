import datetime
from pydantic import BaseModel, EmailStr
from pydantic import field_validator
from pydantic_core.core_schema import FieldValidationInfo


class PyboUserSchema(BaseModel):
    idx: int
    username: str
    email: str


class PyboAnswerSchema(BaseModel):
    idx: int
    content: str
    create_date: datetime.datetime
    user: PyboUserSchema | None
    question_idx: int
    modify_date: datetime.datetime | None = None
    voter: list[PyboUserSchema]

    class Config:
        orm_mode = True


class PyboQuestionSchema(BaseModel):
    idx: int
    subject: str | None = None
    content: str | None = None
    create_date: datetime.datetime
    answers: list[PyboAnswerSchema] = []
    user: PyboUserSchema | None
    modify_date: datetime.datetime | None = None
    voter: list[PyboUserSchema]

    class Config:
        orm_mode = True


class PyboAnswerCreateSchema(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    class Config:
        orm_mode = True


class PyboQuestionCreateSchema(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    class Config:
        orm_mode = True


class PyboQuestionListSchema(BaseModel):
    total: int = 0
    question_list: list[PyboQuestionSchema] = []


class PyboUserCreateSchema(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr

    @field_validator('username', 'password1', 'password2', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다')
        return v

    @field_validator('password2')
    def passwords_match(cls, v, info: FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v


class PyboTokenSchema(BaseModel):
    access_token: str
    token_type: str
    username: str


class PyboQuestionUpdateSchema(PyboQuestionCreateSchema):
    question_idx: int


class PyboQuestionDeleteSchema(BaseModel):
    question_idx: int


class PyboAnswerUpdateSchema(PyboAnswerCreateSchema):
    answer_idx: int


class PyboAnswerDeleteScheme(BaseModel):
    answer_idx: int


class PyboQuestionVoteSchema(BaseModel):
    question_idx: int


class PyboAnswerVoteSchema(BaseModel):
    answer_idx: int
