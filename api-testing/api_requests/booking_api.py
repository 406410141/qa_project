from api_requests.base import BaseAPI


class BookingAPI(BaseAPI):
    def __init__(self, base_url, session):
        super().__init__(base_url, session)

    #GetBookingIds
    def get_booking_ids(self, params=None):
        endpoint = "/booking"

        return self.get(endpoint, params=params)
    #GetBooking
    def get_booking(self,booking_id):
        endpoint = f"/booking/{booking_id}"
        headers = {"Accept": "application/json"}
        return self.get(endpoint, headers=headers)
    #CreateBooking
    def create_booking(self, payload):
        endpoint = "/booking"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        return self.post(endpoint, json=payload, headers=headers)
    #UpdateBooking

    def update_booking(self, booking_id, payload, token):
        endpoint = f"/booking/{booking_id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }
        return self.put(endpoint, json=payload, headers=headers)
    

    #PartialUpdateBooking
    def partial_update_booking(self, booking_id, payload, token):   
        endpoint = f"/booking/{booking_id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }
        return self.patch(endpoint, json=payload, headers=headers)    
    #DeleteBooking
    def delete_booking(self, booking_id, token):
        endpoint = f"/booking/{booking_id}"
        headers = {
            "Cookie": f"token={token}"
        }
        return self.delete(endpoint, headers=headers)   
    #HealthCheck
    def health_check(self):
        endpoint = "/ping"
        return self.get(endpoint)



