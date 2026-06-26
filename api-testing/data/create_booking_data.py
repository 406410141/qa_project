

INVALID_BOOKING_CASES = [
    # Case 1:  Don't Have lastname 
    (
        "missing_lastname", 
        {"firstname": "Bruce", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"}}
    ),


    # Case 2: wrong totalprice 
    (
        "wrong_totalprice_type", 
        {"firstname": "Bruce", "lastname": "Wayne", "totalprice": "one_hundred", "depositpaid": True, "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"}}
    ),
    # Case 3: Wrong depositpaid  bug
    (
        "wrong_depositpaid_type",  
        {"firstname": "Bruce", "lastname": "Wayne", "totalprice": 100, "depositpaid": "Yes", "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"}}
    ),

    (
        "wrong_bookingdates_format", 
        {"firstname": "Bruce", "lastname": "Wayne", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "not-a-date", "checkout": "2026-01-02"}}
    ),
    # Case 4: Empty
    (
        "empty_booking", 
        {}
    ),
    (
        #Case 5:invalid first name 
        #expect 500 Internal Server Error or 400 Bad Request
        "invalid_firstname_type",
        {
            "firstname": 123, 
            "lastname": "Wayne", 
            "totalprice": 100, 
            "depositpaid": True, 
            "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"}
        }
    ),
    (
        #POST create booking with invalid model
        "invalid_booking_model",
        {
            "invalid_model": "This is not a valid booking model"
        }
    )
]


