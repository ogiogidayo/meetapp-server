from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from .entities import Meeting, User, Answer, AIQuestion


class MeetingRepository(ABC):
    @abstractmethod
    def create_meeting(self,  meet_link: str, date_time: datetime) -> Meeting:
        pass

    @abstractmethod
    def get_meeting(self, meet_id: str) -> Meeting:
        pass


class UserRepository(ABC):
    @abstractmethod
    def register_user(self, user_id: str, org: str, meet_id: str) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> User:
        pass


class AnswerRepository(ABC):
    @abstractmethod
    def submit_answer(self, user_id: str, name: str, answer_1: str, answer_2: str, answer_ai: str, meet_id: str) -> Answer:
        pass

    @abstractmethod
    def get_answers(self, meet_id: str) -> List[Answer]:
        pass


class AIQuestionRepository(ABC):
    @abstractmethod
    def add_question(self, meet_id: str, question: str) -> AIQuestion:
        pass

    @abstractmethod
    def get_questions(self, meet_id: str) -> List[AIQuestion]:
        pass
