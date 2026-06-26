
from api_requests.base import BaseAPI

class AuthAPI(BaseAPI):
    def __init__(self, base_url, session):
        super().__init__(base_url, session)

    def create_token(self,username, password,):

        endpoint = "/auth"
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "username": username,
            "password": password
        }
        return self.post(endpoint, json=payload, headers=headers)
