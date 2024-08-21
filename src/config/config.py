from database.meeting_repository import APIMeetingRepository
from database.user_repository import APIUserRepository
from database.answer_repository import APIAnswerRepository
from database.ai_question_repository import APIAIQuestionRepository
from services.meeting_service import MeetingService
from services.user_service import UserService
from services.answer_service import AnswerService
from services.ai_question_service import AIQuestionService

def get_meeting_service() -> MeetingService:
    api_token = "XXXXXXXXXXXXXXXXXXXXXXXX"
    app_id = 1
    repository = APIMeetingRepository(api_token, app_id)
    return MeetingService(repository)

def get_user_service() -> UserService:
    api_token = "XXXXXXXXXXXXXXXXXXXXXXXX"
    app_id = 4
    repository = APIUserRepository(api_token, app_id)
    return UserService(repository)

def get_answer_service() -> AnswerService:
    api_token = "XXXXXXXXXXXXXXXXXXXXXXXX"
    app_id = 3
    repository = APIAnswerRepository(api_token, app_id)
    return AnswerService(repository)

def get_ai_question_service() -> AIQuestionService:
    api_token = "XXXXXXXXXXXXXXXXXXXXXXXX"
    app_id = 2
    repository = APIAIQuestionRepository(api_token, app_id)
    return AIQuestionService(repository)
