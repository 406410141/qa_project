# data/get_booking_data.py（或加入你既有的測資檔中）

INVALID_GET_BOOKING_CASES = [

    (
        "id_is_string", 
        "Brown", 
        404
    ),
    (
        "id_is_boolean", 
        True, 
        404
    )
]