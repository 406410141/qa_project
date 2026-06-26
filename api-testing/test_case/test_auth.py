import pytest
from api_requests.auth_api import AuthAPI


def test_create_token(base_url, session):
    auth = AuthAPI(base_url, session)
    response = auth.create_token("admin", "password123")
    assert response.status_code == 200
    assert "token" in response.json()
