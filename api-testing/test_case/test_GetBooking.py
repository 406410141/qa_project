import pytest
from api_requests.booking_api import BookingAPI
from api_requests.auth_api import AuthAPI
from api_requests.base import BaseAPI
from data.get_booking_data import INVALID_GET_BOOKING_CASES 


def test_get_booking(base_url, session,created_booking):
    booking_api = BookingAPI(base_url, session)
    target_id = created_booking["booking_id"]
    response = booking_api.get_booking(target_id)
    

    assert response.status_code == 200
    booking = response.json()
    assert isinstance(booking, dict)
    assert booking["firstname"] == created_booking["firstname"]
    assert booking["lastname"] == created_booking["lastname"]
    assert booking["totalprice"] == created_booking["totalprice"]
    assert booking["depositpaid"] == created_booking["depositpaid"]
    assert booking["additionalneeds"] == created_booking["additionalneeds"]
    assert "bookingdates" in booking
    assert booking["bookingdates"]["checkin"] == created_booking["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == created_booking["bookingdates"]["checkout"]

def test_get_booking_not_found(base_url, session):
    booking_api = BookingAPI(base_url, session)
    response = booking_api.get_booking(99999)
    assert response.status_code == 404


@pytest.mark.parametrize("test_label, invalid_id, expected_status", INVALID_GET_BOOKING_CASES)
def test_get_booking_invalid_inputs(base_url, session, test_label, invalid_id, expected_status):
    booking_api = BookingAPI(base_url, session)
    
    response = booking_api.get_booking(invalid_id)
    
    print(f"\nGET Wrong ID Test : {test_label}， Send ID : {invalid_id}")
    
    assert response.status_code == expected_status