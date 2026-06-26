import pytest
from api_requests.booking_api import BookingAPI
from api_requests.auth_api import AuthAPI
from api_requests.base import BaseAPI


def test_partial_update_booking(base_url, session, created_booking, auth_token):
    booking_api = BookingAPI(base_url, session)
    target_id = created_booking["booking_id"]
    partial_update_payload = {
        "firstname": "PartialUpdate",
        "totalprice": 777
    }
    
    response = booking_api.partial_update_booking(target_id, partial_update_payload, auth_token)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == partial_update_payload["firstname"]
    assert data["totalprice"] == partial_update_payload["totalprice"]


    response_get = booking_api.get_booking(target_id)
    assert response_get.status_code == 200
    data_get = response_get.json()
    

    assert data_get == data