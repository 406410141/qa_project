import pytest
import allure
from api_requests.booking_api import BookingAPI
from data.create_booking_data import INVALID_BOOKING_CASES

@allure.epic("API Testing Project")
@allure.feature("API_CreateBooking")
@allure.story("Create Booking")
@allure.tag("smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_booking_success(base_url, session):

    booking_api = BookingAPI(base_url, session)
    booking_payload = {
        "firstname": "Tony",
        "lastname": "Stark",
        "totalprice": 999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-07-01",
            "checkout": "2026-07-10"
        },
        "additionalneeds": "Mini Fridge"
    }

    response = booking_api.create_booking(booking_payload)

    assert response.status_code == 200
    data = response.json()

    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)
    assert "booking" in data

    booking = data["booking"]
    assert booking["firstname"] == booking_payload["firstname"]
    assert booking["lastname"] == booking_payload["lastname"]
    assert booking["totalprice"] == booking_payload["totalprice"]
    assert booking["depositpaid"] == booking_payload["depositpaid"]
    assert booking["additionalneeds"] == booking_payload["additionalneeds"]
    assert booking["bookingdates"]["checkin"] == booking_payload["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == booking_payload["bookingdates"]["checkout"]



@allure.epic("API Testing Project")
@allure.feature("API_CreateBooking")
@allure.story("Invalid Booking Cases")
@allure.tag("negative")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("test_label, invalid_payload", INVALID_BOOKING_CASES)
def test_create_booking_invalid_inputs(base_url, session, test_label, invalid_payload):

    booking_api = BookingAPI(base_url, session)

    response = booking_api.create_booking(invalid_payload)

    assert response.status_code != 200
