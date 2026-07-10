import pytest
import allure
from api_requests.booking_api import BookingAPI
from api_requests.auth_api import AuthAPI
from api_requests.base import BaseAPI

@allure.epic("API Testing Project")
@allure.feature("API_GetBookingIds")
@allure.story("Get Booking Ids")
@allure.tag("smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_booking_ids(base_url, session):
    booking_api = BookingAPI(base_url, session)
    response = booking_api.get_booking_ids()
    assert response.status_code == 200
    booking_ids = response.json()
    elapsed = response.elapsed.total_seconds()

    allure.attach(
        f"{elapsed:.3f} seconds",
        name="Response Time",
        attachment_type=allure.attachment_type.TEXT
    )
    assert elapsed < 0.95, f"Response Time too Long：{elapsed:.2f}s（Standerd 0.95s）"
    assert isinstance(booking_ids, list)

@allure.epic("API Testing Project")
@allure.feature("API_GetBookingIds")
@allure.story("Get Booking Ids With Name")
@allure.tag("smoke")
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_ids_with_name(base_url, session, created_booking):
    booking_api = BookingAPI(base_url, session)
    target_id = created_booking["booking_id"]
    target_firstname = created_booking["firstname"]
    target_lastname = created_booking["lastname"]
    query_params = {
        "firstname": target_firstname,
        "lastname": target_lastname
    }
    response = booking_api.get_booking_ids(params=query_params)

    assert response.status_code == 200
    booking_ids = response.json()
    ids = [item["bookingid"] for item in booking_ids]
    assert target_id in ids
    print(f"Booking IDs retrieved: {booking_ids}")
    print(f"Target Booking ID: {target_id}")
    assert isinstance(booking_ids, list)
    assert len(booking_ids) > 0

@allure.epic("API Testing Project")
@allure.feature("API_GetBookingIds")
@allure.story("Get Booking Ids With Date Range")
@allure.tag("smoke")
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_ids_by_date_range(base_url, session, created_booking):
    booking_api = BookingAPI(base_url, session)
    target_id = created_booking["booking_id"]
    checkin_date = "2025-12-31"
    checkout_date = "2026-01-02"
    query_params = {
        "checkin": checkin_date,
        "checkout": checkout_date
    }
    response = booking_api.get_booking_ids(params=query_params)

    assert response.status_code == 200
    booking_ids = response.json()
    assert isinstance(booking_ids, list)
    ids = [item["bookingid"] for item in booking_ids]
    assert target_id in ids
    print(f"Booking IDs retrieved: {booking_ids}")
    print(f"Target Booking ID: {target_id}")
