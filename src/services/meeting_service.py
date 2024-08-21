from domain.repositories import MeetingRepository
from domain.entities import Meeting
from datetime import datetime


class MeetingService:
    def __init__(self, repository: MeetingRepository):
        self.repository = repository

    def create_meeting(self, meet_link: str, date_time: str,) -> Meeting:
        return self.repository.create_meeting(meet_link, date_time)

    def get_meeting(self, meet_id: str) -> Meeting:
        return self.repository.get_meeting(meet_id)