import requests

class KintoneClient:
    BASE_URL = "https://XXXXXXXXXX.cybozu.com/k/v1/"

    def __init__(self, api_token: str, app_id: int):
        self.api_token = api_token
        self.app_id = app_id

    def post(self, endpoint: str, params: dict):
        url = f"{self.BASE_URL}{endpoint}.json"
        headers = {
            "X-Cybozu-API-Token": self.api_token,
            "Content-Type": "application/json"
        }
        params["app"] = self.app_id
        resp = requests.post(url, json=params, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.BASE_URL}{endpoint}.json"
        headers = {
            "X-Cybozu-API-Token": self.api_token,
        }
        if params:
            params["app"] = self.app_id
        else:
            params = {"app": self.app_id}
        resp = requests.get(url, params=params, headers=headers)
        resp.raise_for_status()
        return resp.json()
