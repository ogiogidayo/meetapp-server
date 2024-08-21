from domain.entities import User
from domain.repositories import UserRepository
from client.kintone import KintoneClient

class APIUserRepository(UserRepository):
    def __init__(self, api_token: str, app_id: int):
        self.api_client = KintoneClient(api_token, app_id)

    def register_user(self, user_id: str, org: str, meet_id: str) -> User:
        params = {
            "record": {
                "user_id": {"value": user_id},
                "org": {"value": org},
                "meet_id": {"value": meet_id}
            }
        }
        response = self.api_client.post("record", params)
        return User(user_id, org, meet_id)

    def get_user(self, user_id: str) -> User:
        params = {"query": f"user_id = \"{user_id}\""}
        response = self.api_client.get("records", params)
        record = response["records"][0]
        return User(record["user_id"]["value"], record["org"]["value"], record["meet_id"]["value"])