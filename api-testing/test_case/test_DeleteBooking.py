import  pytest
from api_requests.booking_api import BookingAPI
from api_requests.auth_api import AuthAPI
from api_requests.base import BaseAPI


def test_delete_booking(base_url, session, auth_token):
    booking_api = BookingAPI(base_url, session)
    booking_payload = {
        "firstname": "Bruce",
        "lastname": "Wayne",
        "totalprice": 888,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-05"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = booking_api.create_booking(booking_payload)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]
    
    delete_response = booking_api.delete_booking(booking_id, auth_token)
    assert delete_response.status_code == 201
    get_response = booking_api.get_booking(booking_id)
    assert get_response.status_code == 404

def test_delete_booking_not_found(base_url, session, auth_token):
    booking_api = BookingAPI(base_url, session)
    delete_response = booking_api.delete_booking(99999, auth_token)
    assert delete_response.status_code == 405


def test_delete_booking_unauthorized(base_url, session):
    booking_api = BookingAPI(base_url, session)
    booking_payload = {
        "firstname": "NoAuth",
        "lastname": "Test",
        "totalprice": 777,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-09-01",
            "checkout": "2026-09-05"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = booking_api.create_booking(booking_payload)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]
    
    delete_response = booking_api.delete_booking(booking_id, "")
    
    assert delete_response.status_code == 403

    get_response = booking_api.get_booking(booking_id)
    assert get_response.status_code == 200