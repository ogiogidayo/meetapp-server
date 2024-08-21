from domain.repositories import AIQuestionRepository
from domain.entities import AIQuestion
from typing import List

class AIQuestionService:
    def __init__(self, repository: AIQuestionRepository):
        self.repository = repository

    def add_question(self, meet_id: str, question: str) -> AIQuestion:
        return self.repository.add_question(meet_id, question)

    def get_questions(self, meet_id: str) -> List[AIQuestion]:
        return self.repository.get_questions(meet_id)
