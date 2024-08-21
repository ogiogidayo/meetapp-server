from domain.entities import AIQuestion
from domain.repositories import AIQuestionRepository
from client.kintone import KintoneClient
from typing import List


class APIAIQuestionRepository(AIQuestionRepository):
    def __init__(self, api_token: str, app_id: int):
        self.api_client = KintoneClient(api_token, app_id)

    def add_question(self, meet_id: str, question: str) -> AIQuestion:
        params = {
            "record": {
                "meet_id": {"value": meet_id},
                "question": {"value": question}
            }
        }
        response = self.api_client.post("record", params)
        return AIQuestion(meet_id, question)

    def get_questions(self, meet_id: str) -> List[AIQuestion]:
        params = {"query": f"meet_id = \"{meet_id}\""}
        response = self.api_client.get("records", params)
        return [AIQuestion(record["meet_id"]["value"], record["question"]["value"]) for record in response["records"]]
