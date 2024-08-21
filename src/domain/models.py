from pydantic import BaseModel
from datetime import datetime

class MeetingModel(BaseModel):
    meet_id: str
    date_time: str
    meet_link: str

class UserModel(BaseModel):
    user_id: str
    org: str
    meet_id: str

class AnswerModel(BaseModel):
    user_id: str
    name: str
    answer_1: str
    answer_2: str
    answer_ai: str
    meet_id: str

class AIQuestionModel(BaseModel):
    meet_id: str
    question: str
