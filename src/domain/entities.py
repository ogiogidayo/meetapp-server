from datetime import datetime

class Meeting:
    def __init__(self, meet_id: str,  meet_link: str, date_time: datetime):
        self.meet_id = meet_id
        self.meet_link = meet_link
        self.date_time = date_time

class User:
    def __init__(self, user_id: str, org: str, meet_id: str):
        self.user_id = user_id
        self.org = org
        self.meet_id = meet_id

class Answer:
    def __init__(self, user_id: str, name: str, answer_1: str, answer_2: str, answer_ai: str, meet_id: str):
        self.user_id = user_id
        self.name = name
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_ai = answer_ai
        self.meet_id = meet_id

class AIQuestion:
    def __init__(self, meet_id: str, question: str):
        self.meet_id = meet_id
        self.question = question
