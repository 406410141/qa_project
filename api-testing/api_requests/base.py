import requests
import allure

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
        #response.raise_for_status()
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



"""
  with allure.step(f"Send {method} {endpoint}"):
            # 記錄請求
            allure.attach(f"URL: {url}", "Request URL", allure.attachment_type.TEXT)
            if "params" in kwargs:
                allure.attach(str(kwargs["params"]), "Request Params", allure.attachment_type.TEXT)
            if "json" in kwargs:
                allure.attach(str(kwargs["json"]), "Request JSON", allure.attachment_type.TEXT)
            
            response = self.session.request(method, url, **kwargs)
            
            # 記錄回應
            allure.attach(str(response.status_code), "Response Status", allure.attachment_type.TEXT)
            try:
                allure.attach(response.text, "Response Body", allure.attachment_type.JSON)
            except:
                allure.attach(response.text, "Response Body", allure.attachment_type.TEXT)
            
            return response


"""