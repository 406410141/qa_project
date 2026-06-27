import pytest
from api_requests.booking_api import BookingAPI


def test_update_booking(base_url, session, created_booking, auth_token):
    booking_api = BookingAPI(base_url, session)
    target_id = created_booking["booking_id"]
    update_payload = {
        "firstname": "Update",
        "lastname": "Test",
        "totalprice": 888,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }

    response = booking_api.update_booking(target_id, update_payload, auth_token)
    assert response.status_code == 200
    data = response.json()

    assert data["firstname"] == update_payload["firstname"]
    assert data["lastname"] == update_payload["lastname"]
    assert data["totalprice"] == update_payload["totalprice"]
    assert data["depositpaid"] == update_payload["depositpaid"]
    assert data["additionalneeds"] == update_payload["additionalneeds"]
    assert data["bookingdates"]["checkin"] == update_payload["bookingdates"]["checkin"]
    assert data["bookingdates"]["checkout"] == update_payload["bookingdates"]["checkout"]

    response_get = booking_api.get_booking(target_id)
    assert response_get.status_code == 200
    data_get = response_get.json()

    assert data_get == data


def test_update_booking_with_invalid_token(base_url, session, created_booking):
    booking_api = BookingAPI(base_url, session)

    target_id = created_booking["booking_id"]

    update_payload = {
        "firstname": "Invalid",
        "lastname": "Token",
        "totalprice": 999,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"},
        "additionalneeds": "Nothing"
    }

    invalid_token_header = {"Cookie": "token=invalid_token_12345_xyz"}

    response = booking_api.update_booking(target_id, update_payload, invalid_token_header)

    print(f"\n RunningPUT Wrong Token Testing . ID : {target_id}，Response Code: {response.status_code}")

    assert response.status_code == 403
