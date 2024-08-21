from domain.repositories import AnswerRepository
from domain.entities import Answer
from typing import List

class AnswerService:
    def __init__(self, repository: AnswerRepository):
        self.repository = repository

    def submit_answer(self, user_id: str, name: str, answer_1: str, answer_2: str, answer_ai: str,
                      meet_id: str) -> Answer:
        return self.repository.submit_answer(user_id, name, answer_1, answer_2, answer_ai, meet_id)

    def get_answers(self, meet_id: str) -> List[Answer]:
        return self.repository.get_answers(meet_id)