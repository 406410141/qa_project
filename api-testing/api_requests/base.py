import requests


class BaseAPI:
    def __init__(self, base_url, session=None):
        self.base_url = base_url.rstrip("/")
        self.session = session if session else requests.Session()

    def _send_request(self, method, endpoint, **kwargs):
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        print(f"[Response] Status: {response.status_code}")
        print(f"[Response Body] {response.text}")
        # response.raise_for_status()
        return response

    def get(self, endpoint, **kwargs):

        return self._send_request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._send_request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._send_request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self._send_request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._send_request("DELETE", endpoint, **kwargs)
