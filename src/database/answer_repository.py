from domain.entities import Answer
from domain.repositories import AnswerRepository
from client.kintone import KintoneClient
from typing import List


class APIAnswerRepository(AnswerRepository):
    def __init__(self, api_token: str, app_id: int):
        self.api_client = KintoneClient(api_token, app_id)

    def submit_answer(self, user_id: str, name: str, answer_1: str, answer_2: str, answer_ai: str, meet_id: str) -> Answer:
        params = {
            "record": {
                "user_id": {"value": user_id},
                "name": {"value": name},
                "answer_1": {"value": answer_1},
                "answer_2": {"value": answer_2},
                "answer_ai": {"value": answer_ai},
                "meet_id": {"value": meet_id},
            }
        }
        response = self.api_client.post("record", params)
        return Answer(user_id, name, answer_1, answer_2, answer_ai, meet_id)

    def get_answers(self, meet_id: str) -> List[Answer]:
        params = {"query": f"meet_id = \"{meet_id}\""}
        response = self.api_client.get("records", params)
        return [Answer(record["user_id"]["value"], record["name"]["value"], record["answer_1"]["value"],  record["answer_2"]["value"], record["answer_ai"]["value"], meet_id) for record in  response["records"]]
