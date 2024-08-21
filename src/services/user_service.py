from domain.repositories import UserRepository
from domain.entities import User


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, user_id: str, org: str, meet_id: str) -> User:
        return self.repository.register_user(user_id, org, meet_id)

    def get_user(self, user_id: str) -> User:
        return self.repository.get_user(user_id)
