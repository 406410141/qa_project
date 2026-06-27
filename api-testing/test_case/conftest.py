import pytest
import requests
from api_requests.auth_api import AuthAPI
from api_requests.booking_api import BookingAPI


@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def session():
    with requests.Session() as s:
        yield s


@pytest.fixture(scope="session")
def auth_token(base_url, session):
    auth = AuthAPI(base_url, session)
    response = auth.create_token("admin", "password123")
    return response.json()["token"]


@pytest.fixture(scope="function")
def created_booking(base_url, session):
    booking_api = BookingAPI(base_url, session)
    data = {
        "firstname": "Happy",
        "lastname": "Test",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    response = booking_api.create_booking(data)
    booking_id = response.json()["bookingid"]
    booking = response.json()["booking"]
    bookingdates = booking["bookingdates"]
    return {
        "booking_id": booking_id,
        "firstname": booking["firstname"],
        "lastname": booking["lastname"],
        "totalprice": booking["totalprice"],
        "depositpaid": booking["depositpaid"],
        "bookingdates": booking["bookingdates"],
        "additionalneeds": booking["additionalneeds"],
        "checkin": bookingdates["checkin"],
        "checkout": bookingdates["checkout"]


    }
