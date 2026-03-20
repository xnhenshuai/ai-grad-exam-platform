from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    subject: str
    topic: str
    content: str
    answer: str


class QuestionCreate(QuestionBase):
    pass


class QuestionOut(QuestionBase):
    id: int

    class Config:
        orm_mode = True


class MistakeBase(BaseModel):
    user_id: int
    question_id: int
    note: str | None = None


class MistakeCreate(MistakeBase):
    pass


class MistakeOut(MistakeBase):
    id: int
    created_at: datetime | None

    class Config:
        orm_mode = True


class StudyPlanBase(BaseModel):
    user_id: int
    plan_name: str
    details: str


class StudyPlanCreate(StudyPlanBase):
    pass


class StudyPlanOut(StudyPlanBase):
    id: int
    updated_at: datetime | None

    class Config:
        orm_mode = True
