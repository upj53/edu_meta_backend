import datetime
from pydantic import BaseModel, EmailStr
from pydantic import field_validator
from pydantic_core.core_schema import FieldValidationInfo


class EduUserSchema(BaseModel):
    idx: int
    userid: str
    usertype: str
    username: str
    email: str
    current_classroom: int
    teacherid: str


class EduUserCreateScheme(BaseModel):
    userid: str = ""
    usertype: str = ""
    password1: str = ""
    password2: str = ""
    username: str = ""
    email: EmailStr = ""
    current_classroom: int = 0
    teacherid:str = ""

    @field_validator("userid", "password1", "password2", "email")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v


class EduUserUpdateScheme(BaseModel):
    userid: str = ""
    usertype: str = ""
    password1: str = ""
    password2: str = ""
    username: str = ""
    email: EmailStr = ""
    current_classroom: int = 0

    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v


class EduUserMyClassroomUpdateScheme(BaseModel):
    idx: int = 0
    userid: str = ""
    current_classroom: int = 0
    time_goal_at: datetime.datetime | None = None
    time_goal_status: int = 0
    time_goal: datetime.datetime | None = None
    time_goal_delay: list = []

'''
update_params = {
    "idx": 0,
    "userid": "user9",
    "current_classroom": 4,
    "time_goal_at": "2024-07-25T1:12:34.000Z",
    "time_goal_status": 1,
    "time_goal": "2024-07-25T2:12:34.000Z",
    "time_goal_delay": [],
}
'''

class EduUserMyClassroomChatgptUpdateScheme(BaseModel):
    idx: int = 0
    dialog: str = ""


class EduUserMyClassroomScheme(BaseModel):
    idx: int = 0
    userid: str = ""
    classroom_idx: int = 0
    current_problem_seq: int = 1
    classroom_status: int = 0
    answers_idx_list: list = []
    time_goal_at: datetime.datetime | None = None
    time_goal_status: int = 0
    time_goal: datetime.datetime | None = None
    time_goal_delay: list = []
    chatgpt: list = []
    chatgpt_dialog: list = []
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None


class EduUserMyClassroomListScheme(BaseModel):
    my_classroom_list: list[EduUserMyClassroomScheme] = []


class EduUserAnswerScheme(BaseModel):
    idx: int = 0
    userid: str = ""
    classroom_idx: int = 0
    problem_seq: int = 0
    problem_idx: int = 0
    selection_list: list = []
    answer: list = []
    is_correct: list = []
    is_correct_teacher: list = []
    answer_status: int = 0
    comment_to_student: list = []
    memo_from_teacher: list = []
    particial_score: int = 0
    answer_score: int = 0
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None


class EduUserAnswerListScheme(BaseModel):
    my_answer_list: list[EduUserAnswerScheme] = []


class EduTokenSchema(BaseModel):
    access_token: str
    token_type: str
    userid: str
    usertype: str
    current_classroom: int


class EduUserListSchema(BaseModel):
    total: int = 0
    student_list: list[EduUserSchema] = []


class EduDesignSubjectSchema(BaseModel):
    idx: int
    subject_title: str
    subject_main_idea: str
    subject_main_1: str
    subject_main_2: str
    subject_main_3: str
    subject_goal: str
    subject_goal_detail: str


class EduDesignSubjectListSchema(BaseModel):
    subject_list: list[EduDesignSubjectSchema] = []


class EduDesignObjectSchema(BaseModel):
    idx: int
    subject_idx: int
    object_title: str
    object_detail: str


class EduDesignObjectListScheme(BaseModel):
    object_list: list[EduDesignObjectSchema] = []


class EduDevelopProblemSchema(BaseModel):
    idx: int = 0
    object_idx: int = 0
    problem_level: int = 0
    problem_answer: list = []
    problem_question: str = ""
    problem_content: str = ""
    problem_result: str = ""
    level_1_selection_answer: str = ""
    level_1_selection_1: str = ""
    level_1_selection_2: str = ""
    level_1_selection_3: str = ""
    level_2_initcodes: str = ""
    level_2_num_of_answers: int = 1
    level_2_answer_1: list = []
    level_2_answer_2: list = []
    level_2_answer_3: list = []
    level_2_answer_4: list = []
    level_2_answer_5: list = []
    level_2_scores_precent: list = []
    level_3_initcodes: str = ""


class EduDevelopProblemListSchema(BaseModel):
    problem_list: list[EduDevelopProblemSchema] = []


class EduDevelopClassroomSchema(BaseModel):
    idx: int = 0
    title: str = ""
    object_idx: int = 0
    previous_classroom_idx: int = 0
    level_1_num_of_problems: int = 0
    level_2_num_of_problems: int = 0
    level_3_num_of_problems: int = 0
    level_1_problems: list = []
    level_2_problems: list = []
    level_3_problems: list = []
    level_1_problems_scores: list = []
    level_2_problems_scores: list = []
    level_3_problems_scores: list = []
    total_score: int = 0
    score_is_show: int = 0


class EduDevelopClassroomListSchema(BaseModel):
    classroom_list: list[EduDevelopClassroomSchema] = []


class EduDevelopClassroomAllSchema(BaseModel):
    classroom: EduDevelopClassroomSchema
    level_2_problems: list[EduDevelopProblemSchema] = []


class EduUserMyClassroomAllScheme(BaseModel):
    student: EduUserSchema
    classroom: EduDevelopClassroomSchema
    my_classroom: EduUserMyClassroomScheme
    my_answer_list: list[EduUserAnswerScheme] = []
    problem_list: list[EduDevelopProblemSchema] = []
    num_of_problems: int = 0
    current_problem_seq: int = 0
    current_problem_idx: int = 0


class EduEvaluateClassroomStudentListScheme(BaseModel):
    my_classroom_list: list[EduUserMyClassroomScheme] = []
    student_list: list[EduUserSchema] = []
    classroom_list: list[EduDevelopClassroomSchema] = []
