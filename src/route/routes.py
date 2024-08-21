from fastapi import APIRouter, Depends
from domain.models import MeetingModel, UserModel, AnswerModel, AIQuestionModel
from config.config import *
from typing import List

router = APIRouter()
@router.post("/meetings", response_model=MeetingModel)
def create_meeting(meet_link: str, date_time: str, service: MeetingService = Depends(get_meeting_service)):
    meeting = service.create_meeting(meet_link, date_time)
    return MeetingModel(
        meet_id=meeting.meet_id,
        meet_link=meeting.meet_link,
        date_time=meeting.date_time,
    )

@router.get("/meetings/{meet_id}", response_model=MeetingModel)
def get_meeting(meet_id: str, service: MeetingService = Depends(get_meeting_service)):
    meeting = service.get_meeting(meet_id)
    return MeetingModel(
        meet_id=meeting.meet_id,
        meet_link=meeting.meet_link,
        date_time=meeting.date_time,
    )

@router.post("/users", response_model=UserModel)
def register_user(user_id: str, org: str, meet_id: str, service: UserService = Depends(get_user_service)):
    user = service.register_user(user_id, org, meet_id)
    return UserModel(
        user_id=user.user_id,
        org=user.org,
        meet_id=user.meet_id
    )

@router.post("/answer", response_model=AnswerModel)
def submit_answer(user_id: str, name: str, answer_1: str, answer_2: str, answer_ai: str, meet_id: str, service: AnswerService = Depends(get_answer_service)):
    answer = service.submit_answer(user_id, name, answer_1, answer_2, answer_ai, meet_id)
    return AnswerModel(
        user_id=answer.user_id,
        name=answer.name,
        answer_1=answer.answer_1,
        answer_2=answer.answer_2,
        answer_ai=answer.answer_ai,
        meet_id=answer.meet_id
    )

@router.get("/answers/{meet_id}", response_model=List[AnswerModel])
def get_answers(meet_id: str, service: AnswerService = Depends(get_answer_service)):
    answers = service.get_answers(meet_id)
    return [
        AnswerModel(
            user_id=answer.user_id,
            name=answer.name,
            answer_1=answer.answer_1,
            answer_2=answer.answer_2,
            answer_ai=answer.answer_ai,
            meet_id=answer.meet_id
        ) for answer in answers
    ]

@router.post("/questions", response_model=AIQuestionModel)
def add_question(meet_id: str, question: str, service: AIQuestionService = Depends(get_ai_question_service)):
    ai_question = service.add_question(meet_id, question)
    return AIQuestionModel(
        meet_id=ai_question.meet_id,
        question=ai_question.question
    )

@router.get("/questions/{meet_id}", response_model=List[AIQuestionModel])
def get_questions(meet_id: str, service: AIQuestionService = Depends(get_ai_question_service)):
    questions = service.get_questions(meet_id)
    return [
        AIQuestionModel(
            meet_id=question.meet_id,
            question=question.question
        ) for question in questions
    ]

