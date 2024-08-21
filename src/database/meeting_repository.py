from datetime import datetime
from domain.entities import Meeting
from domain.repositories import MeetingRepository
from client.kintone import KintoneClient
import uuid
import base64
import asyncio
import aiohttp

class APIMeetingRepository(MeetingRepository):
    def __init__(self, api_token: str, app_id: int):
        self.api_client = KintoneClient(api_token, app_id)

    def create_meeting(self, meet_link: str, date_time: datetime) -> Meeting:
        uuid_full = uuid.uuid4()
        uuid_bytes = uuid_full.bytes
        short_uuid = base64.urlsafe_b64encode(uuid_bytes).decode('utf-8')
        uuid_str = short_uuid[:5]
        asyncio.run(send_post_request(uuid_str))
        params = {
            "record": {
                "meet_link": {"value": meet_link},
                "date_time": {"value": date_time},
                "meet_id": {"value": uuid_str},
            }
        }
        response = self.api_client.post("record", params)
        return Meeting(uuid_str,meet_link, date_time)

    def get_meeting(self, meet_id: str) -> Meeting:
        params = {"query": f"meet_id = \"{meet_id}\""}
        response = self.api_client.get("records", params)
        record = response["records"][0]
        return Meeting(record["meet_id"]["value"], record["date_time"]["value"], record["meet_link"]["value"])

async def send_post_request(meet_id):
    url = f"https://id3sjlyq67ppn2e5gjsgivagmi0ierma.lambda-url.ap-northeast-1.on.aws/questions?meet_id=%s" % meet_id
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as resp:
            pass